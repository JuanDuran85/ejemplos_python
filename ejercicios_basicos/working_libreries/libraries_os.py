"""_summary_

    Working with library os

"""

import os

PRINCIPAL_DIR: str = "/home/juan/Descargas/programacion/ejemplos_python/"

# get environment variables
print(os.environ)
print(os.environ['PATH'])
print(os.environ['HOME'])
#print(os.environ['HOSTNAME'])
print(os.environ['PWD'])
print(os.environ['LANG'])
print(os.environ['TERM'])
print(os.environ['SHELL'])
print(os.getcwd())

# get LANG variable without KeyError
print(os.environ.get('LANG'))

# set enviroment variables
os.environ['MY_VAR'] = 'my_value'

# create a new directory
os.mkdir("/home/juan/Descargas/programacion/ejemplo_os")

# create a new nested directories
os.makedirs('/home/juan/Descargas/programacion/ejemplo_os/nested_dir')

# create a file in a directory
os.mknod('/home/juan/Descargas/programacion/ejemplo_os/file.txt')

# show all directories
print(os.listdir('./'))

# actual directory
print(os.getcwd())

# size directory
print(os.path.getsize(PRINCIPAL_DIR))

# is a directory
print(os.path.isdir(PRINCIPAL_DIR))

# is a file
print(os.path.isdir(PRINCIPAL_DIR))

# change directory
os.chdir("/home/juan/Descargas/programacion/")
print(os.getcwd())
print(os.listdir('./'))

# rename directory
os.rename('/home/juan/Descargas/programacion/ejemplo_os', 'ejemplo_os_renamed')

# delete a file
print(os.getcwd())
print(os.listdir('./'))
os.remove(os.getcwd()+'/ejemplo_os_renamed'+'/file.txt')

# delete a directory
os.rmdir('/home/juan/Descargas/programacion/ejemplo_os_renamed/nested_dir')
os.rmdir('/home/juan/Descargas/programacion/ejemplo_os_renamed')
print(os.getcwd())
print(os.listdir('./'))
