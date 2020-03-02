"""Monte carlo class storing functions for the method"""

from random import uniform
from math import sqrt

def point_generator():
    """Point generator in the range within the square"""

    x_value = uniform(0, sqrt(2))
    y_value = uniform(0, sqrt(2))
    return point_verifier(x_value, y_value)


def point_verifier(x_value: float, y_value: float):
    """Checks if generated point is within the area of the circle"""

    distance = sqrt((x_value**2)+(y_value**2))
    if distance < sqrt(2):
        return True
    return False

def monte_carlo(n_points: int):
    """recieves number of generated points and returns pi approximation"""
    total = 0
    inside = 0

    for _ in range(n_points):
        total += 1
        if point_generator():
            inside += 1
    final = 4*(inside/total)
    return final
