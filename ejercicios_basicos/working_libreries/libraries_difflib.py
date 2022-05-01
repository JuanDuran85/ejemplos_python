"""_summary_

    Working with difflib library

"""

import difflib
from typing import Iterator

text_one: str = """Mike is a Python blogger.
He writes about Python.
"""
text_two: str = """Mike is a Python blogger.
He writes about Python, and about programming with python.
"""
# option 1
diff: Iterator = difflib.unified_diff(
    text_one.splitlines(), text_two.splitlines(), lineterm='')
print("\n".join(diff))

print("-------------------------------------------------------------------")

# option 2
different_total = difflib.Differ()
diff_two = different_total.compare(text_one.splitlines(), text_two.splitlines())
print("\n".join(diff_two))

