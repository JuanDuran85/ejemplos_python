"""_summary_

    Using eyed3 library to read mp3 files

"""

import eyed3

path_file: str = "/home/juan/Descargas/programacion/ejemplos_python/Brendel, Alfred, piano (Philips 12-1987)-07-Allegretto in C minor, D. 915.mp3"

try:
    id3 = eyed3.load(path_file)
    print(id3.tag.artist)
    print(id3.tag.album)
    print(id3.tag.title)
    print(id3.tag.track_num)
    print(id3.tag.genre)
    print(id3.tag.release_date)
except Exception as e:
    print(f"Error: {e}")
