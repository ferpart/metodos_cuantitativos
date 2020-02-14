"""Class used for solving the poisson_distribution_1 problem"""

from distributions import poisson_distribution

def main():
    """Main method for the poisson_distribution_1 problem"""

    avg_num_success = float(input())
    act_num_success = int(input())

    solution = poisson_distribution(act_num_success, avg_num_success)

    print(solution)

if __name__ == "__main__":
    main()
