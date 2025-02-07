from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .models import Piosenka

def glowna(request):
    piosenki = Piosenka.objects.order_by('-id')[:10]
    return render(request, "strona/glowna.html", {'piosenki': piosenki})


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
    if not request.user.is_authenticated:
        return render(request, "strona/niezalogowany.html")
    
    if request.method == 'POST':
        tytul = request.POST.get("tytul")
        wykonawcy = request.POST.get("wykonawcy")

        if not tytul or not wykonawcy:
            wiadomosc = "Pola tytuł oraz wykonawcy są obowiązkowe!"
            return render(request, "strona/dodaj.html", {"wiadomosc": wiadomosc});
    
        if Piosenka.objects.filter(tytul=tytul, wykonawcy=wykonawcy).exists():
            wiadomosc = f'Piosenka o tytule "{tytul}" artysty {wykonawcy} istnieje już w bazie danych!'
            return render(request, "strona/dodaj.html", {"wiadomosc": wiadomosc});  
    
        data = request.POST.get("data") if request.POST.get("data") else None   #bez tej linii wyrzuca błąd invalid format data jezeli pole jest puste

        piosenka = Piosenka(
            tytul = tytul,
            wykonawcy = wykonawcy,
            album = request.POST.get("album"),
            gatunek = request.POST.get("gatunek"),
            data = data,
            link = request.POST.get("link"),
            okladka = request.FILES.get("okladka")
        )
        piosenka.save()
        
    return render(request, "strona/dodaj.html")


def informacje(request, piosenkaID):
    piosenka = Piosenka.objects.get(id = piosenkaID)
    return render(request, 'strona/informacje.html', {"piosenka": piosenka})