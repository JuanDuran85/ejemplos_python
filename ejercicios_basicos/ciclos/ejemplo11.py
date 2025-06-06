# !/usr/bin/python3
# flake8: noqa: E501
# pylint: disable=line-too-long
# pylint: disable=C0103
# working with while loop

"""_summary_
"""

count_num = 0

while count_num <= 10:
    print(count_num)
    count_num += 1

i = 5

while i >= 1:
    print(i)
    i -= 1

# working with for loop

word = "Santiago"

for letter in word:
    print(letter)
    if letter == "i":
        print(f"Letter found: {letter}")
        break
else:
    print("End of cycle")

# even numbers with for
for i in range(6):
    if i % 2 == 0:
        print(f"The value is: {i}")

# even numbers with for and continue
for i in range(10):
    if i % 2 != 0:
        continue
    print(f"The value is: {i}")


# implementing enumerate in a for loop
print("\r\nimplementing enumerate in a for loop\r\n")
list_numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"{list_numbers=}")
for key, value in enumerate(list_numbers):
    print(f"Position: {key} - Value: {value}")


# implementing enumerate to get negative numbers from a list
numbers: list = [3, 67, -3, 7, -87, 0, -9]
for index, item in enumerate(numbers):
    if item < 0:
        print(f"The value is: {item} for position {index}")


# using the walrus operator in a for loop
words: list = ["Word number one", "Another word", "New type of words", "More words"]
for string in words:
    if len(result := string.split(" ")) == 2:
        print(f"{result=}")
