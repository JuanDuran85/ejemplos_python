"""_summary_

    Working with re library

    Regular expression operations library: This module provides regular
    expression matching operations similar to those found in Perl.

"""

import re

# ----------------------------------------------------------------------------
# Find all python errors using re library
# ----------------------------------------------------------------------------

for i in dir(__builtins__):
    if re.match('^[A-Z]', i):
        print(i)
# ----------------------------------------------------------------------------}

# ----------------------------------------------------------------------------
# Creating a New List By applying Some operations On the Other List
# ----------------------------------------------------------------------------

# Suppose you have a 2D list containing general information like names, emails,
# and mobile numbers for different users. Your task is to extract all the emails
# provided by Gmail inside a list.'''

users = [
    ['Elio', 'P2MlS@example.com', '1234567890', 'VE'],
    ['John', 'GtZMw@example.com', '548585354'],
    ['Jane', 'jane@me.com', '5482006658', 'SF'],
    ['Doe', 't9EYh@example.com', '5482006658']
]
# you can use fullmatch to check if the whole string is a valid email
emails = [item for user in users for item in user if re.findall(r'(\w+@example\.com)', str(item))]

print(emails, "", end="")


# ----------------------------------------------------------------------------
