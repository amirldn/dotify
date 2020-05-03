import re

from spotifyHandle import *
from youtubeHandle import *

user_songInput = input("Enter a Spotify URI/URL or name of an individual song: ")
if re.match(r"\Aspotify:track|\Ahttp://open.spotify.com/track|\Ahttps://open.spotify.com/track|open.spotify.com/track", user_songInput) or user_songInput == "i":
    print("Matched to a Spotfify track detected")
    if user_songInput == "i":
        user_songInput = "spotify:track:64T3mDRHqtchar88NZ4Bnf"
    currentTrackName = pull_track_artist_spotify(user_songInput)
    current_YT_link = yt_return_first_result(currentTrackName)
    print(currentTrackName)
    print(current_YT_link)
    yt_dl_then_convert(current_YT_link)
elif re.match(r"\Aspotify:playlist|\Ahttp://open.spotify.com/playlist|\Ahttps://open.spotify.com/playlist|open.spotify.com/playlist", user_songInput):
    # spotify:playlist:6Zun9zueSjc3OMcJu15nbV
    playlist_info = pull_playlist_info(user_songInput)
    print(pull_playlist_name_spotify(playlist_info))
    print(pull_playlist_songs_list_spotify(playlist_info))
    print_playlist_songs_spotify(playlist_info)
else:
    print("Non-Spotify link detected, searching for the track name provided on YouTube")
    currentTrackName = user_songInput
    current_YT_link = yt_return_first_result(currentTrackName)
    yt_dl_then_convert(current_YT_link)
