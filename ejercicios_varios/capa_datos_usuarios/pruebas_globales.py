import bcrypt

password = b"super secret password"
# Hash a password for the first time, with a certain number of rounds
hashed = bcrypt.hashpw(password, bcrypt.gensalt(14))
# Check that a unhashed password matches one that has previously been

print(hashed)
#   hashed
if bcrypt.checkpw(b"nuevo password ingresado", hashed):
    print("It Matches!")
else:
    print("It Does not Match :(")
