from __future__ import unicode_literals

import youtube_dl
from youtube_search import YoutubeSearch as yts


def yt_return_first_result(track_artist_name):
    yts_results = yts(str(track_artist_name), max_results=10).to_dict()
    videoLink = "https://www.youtube.com" + yts_results[0]["link"]
    return videoLink

def ytDl_and_convert(link):
     # Maybe make it download all at once first and then convert them for speed
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

