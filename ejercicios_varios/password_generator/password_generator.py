import string
from random import sample

c_lower = string.ascii_lowercase
print(f"{c_lower = }")

c_upper = string.ascii_uppercase
print(f"{c_upper = }")

c_digits = string.digits
print(f"{c_digits = }")

c_special = string.punctuation
print(f"{c_special = }")

cl = sample(c_lower, 4)
print(f"{cl = }")

cu = sample(c_upper, 4)
print(f"{cu = }")

cd = sample(c_digits, 2)
print(f"{cd = }")

cs = sample(c_special, 2)
print(f"{cs = }")

c = cl + cu + cd + cs
print(f"{c = }")

password_new = "".join(sample(c,12))
print(f"{password_new = }")
