"""Class for storing formulas used for day_7 these formulas are that of the
Covariance, as well as the Pearson Correlation Coefficient"""

def mean(x_values: list, n_count: int):
    """method used for calculating the mean of a list of x values"""

    solution = sum(x_values)/n_count
    return solution

def standard_deviation(x_values: list, n_count: int):
    """method for calculating the standard deviation of a list of x values"""

    if n_count != 0:
        avg = mean(x_values, n_count)
        summatory = 0
        for i in range(n_count):
            summatory += (x_values[i]-avg)**2

        solution = (summatory/n_count)**(1/2)

        return solution
    return 0

def covariance(x_values: list, y_values: list, n_count: int):
    """method used to calculate the covariance"""

    x_average = mean(x_values, n_count)
    y_average = mean(y_values, n_count)

    summatory = 0

    for i in range(n_count):
        x_subsection = x_values[i]-x_average
        y_subsection = y_values[i]-y_average
        summatory += x_subsection*y_subsection

    solution = summatory/n_count

    return solution

def pearson_correlation_coefficient(x_values: list, y_values: list, n_count: int):
    """method for obtaining the pearson correllation coefficient"""
    std_deviation_x = standard_deviation(x_values, n_count)
    std_deviation_y = standard_deviation(y_values, n_count)
    cov = covariance(x_values, y_values, n_count)

    solution = cov/(std_deviation_x*std_deviation_y)

    return solution

def rank(x_values):
    """rank getter"""
    x_rank = dict((x_value, i+1) for i, x_value in enumerate(sorted(set(x_values))))
    return [x_rank[x_value] for x_value in x_values]

def spearmans_rank_correlation(x_values: list, y_values: list, n_count: int):
    """formula used to obtain the spearmans rank collection"""
    x_rank = rank(x_values)
    y_rank = rank(y_values)

    solution = pearson_correlation_coefficient(x_rank, y_rank, n_count)

    return solution
