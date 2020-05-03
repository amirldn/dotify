import re

from dotify.spotifyHandle import *
from dotify.youtubeHandle import *


def start():
    user_songInput = input("Enter a Spotify URI/URL or name of an individual song or (q) to quit: ")
    if re.match(
            r"\Aspotify:track|\Ahttp://open.spotify.com/track|\Ahttps://open.spotify.com/track|open.spotify.com/track",
            user_songInput) or user_songInput == "i":
        print("Spotify Track")
        if user_songInput == "i":
            user_songInput = "spotify:track:64T3mDRHqtchar88NZ4Bnf"
        currentTrackName = pull_track_artist_spotify(user_songInput)
        current_YT_link = yt_return_first_result(currentTrackName)
        print(currentTrackName)
        print(current_YT_link)
        yt_dl_then_convert(current_YT_link)
    elif re.match(
            r"\Aspotify:playlist|\Ahttp://open.spotify.com/playlist|\Ahttps://open.spotify.com/playlist|open.spotify.com/playlist",
            user_songInput) or user_songInput == "p":
        yt_links = []
        yt_failed_tracks = []
        print("Spotify Playlist")
        if user_songInput == "p":
            user_songInput = "spotify:playlist:6Zun9zueSjc3OMcJu15nbV"
        playlist_info = pull_playlist_info(user_songInput)
        print(pull_playlist_name_spotify(playlist_info))
        print_playlist_songs_spotify(playlist_info)
        for song in pull_playlist_songs_list_spotify(playlist_info):
            link = yt_return_first_result(song)
            if link is not None:
                yt_links.append(link)
            else:
                yt_failed_tracks.append(song)
        print(yt_links)
        print(yt_failed_tracks)

    elif user_songInput == "q":
        return "quit"
    else:
        print("Searching " + user_songInput + "on YouTube...")
        currentTrackName = user_songInput
        current_YT_link = yt_return_first_result(currentTrackName)
        yt_dl_then_convert(current_YT_link)


while True:
    if start() == "quit":
        break


print("Thank you for using dotify!")
print("https://github.com/amirmaula/dotify")