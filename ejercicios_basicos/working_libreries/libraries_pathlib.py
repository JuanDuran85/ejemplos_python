# !/usr/bin/python3
# flake8: noqa: E501
# pylint: disable=line-too-long
# pylint: disable=C0103

"""_summary_

    Working with Pathlib.

"""

from pathlib import Path

LINES = "---------------------------------------------------------------------\r"
filename: str = "example_one.pdf"

print("using Pathlib")
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
