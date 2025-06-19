# !/usr/bin/python3
# flake8: noqa: E501
# pylint: disable=line-too-long
# pylint: disable=C0103

"""_summary_

    Libreria para crear hilos: Thread
    Esto permite gestionatr multiples operaciones concurrentes dentro un proceso.

"""


from threading import Thread


def worker(command: list) -> None:
    for i in range(command):  # type: ignore
        print(f"Thread {i} - funcionando")


new_hilo: Thread = Thread(target=worker, args=(10,))
new_hilo.start()
