"""Class used for solving the permutations and combinations formulas"""

from fractions import Fraction
from math import factorial

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
