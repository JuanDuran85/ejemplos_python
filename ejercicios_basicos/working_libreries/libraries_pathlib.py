# !/usr/bin/python3
# flake8: noqa: E501
# pylint: disable=line-too-long
# pylint: disable=C0103

"""_summary_

    Working with Pathlib.
    Using pathlib makes path manipulation more readable and platform-independent,
    and it offers a more object-oriented approach.
    
    With "pathlib", you can access various parts of a path, such as the filename,
    extension, and parent directory. This makes it easy to manipulate and analyze file paths.
    
    The pathlib expressions are more object-oriented and readable.
"""

from pathlib import Path

LINES = "---------------------------------------------------------------------\r"
filename: str = "example_one.pdf"
PATH_LINK = "C:\\Users\\duran\\Downloads\\codigos_exa\\ejemplos_pythonejercicios_basicos\\working_libreries\\libraries_pathlib.py"
print("using Pathlib")

print(LINES)
print("using Path to get name")
print(Path(PATH_LINK).name)

print(LINES)
print("using Path to get stem")
print(Path(PATH_LINK).stem)

print(LINES)
print("using Path to get suffix")
print(Path(PATH_LINK).suffix)

print(LINES)
print("using Path to get parent")
print(Path(PATH_LINK).parent)

print(LINES)
print("using Path to get the suffix")
file_type_suffix: str = Path(filename).suffix
print(f"{filename} has the suffix {file_type_suffix}")

print(LINES)
print("using Path to remove the suffix")
print(f"Removing: {filename.removesuffix(file_type_suffix)}")

print(LINES)
print("using Path to create a path")
base_path: Path = Path("\\home\\work\\project_one")
file_name = "data.csv"

filepath: Path = base_path / file_name
print(filepath)

print(LINES)
print("using Path to get absolute path")
abs_path: Path = Path(".\\ejemplos_python\\README.md").absolute()
print(abs_path)

print(LINES)
print("using Path to get current path")
current_file_path: Path = Path(__file__).resolve()
print(current_file_path)

print(LINES)
print("using Path to get parent path")
parent_path: Path = Path(__file__).parent
print(parent_path)

print(LINES)
print("using Path to get name")
file_name: str = Path(__file__).name
print(file_name)

print(LINES)
print("Join path components and normalize (remove redundant separators)")
cleaned_path = Path("\\first_path").joinpath("\\second_path", "file.txt").resolve()
print(cleaned_path)
