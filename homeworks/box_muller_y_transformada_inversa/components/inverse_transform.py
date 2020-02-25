"""class used for obtaining the result of the inverse transformation"""

from math import log
from random import randint

from .normalizer import normalizer

def inverse_transform(i: int, x_min: int, x_max: int):
    """method used to generate random values for the inverse transform function"""

    result_array = []

    for _ in range(i):
        x_value = normalizer(randint(x_min, x_max), x_min, x_max)
        result_array.append(inverse_transforme_method(x_value, 0.5))

    return result_array

def inverse_transforme_method(u_value: float, lambda_value: float):
    """method for returning a value with an inverse transformation"""

    try:
        return -(log(1-u_value)/lambda_value)
    except ValueError:
        return 0
