#!/usr/bin/python3
"""Python implementation of the middle product method seen in class"""

def randomizer(seed_value_a: str, seed_value_b: str):
    """method that contains the formula to obtain a randomized value via the
    middle product method"""
    print(seed_value_a)

    seed_values_multiplied = str(int(seed_value_a)*int(seed_value_b))

    elems_to_crop = int((len(seed_values_multiplied)-len(seed_value_b))//2)
    result = 0

    if elems_to_crop != 0:
        if len(seed_values_multiplied)%2 != 0:
            result = int(seed_values_multiplied[elems_to_crop:-elems_to_crop])
        else:
            result = int(seed_values_multiplied[elems_to_crop:-elems_to_crop-1])
            if len(str(result)) < len(seed_value_a):
                result = int(seed_values_multiplied[elems_to_crop:-elems_to_crop])

    return [seed_value_b, str(result)]


def main():
    """main method for the class"""
    seed_values = []
    seed_values.append(input())
    seed_values.append(input())

    for _ in range(19):
        seed_values = randomizer(seed_values[0], seed_values[1])

if __name__ == "__main__":
    main()
