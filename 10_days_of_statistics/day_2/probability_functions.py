"""This is a class created just for using probability functions on the 2nd day
   of the 10_days_of_statistics course"""

from itertools import product
from itertools import permutations
from fractions import Fraction

def dice_probability_fraction(n_elements: int, x_max_sum: int):
    """Method used to display in fraction format the probability of obtaining
       a maximum of x_max_sum cards"""
    if n_elements != 0:
        a_top_fraction = 0
        s_bot_fraction = int(pow(6, n_elements))
        dice = [1, 2, 3, 4, 5, 6]
        dice_combinations = list(product(dice, repeat=n_elements))

        for i in range(s_bot_fraction):
            if sum(dice_combinations[i]) <= x_max_sum:
                a_top_fraction += 1

        return Fraction(a_top_fraction, s_bot_fraction)
    return 0

def dice_probability(n_elements: int, x_max_sum: int):
    """Method used to display in decimal format the probability of obtaining
       a maximum of x_max_sum cards"""
    if n_elements != 0:
        a_top_fraction = 0
        s_bot_fraction = int(pow(6, n_elements))

        dice = [1, 2, 3, 4, 5, 6]
        dice_combinations = list(product(dice, repeat=n_elements))

        for i in range(s_bot_fraction):
            if sum(dice_combinations[i]) <= x_max_sum:
                a_top_fraction += 1

        return a_top_fraction/s_bot_fraction
    return 0

def dice_probability_unique_fraction(n_elements: int, x_sum: int):
    """Method used to display in fraction format the probability of obtaining
    exactly x_sum sum of cards cards"""
    if n_elements != 0:
        a_top_fraction = 0
        s_bot_fraction = int(pow(6, n_elements))

        dice = [1, 2, 3, 4, 5, 6]
        dice_combinations = list(permutations(dice, n_elements))
        num_dice_combinations = len(dice_combinations)

        for i in range(num_dice_combinations):
            if sum(dice_combinations[i]) == x_sum:
                a_top_fraction += 1

        return Fraction(a_top_fraction, s_bot_fraction)
    return 0

def dice_probability_unique(n_elements: int, x_sum: int):
    """Method used to display in decimal format the probability of obtaining
       exactly x_sum sum of cards cards"""
    if n_elements != 0:
        a_top_fraction = 0
        s_bot_fraction = int(pow(6, n_elements))

        dice = [1, 2, 3, 4, 5, 6]
        dice_combinations = list(permutations(dice, n_elements))
        num_dice_combinations = len(dice_combinations)

        for i in range(num_dice_combinations):
            if sum(dice_combinations[i]) == x_sum:
                a_top_fraction += 1

        return a_top_fraction/s_bot_fraction
    return 0

def urn_probability(color: str, list_balls: list):
    """Calculates the probability in decimal of getting a specific color of ball
    in an urn from a list of colored balls"""
    red_count = list_balls.count("r")
    blk_count = list_balls.count("b")
    if color == "r":
        return red_count/len(list_balls)
    if color == "b":
        return blk_count/len(list_balls)
    return 0

def urn_probability_fraction(color: str, list_balls: list):
    """Calculates the probability in fraction of getting a specific color of ball
    in an urn from a list of colored balls"""
    red_count = list_balls.count("r")
    blk_count = list_balls.count("b")
    if color == "r":
        return Fraction(red_count, len(list_balls))
    if color == "b":
        return Fraction(blk_count, len(list_balls))
    return 0

def urn_probability_of_retrieval(chain_to_find: list, x_list: list, y_list: list, z_list: list):
    """Calculates the probability of a specific chain to be found within 3 lists
    """
    if (len(chain_to_find) != 0 or len(x_list) != 0 or len(y_list) != 0 or
            len(z_list) != 0):

        first_pull = urn_probability_fraction(chain_to_find[0], x_list)
        second_pull = urn_probability_fraction(chain_to_find[1], y_list)
        third_pull = urn_probability_fraction(chain_to_find[2], z_list)

        final_probability = first_pull*second_pull*third_pull
        return final_probability
    return 0
