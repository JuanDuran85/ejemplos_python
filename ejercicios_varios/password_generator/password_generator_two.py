from random import choice, randint
import string

ch = string.ascii_letters + string.digits + string.digits + string.punctuation
password_generator = "".join(choice(ch) for _ in range(randint(8,16)))
print(f"{password_generator = }")