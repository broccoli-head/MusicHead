from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg, Q

from .spotify import Spotify
from .models import Piosenka, Statystyki, Opinia


def glowna(request):
    piosenki = Piosenka.objects.order_by('-id')[:10]

    context = {
        'piosenki': piosenki
    }
    return render(request, "strona/glowna.html", context)



def rejestracja(request):

    if request.method == 'POST':
        formularz = UserCreationForm(request.POST)
        if formularz.is_valid():
            uzytkownik = formularz.save()
            Statystyki.objects.create(uzytkownik = uzytkownik)
            login(request, uzytkownik)
            return redirect('/')
    else:
        formularz = UserCreationForm()

    return render(request, 'strona/rejestracja.html', {'form': formularz})



def zaloguj(request):

    if request.method == 'POST':
        formularz = AuthenticationForm(data = request.POST)
        if formularz.is_valid():
            uzytkownik = formularz.get_user()
            login(request, uzytkownik)
            
            if not request.POST.get('zapamietaj'):
                request.session.set_expiry(0)
            else:
                request.session.set_expiry(31536000)
            return redirect('/')
    else:
        formularz = AuthenticationForm()
    return render(request, 'strona/login.html', {'form': formularz})


def wyloguj(request):
    logout(request)
    return redirect('/')


def dodaj_piosenke(request):
 
    if request.method == 'POST':
        tytul = request.POST.get("tytul")
        wykonawcy = request.POST.get("wykonawcy")
        album = request.POST.get("album")
        gatunek = request.POST.get("gatunek")

        if not tytul or not wykonawcy:
            wiadomosc = "Pola tytuł oraz wykonawcy są obowiązkowe!"
            return render(request, "strona/dodaj.html", {"wiadomosc": wiadomosc});
    
        if Piosenka.objects.filter(tytul=tytul, wykonawcy=wykonawcy).exists():
            wiadomosc = f'Piosenka o tytule "{tytul}" artysty {wykonawcy} istnieje już w bazie danych!'
            return render(request, "strona/dodaj.html", {"wiadomosc": wiadomosc});  
    
        if len(tytul) > 255 or len(wykonawcy) > 255 or len(album) > 255 or len(gatunek) > 100:
            wiadomosc = f'Wartości nie mogą być dłuższe niż 255 znaków!'
            return render(request, "strona/dodaj.html", {"wiadomosc": wiadomosc}); 


        data = request.POST.get("data") if request.POST.get("data") else None   #bez tej linii wyrzuca błąd invalid format data jezeli pole jest puste

        piosenka = Piosenka(
            tytul = tytul,
            wykonawcy = wykonawcy,
            album = album,
            gatunek = gatunek,
            data = data,
            link = request.POST.get("link"),
            okladka = request.FILES.get("okladka")
        )
        piosenka.save()

        dane = Statystyki.objects.get(uzytkownik = request.user)
        dane.iloscPiosenek += 1
        dane.save()
        
    return render(request, "strona/dodaj.html")



def szukaj(request):
    zapytanie = request.GET.get('q', '')
    wynikiLokalne = Piosenka.objects.filter(
        Q(tytul__icontains = zapytanie) | Q(wykonawcy__icontains = zapytanie) | Q(album__icontains = zapytanie)
    )[:30] if zapytanie else []
    
    wynikiSpotify = Spotify.szukaj(zapytanie)
    context = {
        'zapytanie': zapytanie,
        'wynikiLokalne': wynikiLokalne,
        'wynikiSpotify': wynikiSpotify
    }
    return render(request, 'strona/szukaj.html', context)    



def informacje(request, piosenkaID):
    
    okladka = None
    if not piosenkaID.isdigit():
        piosenka = Spotify.informacje(piosenkaID)
        okladka = piosenka.get('okladka')
    else:
        piosenka = get_object_or_404(Piosenka, id = piosenkaID)
        okladka = piosenka.okladka.url if piosenka.okladka else None

    wiadomosc = ""
    listaOpinii = Opinia.objects.filter(idPiosenki = piosenkaID)
    iloscOpinii = listaOpinii.count()

    srednia = listaOpinii.aggregate(Avg('ocena'))['ocena__avg']
    if srednia is None:
        srednia = 0


    if request.user.is_authenticated:
        opiniaUzytkownika = Opinia.objects.filter(uzytkownik = request.user, idPiosenki = piosenkaID).first()
        opinieInnych = listaOpinii.exclude(uzytkownik = request.user)
    else:
        opiniaUzytkownika = ""
        opinieInnych = Opinia.objects.filter(idPiosenki = piosenkaID)
    

    if not opinieInnych and opiniaUzytkownika:
        opinieWiadomosc = "Jesteś jedyną osobą, która oceniła tą piosenkę."
    else:
        opinieWiadomosc = "Ta piosenka nie ma jeszcze żadnych opinii. Bądź pierwszy!"


    if request.method == 'POST':
        if opiniaUzytkownika:
            if request.POST.get("usunOpinie") == "1":
                dane = Statystyki.objects.get(uzytkownik = request.user)
                if dane.iloscOcen > 0:
                    dane.iloscOcen -= 1

                if opiniaUzytkownika.komentarz and dane.iloscKomentarzy > 0:
                    dane.iloscKomentarzy -= 1
                
                dane.save()
                opiniaUzytkownika.delete()
                return redirect('strona:informacje', piosenkaID)
            
            else:
                wiadomosc = "Już dodałeś opinię do tej piosenki!"
            
        else:
            ocena = request.POST.get("ocena")
            komentarz = request.POST.get("komentarz")
            
            if ocena:
                try:
                    numer = float(ocena)
                    
                    if numer != int(numer) or not (1 <= int(numer) <= 5):
                        wiadomosc = "Ocena musi być liczbą całkowitą od 1 do 5!"
                    elif len(komentarz) > 500:
                        wiadomosc = "Komentarz nie może mieć więcej niż 500 znaków!"

                    else:
                        opinia = Opinia.objects.create(
                            idPiosenki = piosenkaID, uzytkownik = request.user,
                            ocena = numer, komentarz = komentarz
                        )
            
                        dane = Statystyki.objects.get(uzytkownik = request.user)
                        dane.iloscOcen += 1
                        
                        if komentarz:
                            dane.iloscKomentarzy += 1
                        
                        dane.save()
                        return redirect('strona:informacje', piosenkaID)

                except ValueError:
                    wiadomosc = "Ocena musi być liczbą!"
            else:
                wiadomosc = "Musisz podać ocenę!"


    context = {
        "piosenka": piosenka,
        "okladka": okladka,
        "srednia": srednia,
        "iloscOpinii": iloscOpinii,
        "opinie": opinieInnych,
        "iloscGwiazdek": range(1, 6),
        "wiadomosc": wiadomosc,
        "opiniaUzytkownika": opiniaUzytkownika,
        "opinieWiadomosc": opinieWiadomosc
    }
    return render(request, 'strona/informacje.html', context)



def profil(request, nazwaUzytkownika):
    uzytkownik = get_object_or_404(User, username = nazwaUzytkownika)
    dane = Statystyki.objects.get(uzytkownik = uzytkownik)
    
    context = {
        "uzytkownik": uzytkownik,
        "dane": dane
    }

    return render(request, "strona/profil.html", context)