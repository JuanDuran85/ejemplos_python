'''
Docstring for ...
'''

from pathlib import Path
import yt_dlp


def download_one(url_in: str, out_dir: str = "Downloads") -> None:
    '''
    Docstring for download_one

    :param url_in: Description
    :type url_in: str
    :param out_dir: Description
    :type out_dir: str
    '''

    ydl_opts = {
        # you need to use ffmpeg
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best",
        "outtmpl": f'{out_dir}/video01.%(ext)s',
        "noplaylist": True,
        "restrictfilenames": False,
        "overwrites": True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:  # type: ignore
            ydl.download([url_in])
        print(f"\nDownload complete! Saved to {out_dir}")
    except Exception as e:
        print(f"Error: {e}")
        raise e


if __name__ == "__main__":
    print("downloading video")
    url = input("URL del video: ").strip()
    download_one(url)
