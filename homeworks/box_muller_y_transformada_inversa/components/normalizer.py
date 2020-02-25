"""class for normalizing a random value"""

def normalizer(x_value: int, x_min: int, x_max: int):
    """function for returning normalized value from a randomly generated value"""

    normalized_value = float((x_value-x_min)/(x_max-x_min))
    return normalized_value
