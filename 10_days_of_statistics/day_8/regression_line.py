"""class used to hold formulas used to solve day 8 problems"""


def regression_line(x_values: list, y_values: list, n_count: int, x_element: int):
    """formula to calculate the regression line based on two given lists, and a
    element to solbe te formula with"""

    x_sum = sum(x_values)
    x_prom = x_sum/n_count

    y_sum = sum(y_values)
    y_prom = y_sum/n_count

    x_sum_squared = sum([i**2 for i in x_values])

    x_y_multiplied = sum([a*b for a, b in zip(x_values, y_values)])

    b_result_upper = (n_count*x_y_multiplied)-(x_sum*y_sum)
    b_result_lower = (n_count*x_sum_squared)-(x_sum**2)

    b_result = b_result_upper/b_result_lower

    a_result = y_prom-b_result*x_prom

    regression = a_result+b_result*x_element

    return regression
