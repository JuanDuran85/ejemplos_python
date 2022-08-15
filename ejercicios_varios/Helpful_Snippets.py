"""
https://morioh.com/p/271bc88c0100?f=5c21fb01c16e2556b555ab32
"""

#1. All unique characters in a string/ The following method checks whether the given list
# has duplicate elements. It uses the property of set() which removes duplicate elements from 
# the list.
def all_unique(lst):
    return len(lst) == len(set(lst))

x = [1,1,2,2,3,2,3,4,5,6]
y = [1,2,3,4,5]
all_unique(x) # False
all_unique(y) # True

#2. Anagrams /This method can be used to check if two strings are anagrams. An anagram is
#  a word or phrase formed by rearranging the letters of a different word or phrase, typically
#  using all the original letters exactly once.

from collections import Counter

def anagram(first, second):
    return Counter(first) == Counter(second)

anagram("abcd3", "3acdb") # True

#3. Memory /This snippet can be used to check the memory usage of an object.
import sys 

variable = 30 
#print(sys.getsizeof(variable)) # 28

#4. Byte size /This method returns the length of a string in bytes.

def byte_size(string):
    return(len(string.encode('utf-8')))
    
byte_size('😀') # 4
byte_size('Hello World') # 11 

#5. Print a string N times /This snippet can be used to print a string n times
#  without having to use loops to do it.
n = 2; 
s ="Programming"; 
#print(s * n); # ProgrammingProgramming

#6. Capitalize first letters /This snippet simply uses the method title() to capitalize
#  first letters of every word in a string.
s = "programming is awesome"
#print(s.title()) # Programming Is Awesome

#7. Chunk / This method chunks a list into smaller lists of a specified size.
def chunk(list, size):
    return [list[i:i+size] for i in range(0,len(list), size)]

#8. Compact /This method removes falsy values (False, None, 0 and “”) from a list
#  by using filter().

def compact(lst):
    return list(filter(None, lst))

compact([0, 1, False, 2, '', 3, 'a', 's', 34]) # [ 1, 2, 3, 'a', 's', 34 ]

#9. Count by /This snippet can be used to transpose a 2D array.

array = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*array)
print(transposed) # [('a', 'c', 'e'), ('b', 'd', 'f')]

#10. Chained comparison /You can do multiple comparisons with all kinds of
#  operators in a single line.
a = 3
print( 2 < a < 8) # True
print(1 == a < 2) # False

#11. Comma-separated /This snippet can be used to turn a list of strings into
#  a single string with each element from the list separated by commas.

hobbies = ["basketball", "football", "swimming"]

print("My hobbies are:") # My hobbies are:
print(", ".join(hobbies)) # basketball, football, swimming

#12. Get vowels /This method gets vowels (‘a’, ‘e’, ‘i’, ‘o’, ‘u’) found in a string.

def get_vowels(string):
    return [each for each in string if each in 'aeiou'] 


get_vowels('foobar') # ['o', 'o', 'a']
get_vowels('gym') # []

#13. Decapitalize /This method can be used to turn the first letter of the given 
# string into lowercase.

def decapitalize(str):
    return str[:1].lower() + str[1:]

decapitalize('FooBar') # 'fooBar'
decapitalize('FooBar') # 'fooBar'

#14. Flatten /The following methods flatten a potentially deep list using recursion.

def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret

def deep_flatten(xs):
    flat_list = []
    [flat_list.extend(deep_flatten(x)) for x in xs] if isinstance(xs, list) else flat_list.append(xs)
    return flat_list


deep_flatten([1, [2], [[3], 4], 5]) # [1,2,3,4,5]

#15. Difference /This method finds the difference between two iterables by keeping
#  only the values that are in the first one.

def difference(a, b):
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    return list(comparison)


difference([1,2,3], [1,2,4]) # [3]

#16. Difference by / The following method returns the difference between two 
# lists after applying a given function to each element of both lists.

def difference_by(a, b, fn):
    b = set(map(fn, b))
    return [item for item in a if fn(item) not in b]


