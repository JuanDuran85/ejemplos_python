# trabajando con la libreria numpy

import numpy as np

some_list = [1,2,3,4,5,6,7,8,9,10]
print(type(some_list))

some_array = np.array(some_list)
print(type(some_array))

# el metodo cumsum suma y acumula los valores presentes en una lista
# the cumsum method sums and accumulates the values ​​present in a list
rest_sum = list(np.cumsum(range(0,10,2)))
print(f"{rest_sum = }")