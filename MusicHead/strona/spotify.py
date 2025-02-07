import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.conf import settings

class Spotify:

    def szukaj(fraza):
        sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(
            client_id = settings.SPOTIFY_CLIENT_ID,
            client_secret = settings.SPOTIFY_CLIENT_SECRET,
        ))

        results = sp.search(q = fraza, type = "track", limit = 10)

        for track in results['tracks']['items']:
            title = track['name']
            artists = ", ".join(artist["name"] for artist in track["artists"])
            print(title + " - " + artists)