from pytubefix import YouTube
from pytubefix.cli import on_progress

CONT = 0
VALOR_INICIO = 0


def complete_function(stream_in, path):
    """_summary_

    Args:
        stream_in (_type_): _description_
        path (_type_): _description_
    """
    valor = (stream_in.filesize)/1e6
    print("")
    print("-------------------------------------")
    print(f"Total del Tamaño del video descargado: {valor:.2f} MB")
    print(f"Ubicacion: {path}")
    print("Fin de la descarga")


URL = input("Introduce el link de youtube: ")
vide_yt = YouTube(URL, on_progress_callback=on_progress,  # type: ignore
                  on_complete_callback=complete_function)
print(vide_yt.title)
print(f"Titulo del video: {vide_yt.title}")
print("Descargando video...")
stream = vide_yt.streams.get_highest_resolution()
# type: ignore
stream.download(  # type: ignore
    output_path="/Users/juanduran/Documents/codigos_cursos/videos_cursos"
)
