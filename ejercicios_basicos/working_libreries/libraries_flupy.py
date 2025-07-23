# !/usr/bin/python3
# flake8: noqa: E501
# pylint: disable=line-too-long
# pylint: disable=C0103

"""_summary_

    Working with flupy library

    flupy chains them fluently, with lazy evaluation.
    It is a simple way to chain functions together.
    flupy is a lightweight library and CLI for implementing python data pipelines with a fluent interface.
"""

from flupy import flu


result = (
    flu(range(50))
    .filter(lambda x: x % 2 == 0)
    .map(lambda x: x * x)
    .take(6)
    .collect()
)

print(result)
