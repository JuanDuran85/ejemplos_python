"""_summary_

    Working with library platform
    
    - platform.architecture(executable=sys.executable, bits='', linkage='')
        Consulta el ejecutable provisto (por defecto el archivo binario del intérprete de Python) para obtener información de diversas arquitecturas.
    - platform.machine()
        Retorna el tipo de máquina, por ejemplo 'i386'. Si no se puede determinar el valor, retorna una cadena vacía.
    - platform.node()
        Retorna el nombre de la red del ordenador (¡tal vez no sea el nombre completo!). Si no se puede determinar el valor, se retorna una cadena vacía.
    - platform.platform(aliased=0, terse=0)
        Retorna una sola cadena identificando la plataforma subyacente con la mayor información útil posible.  
    - platform.processor()
        Retorna el nombre (real) del procesador. E.j. 'amdk6'.
    - platform.python_build()
        Retorna una tupla (buildno, builddate) con buildno indicando el número de la build de Python y builddate su fecha de publicación como cadenas.
    - platform.python_compiler()
        Retorna la string con la identificación del compilador usado para compilar Python.
    - platform.python_branch()
        Retorna la string identificando la implementación de la rama SCM de Python.
    - platform.python_implementation()
        Retorna la string identificando la implementación de Python. Algunos valores posibles son: “CPython”, “IronPython”, “Jython”, “PyPy”.
    - platform.python_revision()
        Retorna la string identificando la implementación de la revisión SCM de Python.
    - platform.python_version()
        Retorna la versión de Python en formato de cadena de caracteres con la forma 'major.minor.patchlevel' siendo major la versión principal, minor la versión menor y patchlevel el último parche aplicado.
    - platform.python_version_tuple()
        Retorna la versión de Python como una tupla (major, minor, patchlevel) de cadena, siendo major la versión principal, minor la versión menor y patchlevel último parche aplicado.
    - platform.release()
        Retorna la versión de publicación del sistema. Por ejemplo '2.2.0' o 'NT'. Si no se puede determinar el valor, retorna una cadena vacía.
    - platform.system()
        Retorna el nombre del sistema/SO, como 'Linux', 'Darwin', 'Java', 'Windows'. Si no se puede determinar el valor, retorna una cadena vacía.
    - platform.system_alias(system, release, version)
        Retorna la tupla (system, release, version) con los alias de los nombres comerciales usados por algunos sistemas siendo system el nombre comercial del sistema, release como la versión principal de publicación y version como el número de la versión del sistema.
    - platform.version()
        Retorna la versión de la publicación del sistema. Por ejemplo: '#3 on degas'. Una cadena vacía se retorna en el caso de que el valor no pueda ser determinado.
    - platform.uname()
        Interfaz uname relativamente portable. Retorna una namedtuple() con seis atributos: system, node, release, version, machine, and processor.
        
    Funte: https://docs.python.org/es/3/library/platform.html

"""

import platform

print('\n Inf. tca. del sistema operativo/Procc./otros:')
print(' -> S.O./version: ', platform.uname())


print(' -> Architecture/SO: ', platform.architecture(), platform.win32_ver())
print(' -> Caracteristicas del Procesador: ', platform.processor())
print(' -> Version de  Python: ', platform.python_version())
print(' -> Compilador usado para Python: ', platform.python_compiler())
print(' -> Tipo de máquina: ', platform.machine())

print('freedesktop_os_release ',  platform.freedesktop_os_release())
print('libc_ver ',  platform.libc_ver())
print('uname ',  platform.uname())
print('version ',  platform.version())
print('python_version_tuple ',  platform.python_version_tuple())
print('system ',  platform.system())
print('release ',  platform.release())
print('python_branch ',  platform.python_branch())
print('python_compiler ',  platform.python_compiler())
print('python_build ',  platform.python_build())
print('system_alias ',  platform.system_alias(platform.system(),platform.release(), platform.version()))
