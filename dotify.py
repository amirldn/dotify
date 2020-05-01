import re

from spotifyHandle import pull_track_artistSpot
from youtubeHandle import yt_return_first_result, ytDl_and_convert

# Return track name and track artist(s) from spotify link


user_mode = int(input("Playlist or Song Mode? "))
if user_mode == 1:
    print("coming soon")
else:
    user_songInput = input("Enter a Spotify URI or name of song: ")
    if re.match(r"\Aspotify", user_songInput) or user_songInput == "i":
        if user_songInput == "i":
            user_songInput = "spotify:track:64T3mDRHqtchar88NZ4Bnf"
        currentTrackName = pull_track_artistSpot(user_songInput)
        # print(currentTrackName)

        current_YT_link = yt_return_first_result(currentTrackName)
        ytDl_and_convert(current_YT_link)
    else:
        currentTrackName = user_songInput
        current_YT_link = yt_return_first_result(currentTrackName)
        ytDl_and_convert(current_YT_link)







