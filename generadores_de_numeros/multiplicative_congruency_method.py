#!/usr/bin/python3
"""Python implementation of the multiplicative congruency method seen in class"""

def generator(x_value: int, a_multiplier: int, m_modulus: int):
    """method that contains the formula to obtain a randomized value via the
    multiplicative congruency method"""
    print(x_value)
    result = a_multiplier*x_value%m_modulus

    return result

def main():
    """main method for the class"""

    x_value = 5         # x initial value for method
    a_multiplier = 5    # a multiplier for the method
    m_modulus = 32      # m modulus for the method

    for _ in range(11):
        x_value = generator(x_value, a_multiplier, m_modulus)

if __name__ == "__main__":
    main()
