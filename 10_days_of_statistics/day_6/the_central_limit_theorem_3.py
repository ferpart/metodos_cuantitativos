#!/usr/bin/python3
"""Solution code for the Day 6: The Central Limit Theorem III problem"""

def margin_of_error(z_value: float, std_deviation: float, n_value: int):
    """method used to find the error margin"""
    result = z_value*std_deviation/(n_value**(1/2))

    return result

def main():
    """Main method for the_central_limit_theorem_3 class"""

    n_value = int(input())
    mean = float(input())
    std_deviation = float(input())
    _ = input()
    z_value = float(input())

    error_margin = margin_of_error(z_value, std_deviation, n_value)

    print("%0.2f\n%0.2f" %(round(mean-error_margin, 2), round(mean+error_margin, 2)))

if __name__ == "__main__":
    main()
