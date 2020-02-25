"""class used for obtaining the result of the box muller transformation"""

from math import log, sqrt, cos, sin, pi
from random import randint

from .normalizer import normalizer

def box_muller(i: int, x_min: int, x_max: int):
    """method used to generate random values for the box muller function"""

    result_array = []
    x_values = [0, 0]
    for _ in range(i):
        for n_range in range(2):
            x_values[n_range] = normalizer(randint(x_min, x_max), x_min, x_max)
        x1_value, x2_value = box_muller_method(x_values[0], x_values[1])

        result_array.append(x1_value)
        result_array.append(x2_value)

    return result_array

def box_muller_method(r1_value: float, r2_value: float):
    """method for returning 2 values transformed with the box_muller method"""

    try:
        x1_result = sqrt(-2*log(r1_value))*cos(2*pi*r2_value)
        x2_result = sqrt(-2*log(r1_value))*sin(2*pi*r2_value)
        return x1_result, x2_result
    except ValueError:
        return 0, 0
