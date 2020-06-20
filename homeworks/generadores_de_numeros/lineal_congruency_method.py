#!/usr/bin/python3
"""Python implementation of the lineal congruency method seen in class"""

def generator(x_value: int, a_multiplier: int, c_addition: int, m_modulus: int):
    """method that contains the formula to obtain a randomized value via the
    lineal congruency method"""
    print(x_value)
    result = (a_multiplier*x_value+c_addition)%m_modulus

    return result

def main():
    """main method for the class"""

    x_value = 7         # x initial value for the method
    a_multiplier = 7    # a multiplier for the method
    c_addition = 7      # c additive for the method
    m_modulus = 10      # m modulus for the method

    for _ in range(16):
        x_value = generator(x_value, a_multiplier, c_addition, m_modulus)

if __name__ == "__main__":
    main()
