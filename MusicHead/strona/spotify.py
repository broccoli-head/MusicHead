import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.conf import settings

class Spotify:

    def szukaj(fraza):
        sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(
            client_id = settings.SPOTIFY_CLIENT_ID,
            client_secret = settings.SPOTIFY_CLIENT_SECRET,
        ))
        spotifyWyniki = []
        wyniki = sp.search(q = fraza, type = "track", limit = 10)

        for piosenka in wyniki['tracks']['items']:
            spotifyWyniki.append({
                'idPiosenki': piosenka['id'],
                'tytul': piosenka['name'],
                'wykonawcy': ', '.join(artist['name'] for artist in piosenka['artists']),
                'okladka': piosenka['album']['images'][0]['url'] if piosenka['album']['images'] else None
            })

        return spotifyWyniki