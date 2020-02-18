#!/usr/bin/python3
"""Python implementation of the lineal congruency method seen in class"""

def randomizer(x_value: int, a_multiplier: int, c_addition: int, m_modulus: int):
    """method that contains the formula to obtain a randomized value via the
    lineal congruency method"""
    print(x_value)
    result = (a_multiplier*x_value+c_addition)%m_modulus

    return result

def main():
    """main method for the class"""
    x_initial = int(input())
    a_multiplier = 1
    c_addition = 7
    m_modulus = 13

    result = x_initial

    print()

    for _ in range(16):
        result = randomizer(result, a_multiplier, c_addition, m_modulus)

if __name__ == "__main__":
    main()
