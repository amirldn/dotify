import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from dotify.api_keys import *

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
        tuple_return = (track_name, " - ", track_artist)
        return "".join(tuple_return)
    except:
        print("An error occurred as follows; ")
        return None

def pull_playlist_info(spotify_uri):
    playlist_info = sp.playlist(spotify_uri, fields="name,owner,tracks,next")
    return playlist_info

def pull_playlist_name_spotify(spotify_playlist_sp):
    playlist_info = spotify_playlist_sp
    name = playlist_info.get("name")
    owner = playlist_info.get("owner").get("display_name")
    tuple_return = (name, " by ", owner)
    return "".join(tuple_return)

def pull_playlist_songs_list_spotify(spotify_playlist_sp):
    list_of_songs_return = []
    for i, item in enumerate(spotify_playlist_sp['tracks']['items']):
        track = item['track']
        tuple_append = (track['name'], " - ", track['artists'][0]['name'])
        list_of_songs_return.append("".join(tuple_append))
    return list_of_songs_return


def print_playlist_songs_spotify(spotify_playlist_sp):
    print("   %s %32.32s %s" %
         ("*", spotify_playlist_sp.get("name"), spotify_playlist_sp.get("owner").get("display_name")))
    for i, item in enumerate(spotify_playlist_sp['tracks']['items']):
        track = item['track']
        print(
            "   %d %32.32s %s" %
            (i, track['artists'][0]['name'], track['name']))