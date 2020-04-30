import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from api_keys import *

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def stripTitlefromLink(currentSpotifyURI):
    """Provide a Spotify link as string
    and return the Track - Artist Name"""
    currentTrackInfo = sp.track(currentSpotifyURI)
    print(currentTrackInfo)

