from youtube_search import YoutubeSearch  as yts

from spotifyHandle import pull_track_artist

#Return track name and track artist(s) from spotify link

user_SpotifyURI = input("Enter a Spotify URI: ")
if user_SpotifyURI == "i":
    user_SpotifyURI = "spotify:track:64T3mDRHqtchar88NZ4Bnf"

currentTrack = pull_track_artist(user_SpotifyURI)
print(currentTrack)

yts_results = yts(str(currentTrack), max_results=10).to_dict()
print(yts_results)

#Take first result
print(type(yts_results))
videoLink =  ('https://www.youtube.com' + yts_results[0]['link'])
print(videoLink)