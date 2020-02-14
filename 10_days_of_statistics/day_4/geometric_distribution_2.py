"""This class is used to solve the geometric_fistribution_2 problem"""

from distributions import geometric_distribution

def main():
    """Main function for the geometric_distribution_2 class"""

    probability = input()
    probability = probability.split(" ")
    probability = int(probability[0])/int(probability[1])

    inspection_no = int(input())

    solution = 0

    for i in range(1, inspection_no+1):
        solution += geometric_distribution(i, probability)

    print(round(solution, 3))

if __name__ == "__main__":
    main()
