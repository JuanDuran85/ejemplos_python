"""_summary_

    working with libraries numerizer

    A Python module to convert natural language numerics into ints and floats.

    pip install numerizer

"""

from numerizer import numerize

print("------------------------------------------------------------------------")
print("using numerizer")
print("------------------------------------------------------------------------")


NUMBER_IN_LATTER_100 = "one hundred"
print(f"{NUMBER_IN_LATTER_100=}")
print(f"Result in number: {int(numerize(NUMBER_IN_LATTER_100))}")

NUMBER_IN_LATTER_42 = "forty two"
print(f"{NUMBER_IN_LATTER_42=}")
print(f"Result in number: {int(numerize(NUMBER_IN_LATTER_42))}")

NUMBER_IN_LATTER_55 = "fifty five"
print(f"{NUMBER_IN_LATTER_55=}")
print(f"Result in number: {int(numerize(NUMBER_IN_LATTER_55))}")
