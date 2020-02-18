#!/usr/bin/python3
"""Python implementation of the multiplicative congruency method seen in class"""

def randomizer(x_value: int, a_multiplier: int, m_modulus: int):
    """method that contains the formula to obtain a randomized value via the
    multiplicative congruency method"""
    print(x_value)
    result = a_multiplier*x_value%m_modulus

    return result

def main():
    """main method for the class"""
    x_initial = int(input())
    a_multiplier = 5
    m_modulus = 32

    result = x_initial

    print()

    for _ in range(11):
        result = randomizer(result, a_multiplier, m_modulus)

if __name__ == "__main__":
    main()
