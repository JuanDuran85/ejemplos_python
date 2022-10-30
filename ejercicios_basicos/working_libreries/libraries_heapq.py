'''
Heapq library
This module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.
'''

import heapq

grades: list[int] = [403,45,1,33,4,6,7,56,-8]

# nlargest Return a list with the n largest elements from the dataset defined by iterable
print(heapq.nlargest(4,grades))

# nsmallest Return a list with the n smallest elements from the dataset defined by iterable.
print(heapq.nsmallest(4,grades))