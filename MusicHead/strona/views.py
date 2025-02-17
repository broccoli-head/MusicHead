from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

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
    zalogowany = True if request.user.is_authenticated else False
    
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
        
    return render(request, "strona/dodaj.html", {'zalogowany': zalogowany})


def informacje(request, piosenkaID):
    piosenka = Piosenka.objects.get(id = piosenkaID)
    wiadomosc = ""
    zalogowany = True if request.user.is_authenticated else False

    if request.method == 'POST':
        ocena = request.POST.get("ocena")
        komentarz = request.POST.get("komentarz")
        
        try:
            numer = float(ocena)
            
            if numer != int(numer) or not (1 <= int(numer) <= 5):
                wiadomosc = "Ocena musi być liczbą całkowitą od 1 do 5!"
            elif len(komentarz) > 500:
                wiadomosc = "Komentarz nie może mieć więcej niż 500 znaków!"
            elif Opinia.objects.filter(uzytkownik = request.user, idPiosenki = piosenka.id).exists():
                wiadomosc = "Już oceniłeś tą piosenkę!"

            else:
                opinia = Opinia.objects.create(
                    idPiosenki = piosenka.id, uzytkownik = request.user,
                    ocena = numer, komentarz = komentarz
                )

        except ValueError:
            wiadomosc = "Ocena musi być liczbą!"


    context = {
        "piosenka": piosenka,
        "iloscGwiazdek": range(1, 6),
        "wiadomosc": wiadomosc,
        "zalogowany": zalogowany
    }
    return render(request, 'strona/informacje.html', context)