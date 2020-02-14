"""Solution for binomial_distribution_1 challenge"""

from distributions import binomial_distribution

def main():
    """main function for the binomial_distribution_1 solution"""

    user_input = input()
    if len(user_input) != 0:

        user_input_list = user_input.split(" ")

        if len(user_input_list) > 1:
            user_input_list = [float(i) for i in user_input_list]

            prob_success = user_input_list[0]/(user_input_list[0]+user_input_list[1])
            total = 0

            for i in range(3, 7):
                total += binomial_distribution(i, 6, prob_success)

            print(round(total, 3))
            return
    return

if __name__ == "__main__":
    main()
