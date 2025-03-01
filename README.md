# 🎧 MusicHead - opinie o muzyce 🎧 

Strona jest oparta o framework Django. Głównym zamierzeniem projektu jest szukanie piosenek, sprawdzanie ich szczegółow oraz dodawanie pod nimi opinii. 

📽️ Link do filmu przedstawiającego działanie strony 📽️
https://youtu.be/bcpdn79W188

# ❗ WAŻNE ❗
## 1. MIGRACJE
Przy pierwszym użyciu, gdy nie ma danych w bazie, należy wykonać migrację (w przeciwnym razie wyskakują błędy):
```
python manage.py makemigrations strona
python manage.py migrate strona
```

UWAGA!
Samo ```python manage.py makemigrations``` nie wystarczy, musi być z dopiskiem ```strona```.


## 2. WYMAGANE BIBLIOTEKI 
Strona używa biblioteki **Pillow** do obsługi zdjęć oraz **Spotipy** do integracji ze Spotify.
Należy je pobrać, aby uniknąć błędów.

# ⚙️ FUNKCJONALNOŚĆ ⚙️
Główne funkcje strony:
- system kont
- dodawanie piosenek do lokalnej bazy danych
- strona główna z listą ostatnio dodanych utworów
- szukanie piosenek po tytule, artyście lub albumie
- wyszukiwanie utworów w ogromnej bazie Spotify
- dodawanie opinii do piosenek w formie gwiazdek od 1 do 5 oraz komentarzy

# 👇 UŻYTE TECHNOLOGIE 👇
- HTML
- JavaScript
- CSS
- Python (Django, Pillow, Spotipy)
- SQLite

## CAŁY KOD JEST PRACĄ WŁASNĄ!
© 2025 Łukasz Rudowski