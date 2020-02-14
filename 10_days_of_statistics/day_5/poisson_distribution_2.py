"""Class used for solving the poisson_distribution_2 problem"""

from distributions import special_poisson_distribution

def main():
    """Main method for the poisson_distribution_2 problem"""

    avg_num_success = input()
    avg_num_success = avg_num_success.split(" ")
    avg_num_success = [float(i) for i in avg_num_success]

    cost_of_operating = [160, 128]

    for i in range(2):
        solution = cost_of_operating[i]+40*special_poisson_distribution(avg_num_success[i])

        print(round(solution, 3))

if __name__ == "__main__":
    main()
