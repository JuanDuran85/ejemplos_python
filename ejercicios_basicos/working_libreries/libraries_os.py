"""_summary_

    Working with library os

"""

import os

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
os.mkdir('/home/juan/Descargas/programacion/ejemplos_python/ejemplo_os')

# create a new nested directories
os.makedirs('/home/juan/Descargas/programacion/ejemplos_python/ejemplo_os/nested_dir')