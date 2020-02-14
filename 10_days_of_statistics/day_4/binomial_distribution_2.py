"""Solution for binomial_distribution_2 challenge"""

from distributions import binomial_distribution

def reject_calculator(range_min: int, range_max: int, total_pistons: int, prob_success: float):
    """method to return rejected piston percent"""

    total = 0
    for i in range(range_min, range_max):
        total += binomial_distribution(i, total_pistons, prob_success)
    return total

def main():
    """main function for the binomial_distribution_2 solution"""

    user_input = input()
    if len(user_input) != 0:

        user_input_list = user_input.split(" ")

        if len(user_input_list) > 1:
            user_input_list = [float(i) for i in user_input_list]

            total_pistons = user_input_list[1]
            prob_success = user_input_list[0]/100

            total_1 = reject_calculator(0, 3, total_pistons, prob_success)
            total_2 = reject_calculator(2, 11, total_pistons, prob_success)

            print(round(total_1, 3))
            print(round(total_2, 3))
            return
    return

if __name__ == "__main__":
    main()
