"""_summary_

    Working with Pathlib.

"""

import pathlib

filename: str = "ejemplo_uno.pdf"

file_type_suffix = pathlib.Path(filename).suffix
print(f"{filename} has the suffix {file_type_suffix}")
print(f"Removing: {filename.removesuffix(file_type_suffix)}")