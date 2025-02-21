from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Piosenka(models.Model):
    tytul = models.CharField(max_length=255)
    wykonawcy = models.CharField(max_length=255)
    album = models.CharField(max_length=255, blank=True)
    gatunek = models.CharField(max_length=100, blank=True)
    data = models.DateField(blank=True, null=True)
    link = models.URLField(blank=True)
    okladka = models.ImageField(upload_to="okladki/", blank=True, null=True)

    def __str__(self):
        return f"{self.tytul} - {self.wykonawcy}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.okladka:
            sciezka = self.okladka.path
            zdjecie = Image.open(sciezka)
            zdjecie = zdjecie.resize((300, 300), Image.Resampling.LANCZOS)   #zmniejszamy do 300x300px zeby rozmiar zdjecia byl mniejszy
            zdjecie.save(sciezka)


class Statystyki(models.Model):
    uzytkownik = models.OneToOneField(User, on_delete = models.CASCADE)
    iloscOcen = models.PositiveIntegerField(default = 0)
    iloscKomentarzy = models.PositiveIntegerField(default = 0)
    iloscPiosenek = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return f"Dane: {self.uzytkownik}"


class Opinia(models.Model):
    idPiosenki = models.CharField(max_length = 50)
    uzytkownik = models.ForeignKey(User, on_delete = models.CASCADE)
    ocena = models.PositiveIntegerField()
    komentarz = models.TextField(blank = True)
    data = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Recenzja: {self.uzytkownik} - {self.data}"