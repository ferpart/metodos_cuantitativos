#!/usr/bin/python
"""Method for solving the spearman's rank correlation coefficient problem for 
day 7"""

from correlation_coefficient import spearmans_rank_correlation

def main():
    """main method for the spearmans rank correlation coeficcient"""
    n_count = int(input())

    x_values = list(map(float, input().split()))
    y_values = list(map(float, input().split()))

    solution = spearmans_rank_correlation(x_values, y_values, n_count)

    print(round(solution, 3))

if __name__ == "__main__":
    main()
