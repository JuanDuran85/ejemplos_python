"""_summary_

    Trabajando con la libreria setuptools
    
    Permite empaquetar un archivo para crear una libreria instalable

    se debe ejecutar en la terminal con sdist al final

"""

from setuptools import setup

setup(
    name='functionsExample',
    version="1.0",
    description='Creando una libreria ejemplo de funciones',
    author='Juan Duran',
    author_email="duran85juan@gmail.com", 
    url='https://github.com/JuanDuran85',
    packages=['libreria_ejemplo'],
)