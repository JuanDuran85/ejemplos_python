# !/usr/bin/python3
# flake8: noqa: E501
# pylint: disable=line-too-long
# pylint: disable=C0103

"""_summary_

    Using Pypika Library

    pip install pypika
    
    It’s a fluent query builder that lets you construct SQL queries 
    without raw strings — while still being readable and flexible.
    
    With this library, you can get the following benefits:
    - Safe from SQL injection
    - Dynamically build WHEREs, JOINs, nested queries, etc
    - Compatible with every SQL backend
"""

from pypika import Query, Table

users = Table('users')
query_result = Query.from_(users).select(users.name, users.age).where(users.age > 70)
print(str(query_result))
