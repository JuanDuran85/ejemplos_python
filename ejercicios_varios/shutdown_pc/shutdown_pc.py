import subprocess

shutdown = input("Do you wish to shutdown your computer ? (yes / no): ")

if shutdown == "yes":
    subprocess.run(["shutdown"])