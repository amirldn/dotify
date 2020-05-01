from spotifyHandle import pull_track_artistSpot
from youtubeHandle import yt_return_first_result, ytDl_and_convert

# Return track name and track artist(s) from spotify link

user_SpotifyURI = input("Enter a Spotify URI: ")
if user_SpotifyURI == "i":
    user_SpotifyURI = "spotify:track:64T3mDRHqtchar88NZ4Bnf"

currentTrackName = pull_track_artistSpot(user_SpotifyURI)
print(currentTrackName)

current_YT_link = yt_return_first_result(currentTrackName)
ytDl_and_convert(current_YT_link)


