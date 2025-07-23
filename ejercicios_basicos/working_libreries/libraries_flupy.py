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

customers = [
    {"customer_id": 1, "name": "John Doe", "email": "jdoe@google.com", "signup_year": 2019, "active": True},
    {"customer_id": 2, "name": "Jane Smith", "email": "jsmith@hotmail.com", "signup_year": 2020, "active": False},
    {"customer_id": 3, "name": "Robert Zboncak", "email": "robert@yahoo.com", "signup_year": 2021, "active": True},
    {"customer_id": 4, "name": "Anna Johnson", "email": "anna@google.com", "signup_year": 2022, "active": True},
]

pipeline_output = (
    flu(customers)
    .filter(lambda x: x["active"])
    .map_item('email') # type: ignore
    .map(lambda x: x.partition('@')[2])
    .group_by()
    .map(lambda x: (x[0], x[1].count()))
    .collect()
)

print(pipeline_output)
