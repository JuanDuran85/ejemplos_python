"""[summary]

Password generator with 4 lowercase letters, 4 uppercase letters, 2 numbers and 2 special characters.

The password is generated with 12 random characters.

"""

import string
from random import sample


def sample_charters(charters, n):
    return sample(charters, n)


result_sample = sample_charters(string.ascii_lowercase, 4) + sample_charters(
    string.ascii_uppercase, 4) + sample_charters(string.digits, 2) + sample_charters(string.punctuation, 2)

password_new = "".join(sample_charters(result_sample, 12))
print(f"{password_new = }")
