"""_summary_

    Working with shutil library

"""

import shutil

# If you need to figure out where a terminal application is installed
print(shutil.which('python3'))

# if you need a function for moving a file from one location to another
shutil.move('/home/juan/Descargas/programacion/ejemplos_python/texto_mover.txt', '/home/juan/Descargas/programacion/ejemplos_python/tricks_tips')