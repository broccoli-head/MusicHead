from django.shortcuts import render
from .models import Piosenka

def glowna(request):
    return render(request, "strona/glowna.html")

def dodaj_piosenke(request):
    if request.method == 'POST':
        tytul = request.POST.get("tytul")
        wykonawcy = request.POST.get("wykonawcy")

        if not tytul or not wykonawcy:
            wiadomosc = "Pola tytuł oraz wykonawcy są obowiązkowe!"
            return render(request, "strona/dodaj.html", {"wiadomosc":wiadomosc});
    
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