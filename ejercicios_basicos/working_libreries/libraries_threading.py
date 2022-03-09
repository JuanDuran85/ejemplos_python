"""_summary_

    Libreria para crear hilos: Thread
    Esto permite gestionatr multiples operaciones concurrentes dentro un proceso.

"""


from threading import Thread

def worker(command: list) -> None:
    for i in range(command):
        print(f"Thread {i} - funcionando")

new_hilo: Thread = Thread(target=worker, args=(10,))
new_hilo.start()