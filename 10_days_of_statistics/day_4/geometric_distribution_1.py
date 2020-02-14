"""This class is used to solve the geometric_fistribution_1 problem"""

from distributions import geometric_distribution

def main():
    """Main function for the geometric_distribution_1 class"""

    probability = input()
    probability = probability.split(" ")
    probability = int(probability[0])/int(probability[1])

    inspection_no = int(input())

    solution = geometric_distribution(inspection_no, probability)

    print(round(solution, 3))

if __name__ == "__main__":
    main()
