# !/usr/bin/python3
# flake8: noqa: E501
# pylint: disable=line-too-long
# pylint: disable=C0103

"""_summary_
"""

# working with the numpy library

import numpy as np

LINES = "---------------------------------------------------------------------\r"

some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(some_list))

some_array = np.array(some_list)
print(type(some_array))

# the cumsum method sums and accumulates the values present in a list
rest_sum = list(np.cumsum(range(0, 10, 2)))
print(f"{rest_sum=}")

# -----------------------------------------------------------------------------
print(LINES)
# Creating an array with zeros
print(f"{np.zeros(4)=}")
# creating an array with ones
print(f"{np.ones(4)=}")
# creating an array of elements
print(f"{np.arange(0, 10, 2)=}")
print(f"{np.arange(2, 20, 3)=}")
# creating an array from another
numbers_list_one: list = [3, 56, 5, 2]
array_one: np.ndarray = np.array(numbers_list_one)
print(f"{array_one=}")
# creating an array from two lists
numbers_list_one: list = [3, 56, 5, 2]
numbers_list_two: list = [8, 6, 3, 1]
double_list: tuple = (numbers_list_one, numbers_list_two)
print(f"{double_list=}")
array_double: np.ndarray = np.array(double_list)
print(f"{array_double=}")
# to show the shape of an array in numpy
print(f"{array_double.shape=}")
# to see the data type of the array
print(f"{array_double.dtype=}")

# -----------------------------------------------------------------------------
print(LINES)
# operations with arrays in numpy
array_one: np.ndarray = np.array([1, 2, 3, 4, 5])
array_five: np.ndarray = np.array([8, 1, 3, 5, 2])
# sum
print(f"{array_one + array_five=}")
# subtraction
print(f"{array_one - array_five=}")  # type: ignore
# multiplication
print(f"{array_one * array_five=}")
# division
print(f"{array_one / array_five=}")
# exponentiation
print(f"{array_one ** 2=}")

# -----------------------------------------------------------------------------
print(LINES)
# indexing with arrays in numpy
array: np.ndarray = np.arange(0, 11)
print(f"{array=}")
# initial position to a final position
print(f"{array[2:5]=}")
# show the original and complete array with :
print(f"{array[:]=}")
# creating a copy of the array without mutation problems
array_copy: np.ndarray = array.copy()
print(f"{array_copy=}")
# modifying values of an array by reference
array_copy[:3] = 9
print(f"{array_copy=}")

# -----------------------------------------------------------------------------
print(LINES)
# matrices and access to their elements in numpy
array_matrix: np.ndarray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"{array_matrix=}")
print(f"{array_matrix[0, 2]=}")
# creating a matrix with 3 rows and 5 columns using the reshape method
matrix_one = np.arange(15).reshape(3, 5)
print(f"{matrix_one=}")
# transposed matrices
transposed_matrix = matrix_one.T
print(f"{transposed_matrix=}")

# -----------------------------------------------------------------------------
print(LINES)
# input and output of arrays in numpy
array_one: np.ndarray = np.arange(6)
print(f"{array_one=}")
# saving an array in numpy as a binary file
np.save("array_one_saved", array_one)
# loading a saved array in numpy
saved_array: np.ndarray = np.load("array_one_saved.npy")
print(f"{saved_array=}")
# saving two arrays at the same time as binary
array_one: np.ndarray = np.arange(6)
print(f"{array_one=}")
array_four: np.ndarray = np.arange(5, 11)
print(f"{array_four=}")
np.savez("array_four_saved", x=array_one, y=array_four)
# recovering saved arrays
saved_two: np.ndarray = np.load("array_four_saved.npz")
print(f"{saved_two['x']=}")
print(f"{saved_two['y']=}")
# saving arrays as text files
np.savetxt("array_saved_text.txt", array_one, delimiter=",")
# recovering the saved text file
array_text = np.loadtxt("array_saved_text.txt", delimiter=",")
print(f"{array_text=}")

# -----------------------------------------------------------------------------
print(LINES)
# functions in arrays
# returning the square root of each element in an array
new_array: np.ndarray = np.arange(5)
print(f"{new_array=}")
print(f"{new_array ** 0.5=}")
print(f"{np.sqrt(new_array)=}")

# -----------------------------------------------------------------------------
print(LINES)
# creating an array randomly
random_array: np.ndarray = np.random.rand((5))
print(f"{random_array=}")

# -----------------------------------------------------------------------------
print(LINES)
# two arrays can be added using numpy's add function
array_one: np.ndarray = np.array([1, 2, 3, 4, 5])
array_three: np.ndarray = np.array([4, 6, 1, 2, 9])
print(f"{array_one + array_three=}")
sum_arrays: np.ndarray = np.add(array_one, array_three)
print(f"{sum_arrays=}")
# to show only the maximum values between two arrays column by column
max_values: np.ndarray = np.maximum(array_one, array_three)
print(f"{max_values=}")

# -----------------------------------------------------------------------------
print(LINES)
# using zeros, mean and std to normalize an array
# function that normalizes the data by subtracting the mean and dividing by the std.
# And by default, it just returns an array with a single zero element
# You should use is None, which checks for identity rather than value equality.


def normalize_fn(data: np.ndarray | None = None):
    """
    Normalizes the input data array by subtracting the mean and dividing by the standard deviation.

    Parameters:
    data (np.ndarray | None): The input data array to be normalized. If None, returns an array with a single zero element.

    Returns:
    np.ndarray: The normalized data array, or an array with a single zero element if the input is None.
    """

    if data is None:
        return np.zeros(1)
    return (data - np.mean(data) / np.std(data))


array_one: np.ndarray = np.array([1, 2, 3, 4, 5])
array_two: np.ndarray | None = None
print(f"{normalize_fn(array_one)=}")
print(f"{normalize_fn(array_two)=}")

print(LINES)
