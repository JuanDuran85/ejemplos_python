# !/usr/bin/python3
# flake8: noqa: E501
# pylint: disable=line-too-long
# pylint: disable=C0103

"""_summary_

    Working with benedict library

"""

from benedict import benedict

d = benedict(keyattr_dynamic=True)  # default False
d.profile.firstname = "John"
d.profile.lastname = "Doe"
print(d)


data_dict = benedict({'abc': 1}, format='json')
print(data_dict['abc'])
print(data_dict.get('abc'))
data_dict.flatten()
print(data_dict)
