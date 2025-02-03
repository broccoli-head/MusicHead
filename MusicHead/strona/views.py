from django.shortcuts import render

def glowna(request):
    return render(request, "strona/glowna.html")