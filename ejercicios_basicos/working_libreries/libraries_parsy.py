# !/usr/bin/python3
# flake8: noqa: E501
# pylint: disable=line-too-long
# pylint: disable=C0103

"""_summary_

    Using Parsy Library

    pip install parsy
    
    Parsy lets you compose parsers in a readable, testable way.
    
    With this library, you can get the following benefits:
    - No more cryptic regex maintenance
    - Composable and testable parsing logic
    - Can build full interpreters
"""

from parsy import string, regex

integer = regex(r'-?\d+').map(int)
comma = string(',')
number_list = integer.sep_by(comma)

print(number_list.parse("65,-76,22"))
