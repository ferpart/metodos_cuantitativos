#!/usr/bin/python3
"""Code for solving the Multiple Linear Regression problem"""

from lib import sklearn

def main():
    """main function for the method"""

    initial_list = list(map(int, str.split(input(), " ")))
    m_value, n_value = initial_list[0], initial_list[1]

    data = [list(float(x) for x in input().split()) for i in range(n_value)]

    x_list = [[item[i] for i in range(m_value)] for item in data]
    y_list = [item[-1] for item in data]
    lm_model = sklearn.linear_model.LinearRegression()
    lm_model.fit(x_list, y_list)
    a_intercept = lm_model.intercept_
    b_coefficient = lm_model.coef_

    for _ in range(int(input())):
        data = list(map(float, input().split()))
        ans = [b_coefficient[j]*data[j] for j in range(m_value)]
        print(a_intercept+sum(ans))

if __name__ == "__main__":
    main()