from math import floor
difference_by([2.1, 1.2], [2.3, 3.4], floor) # [1.2]
difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x']) # [ { x: 2 } ]

#17. Chained function call /You can call multiple functions inside a single line.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

a, b = 4, 5
print((subtract if a > b else add)(a, b)) # 9   

#18. Has duplicates /The following method checks whether a list has duplicate values by using the fact that set() contains only unique elements.

def has_duplicates(lst):
    return len(lst) != len(set(lst))
    
x = [1,2,3,4,5,5]
y = [1,2,3,4,5]
has_duplicates(x) # True
has_duplicates(y) # False

#19. Merge two dictionaries /The following method can be used to merge two dictionaries.

def merge_two_dicts(a, b):
    c = a.copy()   # make a copy of a 
    c.update(b)    # modify keys and values of a with the ones from b
    return c

a = { 'x': 1, 'y': 2}
b = { 'y': 3, 'z': 4}
print(merge_two_dicts(a, b)) # {'y': 3, 'x': 1, 'z': 4}
#In Python 3.5 and above, you can also do it like the following:

def merge_dictionaries(a, b):
   return {**a, **b}

a = { 'x': 1, 'y': 2}
b = { 'y': 3, 'z': 4}
#print(merge_dictionaries(a, b)) # {'y': 3, 'x': 1, 'z': 4}

#20. Convert two lists into a dictionary /The following method can be used
# to convert two lists into a dictionary.

def to_dictionary(keys, values):
    return dict(zip(keys, values))
    

keys = ["a", "b", "c"]    
values = [2, 3, 4]
print(to_dictionary(keys, values)) # {'a': 2, 'c': 4, 'b': 3}

#21. Use enumerate /This snippet shows that you can use enumerate to get both
#  the values and the indexes of lists.

list = ["a", "b", "c", "d"]
for index, element in enumerate(list): 
    print("Value", element, "Index ", index, ) # ('Value', 'a', 'Index ', 0), etc

#22. Time spent /This snippet can be used to calculate the time it takes to 
# execute a particular code.

import time

start_time = time.time()

a = 1
b = 2
c = a + b
print(c) #3

end_time = time.time()
total_time = end_time - start_time
print("Time: ", total_time)

# ('Time: ', 1.1205673217773438e-05)

#23. Try else You can have an else clause as part of a try/except block, which
#  is executed if no exception is thrown.

try:
    2*3
except TypeError:
    print("An exception was raised")
else:
    print("Thank God, no exceptions were raised.")

#Thank God, no exceptions were raised.

#24. Most frequent /This method returns the most frequent element that appears
#  in a list.

def most_frequent(list):
    return max(set(list), key = list.count)

numbers = [1,2,1,2,3,2,1,4,2]
most_frequent(numbers)  

#25. Palindrome /This method checks whether a given string is a palindrome.

def palindrome(a):
    return a == a[::-1]

palindrome('mom') # True

#26. Calculator without if-else /The following snippet shows how you can write 
# a simple calculator without the need to use if-else conditions.

import operator
action = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "**": pow
}
print(action['-'](50, 25)) # 25

#27. Shuffle /This snippet can be used to randomize the order of the elements
# in a list. Note that shuffle works in place, and returns None.

from random import shuffle

foo = [1, 2, 3, 4]
shuffle(foo) 
print(foo) # [1, 4, 3, 2] ,  [1, 2, 4, 3], etc
#28. Spread /This method flattens a list similarly like [].concat(…arr) in JavaScript.

def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret

spread([1,2,3,[4,5,6],[7],8,9]) # [1,2,3,4,5,6,7,8,9]

#29. Swap values /A really quick way for swapping two variables without having to 
# use an additional one.

a, b = -1, 14
a, b = b, a

print(a) # 14
print(b) # -1

#30. Get default value for missing keys /This snippet shows how you can get a 
# default value in case a key you are looking for is not included in the dictionary.

d = {'a': 1, 'b': 2}

print(d.get('c', 3)) # 3