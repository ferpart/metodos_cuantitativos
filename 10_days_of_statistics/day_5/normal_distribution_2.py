#!/usr/bin/python3
"""Class used for solving the normal_distribution_2 problem"""

from distributions import cumulative_normal_distribution

def main():
    """Main method for the normal_distribution_2 class"""
    variables = input()
    variables = variables.split(" ")
    variables = [float(i) for i in variables]

    mean = variables[0]
    std_deviation = variables[1]

    test_1 = float(input())

    test_2_3 = float(input())

    cumulative_1 = 100 - cumulative_normal_distribution(mean, std_deviation, test_1) * 100
    cumulative_2 = 100 - cumulative_normal_distribution(mean, std_deviation, test_2_3) * 100
    cumulative_3 = cumulative_normal_distribution(mean, std_deviation, test_2_3) * 100
    print(round(cumulative_1, 2))
    print(round(cumulative_2, 2))
    print(round(cumulative_3, 2))

if __name__ == "__main__":
    main()
