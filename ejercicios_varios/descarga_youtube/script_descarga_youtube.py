from pytube import YouTube

def progress_function(chunk, file_handle, bytes_remaining):
    megas = bytes_remaining / 1048576
    print(f"Descargando: {megas:.2f} MB")
    
def complete_function(stream,path):
    print(f"Ubicacion: {path}")
    print("Descarga completada")

link = input("Introduce el link de youtube: ")
video = YouTube(link, on_progress_callback = progress_function, on_complete_callback = complete_function, )
stream = video.streams.get_highest_resolution()
print(f"Titulo del video: {video.title}")
print("Descargando video...")
stream.download(output_path="/home/juan/Descargas/cursos/videos")
