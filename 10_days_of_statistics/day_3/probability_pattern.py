"""Class used for solving the permutations and combinations formulas"""

from math import factorial
from fractions import Fraction

def permutations(n_element: int, r_element: int):
    """Method used to solve permutations formula in decimal format"""
    return factorial(n_element)/factorial(n_element-r_element)

def permutations_fraction(n_element, r_element):
    """Method used to solve permutations formula in fraction format"""
    return Fraction(factorial(n_element), factorial(n_element-r_element))

def combinations(n_element, r_element):
    """Method used to solve combinations formula in decimal format"""
    return permutations(n_element, r_element)/factorial(r_element)

def combinations_fraction(n_element, r_element):
    """Method used to solve combinations formula in fraction format"""
    return Fraction(permutations_fraction(n_element, r_element), factorial(r_element))

print(combinations_fraction(4, 1)*permutations_fraction(13, 2)/
      permutations_fraction(52, 2))
