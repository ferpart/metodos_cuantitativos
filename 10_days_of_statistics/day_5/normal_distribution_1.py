"""Class used for solving the normal_distribution_1 problem"""

from distributions import cumulative_normal_distribution

def main():
    """Main method for the normal_distribution_1 class"""
    variables = input()
    variables = variables.split(" ")
    variables = [float(i) for i in variables]

    mean = variables[0]
    std_deviation = variables[1]

    test_1 = float(input())

    test_2 = input()
    test_2 = test_2.split(" ")
    test_2 = [float(i) for i in test_2]
    
    cumulative_1 = cumulative_normal_distribution(mean, std_deviation, test_1)
    cumulative_2 = cumulative_normal_distribution(mean, std_deviation, test_2)
    print(round(cumulative_1, 3))
    print(round(cumulative_2, 3))

if __name__ == "__main__":
    main()
