from __future__ import unicode_literals

import youtube_dl
from youtube_search import YoutubeSearch as YTSearch


def yt_return_first_result(track_artist_name):
    if track_artist_name is None:
        print("An error has occured. track_artist_name was none")
        quit(1)
    yts_results = YTSearch(str(track_artist_name), max_results=10).to_dict()
    yt_video_link = "https://www.youtube.com" + yts_results[0]["link"]
    return yt_video_link


def yt_dl_then_convert(link):
    # Maybe make it download all at once first and then convert them for speed
    ydl_opts = {
        "format": "bestaudio/best",
        "nocheckcertificate": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "328",
            }
        ],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
