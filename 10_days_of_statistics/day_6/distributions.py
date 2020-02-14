"""Class used for creating formulas to solve specific types of distributions"""

from math import e, factorial, sqrt, pi, erf

def poisson_distribution(act_num_success: int, avg_num_success: float):
    """Method used to calculate the poisson distribution"""

    distribution = ((avg_num_success**act_num_success)*(e**(-avg_num_success))/
                    factorial(act_num_success))

    return distribution

def special_poisson_distribution(avg_num_success: float):
    """Method used only in special cases of the poisson distribution where we
    have some poisson random variable X, we ler E[X] be the expectation of X,
    so we use this to find the E[X^2] (Expectation of X squared)"""

    distribution = avg_num_success + avg_num_success**2
    return distribution

def normal_distribution(mean: float, variance: float, x_value):
    """Method used to obtain the probability density of normal distribution"""

    if isinstance(x_value, float):
        e_superscript = -(((x_value-mean)**2)/2*variance)
        distribution = 1/(sqrt(variance)*sqrt(2*pi))
        distribution = distribution*(e**(e_superscript))
        return distribution

    if isinstance(x_value, list):
        distribution = 0
        for i in range(x_value[0], x_value[1]+1):
            e_superscript = -(((i-mean)**2)/2*variance)
            distribution_temp = 1/(sqrt(variance)*sqrt(2*pi))
            distribution_temp = distribution_temp*(e**(e_superscript))
            distribution += distribution_temp
        return distribution

    return 0

def cumulative_normal_distribution(mean: float, std_deviation: float, x_value: (list, float)):
    """Method used to obtain the probability density of cumulative normal distribution"""

    if isinstance(x_value, float):

        erf_equation = (x_value-mean)/(std_deviation*sqrt(2))
        distribution = 1/2*(1+erf(erf_equation))

        return distribution

    if isinstance(x_value, list):

        distribution = (cumulative_normal_distribution(mean, std_deviation, x_value[len(x_value)-1])
                        - cumulative_normal_distribution(mean, std_deviation, x_value[0]))

        return distribution

    return 0
