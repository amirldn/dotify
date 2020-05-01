import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from api_keys import *

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def pull_track_artist_spotify(spotify_uri):
    """Provide a Spotify link as string
    and return the Track - Artist Name"""

    try:
        track_info = sp.track(spotify_uri)
        # For more than 1 artist, get the first two artists
        if len(track_info.get("artists")) > 1:
            track_artist = (
                    str(track_info.get("artists")[0].get("name"))
                    + " "
                    + str(track_info.get("artists")[1].get("name"))
            )
        else:
            # Single artist
            track_artist = track_info.get("artists")[0].get("name")

        track_name = track_info.get("name")
        track_artist = track_artist
        track_album = track_info.get("album").get("name")
        track_explicit = track_info.get("explicit")

        # print("Track Name : "+track_name+
        #     #     #       "\n Artist: "+ str(track_artist)+
        #     #     #       "\n Album: "+ track_album+
        #     #     #       "\n Explicit: "+str(track_explicit))

        return track_name, track_artist
    except:
        print("An error occurred as follows; ")
        return None
