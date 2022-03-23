"""[summary]

    Password generator
    This code generates a password of length 10. If you want to change the length of the password, update the parameter of the range() function. Also, each time when you run the code, you'll get a different random output.

"""

import random

charters: str = "abcdefghijklmnopqrstuvwxyz0123456789%^*(-_=+)"
password_generated: str = ''.join([charters[random.randint(0,len(charters)-1)] for _ in range(10)])
print(f"{password_generated = }")