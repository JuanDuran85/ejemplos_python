"""_summary_

    Working with bcrypt library

"""

from typing import Literal
import bcrypt

# Hashing passwords - Hashing passwords or any other string is incredibly simple using the bcrypt.hashpw() function.

password: bytes = "SuperSercet34".encode("utf-8")
# bcrypt features an adjustable work factor which we can pass to bcrypt.gensalt() using the rounds argument and providing an integer (The default is 12).
hashed: bytes = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)

# Checking passwords - bcrypt also comes with a function to check plain text passwords against hashed passwords, returning True if the passwords match, else returning False.
# Check if password matches the hashed password
if bcrypt.checkpw(password, hashed):
    print("Password matches")
else:
    print("Password does not match")