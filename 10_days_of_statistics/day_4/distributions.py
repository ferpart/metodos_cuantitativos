"""Class used for creating formulas to solve specific types of distributions"""

from formulas import combinations

def binomial_distribution(x_successes: int, n_trials: int, p_probability: float):
    """Method used to calculate the binomial distribution"""

    distribution = (combinations(n_trials, x_successes)*(p_probability**x_successes)*
                    ((1-p_probability)**(n_trials-x_successes)))

    return distribution

def negative_binomial_distribution(x_successes: int, n_trials: int, p_probability: float):
    """Method used to calculate the negative binomial distribution"""

    distribution = (combinations(n_trials-1, x_successes-1)*(p_probability**x_successes)*
                    ((1-p_probability)**(n_trials-x_successes)))

    return distribution

def geometric_distribution(n_trials, p_probability):
    """Method used to calculate the geometric distribution"""

    distribution = ((1-p_probability)**(n_trials-1))*p_probability

    return distribution
