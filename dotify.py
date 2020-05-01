import re

from spotifyHandle import pull_track_artist_spotify
from youtubeHandle import yt_return_first_result, yt_dl_then_convert

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
    print("Playlist detected, this feature is coming soon")
else:
    print("Non-Spotify link detected, searching for the track name provided on YouTube")
    currentTrackName = user_songInput
    current_YT_link = yt_return_first_result(currentTrackName)
    yt_dl_then_convert(current_YT_link)





# DEBUG
# user_mode = int(input("Playlist or Individual Song Mode? "))
# if user_mode == 1:
#     print("playlist mode coming soon")
# else:
#     user_songInput = input("Enter a Spotify URI/URL or just the name of song: ")
#     if re.match(r"\Aspotify:|\Ahttp://open|\Ahttps://open", user_songInput) or user_songInput == "i":
#         print("Matched to a spotify link")
#         if user_songInput == "i":
#             user_songInput = "spotify:track:64T3mDRHqtchar88NZ4Bnf"
#         currentTrackName = pull_track_artist_spotify(user_songInput)
#         current_YT_link = yt_return_first_result(currentTrackName)
#         yt_dl_then_convert(current_YT_link)
#     else:
#         currentTrackName = user_songInput
#         current_YT_link = yt_return_first_result(currentTrackName)
#         yt_dl_then_convert(current_YT_link)
