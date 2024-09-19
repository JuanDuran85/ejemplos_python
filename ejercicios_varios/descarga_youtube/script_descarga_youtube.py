from pytube import YouTube

CONT = 0
VALOR_INICIO = 0


def progress_function(_, file_handle, bytes_remaining):
    global CONT
    global VALOR_INICIO
    global stream
    megas_actuales = (bytes_remaining / 1e6)
    if CONT == 0:
        VALOR_INICIO = (stream.filesize)/1e6  # type: ignore
    progress = ((megas_actuales * 100)/VALOR_INICIO)
    print(f"Descargando: {megas_actuales:.2f} MB")
    print(f"Por descargar: {int(progress)}%")
    CONT += 1


def complete_function(stream, path):
    valor = (stream.filesize)/1e6
    print(f"Total del Tamaño del video descargado: {valor:.2f} MB")
    print(f"Ubicacion: {path}")
    print("Descarga completada")


link = input("Introduce el link de youtube: ")
video = YouTube(link, on_progress_callback=progress_function,  # type: ignore
                on_complete_callback=complete_function)  # type: ignore
stream = video.streams.get_highest_resolution()
print(f"Titulo del video: {video.title}")
print("Descargando video...")
# type: ignore
stream.download(  # type: ignore
    output_path="/Users/juanduran/Documents/codigos_cursos/videos_cursos")
