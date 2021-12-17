from pytube import YouTube

cont = 0
valor_inicio = 0
def progress_function(chunk, file_handle, bytes_remaining):
    global cont
    global valor_inicio
    global stream
    megas_actuales = (bytes_remaining / 1e6)
    if cont == 0:
        valor_inicio = (stream.filesize)/1e6
    progress = ((megas_actuales * 100)/valor_inicio)
    print(f"Descargando: {megas_actuales:.2f} MB")
    print(f"Por descargar: {int(progress)}%")
    cont += 1
    
def complete_function(stream,path):
    valor = (stream.filesize)/1e6
    print(f"Total del Tamaño del video descargado: {valor:.2f} MB")
    print(f"Ubicacion: {path}")
    print("Descarga completada")

link = input("Introduce el link de youtube: ")
video = YouTube(link, on_progress_callback = progress_function, on_complete_callback = complete_function)
stream = video.streams.get_highest_resolution()
print(f"Titulo del video: {video.title}")
print("Descargando video...")
stream.download(output_path="/home/juan/Descargas/cursos/videos")