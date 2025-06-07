# !/usr/bin/python3
# flake8: noqa: E501
# pylint: disable=line-too-long
# pylint: disable=C0103

"""_summary_

    Working with library os

"""

import os
from typing import LiteralString

LINES = "---------------------------------------------------------------------\r"
PRINCIPAL_DIR: str = "C:\\Users\\duran\\Downloads\\codigos_exa\\ejemplos_python"  # type: ignore
SUPER_DIR: str = "C:\\Users\\duran\\Downloads\\codigos_exa"
EXAMPLE_DIR: str = "\\example_os"

# get environment variables

print(LINES)
print("Environment variables")
print(os.environ)
print(LINES)
print("PATH")
print(os.environ['PATH'])
print(LINES)
print("LANG")
print(os.environ['LANG'])
print(LINES)
print("getcwd")
print(os.getcwd())
print(LINES)

# get LANG variable without KeyError
print("Get LANG variable")
print(os.environ.get('LANG'))

# set environment variables
os.environ['MY_VAR'] = 'my_value'

# create a new directory
os.mkdir(PRINCIPAL_DIR + EXAMPLE_DIR)

# create a new nested directories
os.makedirs(PRINCIPAL_DIR + EXAMPLE_DIR + '\\nested_dir')

# create a file in a directory
fd: int = os.open(PRINCIPAL_DIR + '\\example_os\\file.txt', os.O_WRONLY | os.O_CREAT)
os.close(fd)

# show all directories
print("show all directories - listdir")
print(os.listdir('./'))

# actual directory
print("actual directory - getcwd")
print(os.getcwd())

# size directory
print("size directory - getsize")
print(os.path.getsize(PRINCIPAL_DIR))

# is a directory
print("is a directory - isdir")
print(os.path.isdir(PRINCIPAL_DIR))

# is a file
print("is a file - isfile")
print(os.path.isfile(PRINCIPAL_DIR))

# change directory
print("change directory - chdir")
os.chdir(SUPER_DIR)
print(os.getcwd())
print(os.listdir('./'))

# rename directory
print("rename directory - rename")
os.rename(PRINCIPAL_DIR + EXAMPLE_DIR, 'example_os_renamed')

# delete a file
print("delete a file - remove")
print(os.getcwd())
print(os.listdir('./'))
os.remove(os.getcwd()+'/example_os_renamed'+'/file.txt')

# delete a directory
print("delete a directory - rmdir")
os.rmdir(SUPER_DIR + '\\example_os_renamed\\nested_dir')
os.rmdir(SUPER_DIR + '\\example_os_renamed')
print(os.getcwd())
print(os.listdir('./'))

# using path join to avoid errors with a path separator to the base
print("using path join")
file_name = "data_out.csv"
file_path: LiteralString = os.path.join(PRINCIPAL_DIR, file_name)
print(file_path)


# using path abspath to get the absolute path
print("using path abspath")
abs_path: str = os.path.abspath(".\\ejemplos_python\\README.md")
print(abs_path)

# using path realpath to get the real path
print("using path realpath")
current_file_path: str = os.path.realpath(__file__)
print(current_file_path)


# Join path components and normalize (remove redundant separators)
print("using normpath and join")
cleaned_path = os.path.normpath(os.path.join("\\Users\\duran", "..\\Downloads", ".\\data\\file.txt"))
print("cleaned_path:", cleaned_path)
