#!/usr/bin/python3
"""Class used for solving the least regression line problem for day 8"""

from regression_line import regression_line

def main():
    """main method for the least_square_regression_line class"""

    n_count = 5
    x_element = 80

    x_values = []
    y_values = []

    for _ in range(n_count):
        input_value = input().split()
        x_values.append(float(input_value[0]))
        y_values.append(float(input_value[1]))

    result = regression_line(x_values, y_values, n_count, x_element)

    print(round(result, 3))

if __name__ == "__main__":
    main()
