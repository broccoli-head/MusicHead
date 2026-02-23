# 🎧 MusicHead - opinie o muzyce 🎧 

Strona jest oparta o framework Django. Głównym zamierzeniem projektu jest szukanie piosenek, sprawdzanie ich szczegółow oraz dodawanie pod nimi opinii. 
<br><br>
![screen1](https://github.com/user-attachments/assets/d91ddfab-a7c3-4389-9d9e-de58e679dd24)
![screen2](https://github.com/user-attachments/assets/61b3c3e6-5a88-44ef-bfca-f12bae30ac24)

### 👉 [Link do filmu przedstawiającego działanie strony](https://youtu.be/bcpdn79W188) 📽️<br><br>

# ❗ WAŻNE ❗
### 1. Migracje
Przy pierwszym użyciu, gdy nie ma danych w bazie, należy wykonać migracje:
```
python manage.py makemigrations strona
python manage.py migrate strona
```
lub jeżeli występują błędy:
```
python manage.py makemigrations
python manage.py migrate
```

### 2. WYMAGANE BIBLIOTEKI 
Aby pobrać wszystkie biblioteki, wystarczy w terminalu wpisać:<br>
```pip install -r requirements.txt```
<br><br>

### 3. KLUCZ SPOTIFY
Aby API Spotify poprawnie działało, konieczne jest:
1. Utworzenie za darmo własnej aplikacji [pod tym linkiem](https://developer.spotify.com/).
2. Dodanie do pliku settings.py kluczy aplikacji: ```SPOTIFY_CLIENT_ID``` oraz ```SPOTIFY_CLIENT_SECRET```
<br><br>
# ⚙️ FUNKCJONALNOŚĆ ⚙️
Główne funkcje strony:
- system kont
- dodawanie piosenek do lokalnej bazy danych
- strona główna z listą ostatnio dodanych utworów
- szukanie piosenek po tytule, artyście lub albumie
- wyszukiwanie utworów w bazie Spotify
- dodawanie opinii do piosenek w formie gwiazdek od 1 do 5 oraz komentarzy
<br><br>
# 👇 UŻYTE TECHNOLOGIE 👇
- HTML
- JavaScript
- CSS
- Python (biblioteki: **Django**, **Pillow** - do obsługi zdjęć, **Spotipy** - do integracji z API Spotify)
- SQLite
<br><br>
### CAŁY KOD JEST PRACĄ WŁASNĄ!

© 2025 Łukasz Rudowski

