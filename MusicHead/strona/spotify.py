import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.conf import settings

class Spotify:

    sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(
        client_id = settings.SPOTIFY_CLIENT_ID,
        client_secret = settings.SPOTIFY_CLIENT_SECRET,
    ))


    @staticmethod
    def szukaj(fraza):
        spotifyWyniki = []
        wyniki = Spotify.sp.search(q = fraza, type = "track", limit = 10)

        for piosenka in wyniki['tracks']['items']:
            spotifyWyniki.append({
                'idPiosenki': piosenka['id'],
                'tytul': piosenka['name'],
                'wykonawcy': ', '.join(artist['name'] for artist in piosenka['artists']),
                'okladka': piosenka['album']['images'][0]['url'] if piosenka['album']['images'] else None,
            })
        return spotifyWyniki
    

    @staticmethod
    def informacje(piosenkaID):
        piosenka = Spotify.sp.track(piosenkaID)
        
        # do ustalenia czasu trwania piosenki
        milisekundy = piosenka['duration_ms']
        minuty = (milisekundy // 1000) // 60
        sekundy = (milisekundy // 1000) % 60
        czas = f"{minuty}:{sekundy:02d}"

        wykonawca = Spotify.sp.artist(piosenka['artists'][0]['id'])
        gatunki = wykonawca.get('genres', [])[:2]
        
        szczegolyPiosenki = {
            'id': piosenka['id'],
            'tytul': piosenka['name'],
            'wykonawcy': ', '.join(artist['name'] for artist in piosenka['artists']),
            'okladka': piosenka['album']['images'][0]['url'] if piosenka['album']['images'] else None,
            'album': piosenka['album']['name'],
            'czas': czas,
            'gatunek': ", ".join(gatunki),
            'data': piosenka['album']['release_date'],
            'link': piosenka['external_urls']['spotify']
        }

        return szczegolyPiosenki