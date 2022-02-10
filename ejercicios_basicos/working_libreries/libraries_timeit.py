import timeit

''' Using for loop and timeit module'''

'''The timeit module lets you measure the execution time of small bits of Python code. '''

link = "-"
print(f"{link.join(str(n) for n in range(100))}")
print(timeit.timeit(link.join(str(n) for n in range(100))))
print(timeit.timeit(link.join([str(n) for n in range(100)])))
print(timeit.timeit(link.join(map(str,range(100)))))