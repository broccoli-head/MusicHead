from django.shortcuts import render

def glowna(request):
    return render(request, "strona/glowna.html")

def dodaj_piosenke(request):
    return render(request, "strona/dodaj.html");