#!/usr/bin/python3
"""Class used for solving the Pearson Correlation Coefficient I problem for
day 7"""


import math
from correlation_coefficient import pearson_correlation_coefficient

def main():
    """main method for the pearson_correlation_coefficient class"""

    n_count = int(input())
    
    x_values = input().split()
    y_values = input().split()

    x_values = [float(i) for i in x_values]
    y_values = [float(i) for i in y_values]

    solution = pearson_correlation_coefficient(x_values, y_values, n_count)

    print(round(solution, 3))

if __name__ == "__main__":
    main()
