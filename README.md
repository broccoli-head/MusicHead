# 🎧 MusicHead - opinie o muzyce 🎧 

Strona jest oparta o framework Django. Głównym zamierzeniem projektu jest szukanie piosenek, sprawdzanie ich szczegółow oraz dodawanie pod nimi opinii. 
<br><br>
<img width="1910" height="1084" alt="image" src="https://github.com/user-attachments/assets/86946c87-fbe7-4bea-a634-bbbb9e00d87c" />

### 👉 [Link do filmu przedstawiającego działanie strony](https://youtu.be/bcpdn79W188) 📽️<br><br>

# ❗ WAŻNE ❗
### 1. Migracje
Przy pierwszym użyciu, gdy nie ma danych w bazie, należy wykonać migrację (w przeciwnym razie wyskakują błędy):
```
python manage.py makemigrations strona
python manage.py migrate strona
```
lub:
```
python manage.py makemigrations
python manage.py migrate
```
**UWAGA!**
<br>```python manage.py makemigrations``` może nie wystarczyć, więc czasem trzeba dodać dopisek ```strona```, jednak gdzieniegdzie było to zbędne i powodowało błędy. Należy spróbować obu opcji.
<br><br>

### 2. WYMAGANE BIBLIOTEKI 
Strona oprócz całego frameworku Django, używa również bibliotek:
- **Pillow** do obsługi zdjęć
- **Spotipy** do integracji ze Spotify.

Wszystkie potrzebne biblioteki znajdują się w pliku ```requirements.txt```. Wystarczy w terminalu wpisać:
<br>```pip install -r requirements.txt```
<br><br>

### 3. KLUCZ SPOTIFY

W settings.py znajdują się klucze aplikacji: ```SPOTIFY_CLIENT_ID``` oraz ```SPOTIFY_CLIENT_SECRET```
<br>Nie gwarantuję ich działania, dlatego warto utworzyć własną aplikację na: https://developer.spotify.com/ a następnie dodać swoje klucze.
<br><br>
# ⚙️ FUNKCJONALNOŚĆ ⚙️
Główne funkcje strony:
- system kont
- dodawanie piosenek do lokalnej bazy danych
- strona główna z listą ostatnio dodanych utworów
- szukanie piosenek po tytule, artyście lub albumie
- wyszukiwanie utworów w ogromnej bazie Spotify
- dodawanie opinii do piosenek w formie gwiazdek od 1 do 5 oraz komentarzy
<br><br>
# 👇 UŻYTE TECHNOLOGIE 👇
- HTML
- JavaScript
- CSS
- Python (Django, Pillow, Spotipy)
- SQLite
<br><br>
### CAŁY KOD JEST PRACĄ WŁASNĄ!

© 2025 Łukasz Rudowski
