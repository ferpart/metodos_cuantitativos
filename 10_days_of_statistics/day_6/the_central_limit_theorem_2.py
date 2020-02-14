#!/usr/bin/python3
"""Solution code for the Day 6: The Central Limit Theorem II problem"""

from distributions import cumulative_normal_distribution

def mean_prime(n_value: int, mean: float):
    """method used to obtain the prime mean"""
    result = n_value*mean

    return result

def std_deviation_prime(n_value: int, std_deviation: float):
    """method used to obtain the prime standard deviation"""
    result = (n_value**(1/2))*std_deviation

    return result

def main():
    """Main method for the_central_limit_theorem_2 class"""

    x_value = float(input())
    n_value = int(input())
    mean = mean_prime(n_value, float(input()))
    std_deviation = std_deviation_prime(n_value, float(input()))

    print(round(cumulative_normal_distribution(mean, std_deviation, x_value), 4))

if __name__ == "__main__":
    main()
