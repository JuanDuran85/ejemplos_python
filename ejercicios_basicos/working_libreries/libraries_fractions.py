"""_summary_

    Working with fractions library in Python

"""

from fractions import Fraction

# create from two arguments
print(Fraction(1, 2))
print(Fraction(16, 10))
print(Fraction(20, -12))
print(Fraction(-40, 16))

# from a string
print(Fraction('1/2'))
print(Fraction('10/35'))
print(Fraction('12/16'))

# from a float
print(Fraction(0.5))
print(Fraction(1.25))
print(Fraction(4.5))

# numerator and denominator
fraction_one: Fraction = Fraction(0.125)
numerator_number: int = fraction_one.numerator
print(numerator_number)
denominator_number: int = fraction_one.denominator
print(denominator_number)
integer_ratio_number: tuple = fraction_one.as_integer_ratio()
print(integer_ratio_number)