"""[summary]

Tips and tricks for using string, conditions, loop, others.

All the examples are in the same file, but they are separated with a mark

All examples are from the internet with somes variations, so they are not 100% correct. Thanks to the authors.

"""

"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""
''' Using string methods'''

print("\n Using count \n")
letters_any = "aaabbbcccdddeeffffff"
print(f"{letters_any = }")

# if you need to count any letter in a string you can use count method
print(f"{letters_any.count('a') = }")
print(f"{letters_any.count('f') = }")
print(f"{letters_any.count('d') = }")


"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""
''' Diferent ways to test multiple flags at once in Python'''

print("\n Diferent ways to test multiple flags at once\n")

x, y, z = 0, 0, 0

if x==1 or y==1 or z==1:
    print("True")
else:
    print("False")
    
if 1 in (x,y,z):
    print("True")
else: 
    print("False")

# These only test for truthiness, not for equality.
if x or y or z:
    print("True")
else:
    print("False")
    
if any((x,y,z)):
    print("True")
else:
    print("False")

