from __future__ import unicode_literals

import youtube_dl
from youtube_search import YoutubeSearch as YTSearch


def yt_return_first_result(track_artist_name):
    if track_artist_name is None:
        print("An error has occured. track_artist_name was none")
        quit(1)
    yts_results = YTSearch(str(track_artist_name), max_results=10).to_dict()
    try:
        yt_video_link = "https://www.youtube.com" + yts_results[0]["link"]
        return yt_video_link
    except:
        print("Link for "+track_artist_name+" could not be found :(")
        return None




def yt_dl_then_convert(link, dir=None):
    # Maybe make it download all at once first and then convert them for speed
    playlist_name='songs'
    if dir is not None:
        playlist_name=dir
    ydl_opts = {
        "format": "bestaudio/best",
        "nocheckcertificate": True,
        "cachedir": "./temp",
        'outtmpl': './'+playlist_name+'/%(title)s.%(ext)s',
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
