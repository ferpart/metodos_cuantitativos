from itertools import permutations
from fractions import Fraction
from math import pow

# n = int(input("how many dice? ") or "0")
# x = int(input("max sum of " + str(n) + " dice ") or "0")

def probability(n, x):
    if (n!=0):
        a=0
        s=int(pow(6, n))

        dice = [1,2,3,4,5,6]
        dice_combinations = list(permutations(dice, n))

        for i in range(len(dice_combinations)):
            if (sum(dice_combinations[i])==x):
                a+=1

        return (a/s)
    return (0)

def probability_fraction(n, x):
    if (n!=0):
        a=0
        s=int(pow(6, n))

        dice = [1,2,3,4,5,6]
        dice_combinations = list(permutations(dice, n))

        for i in range(len(dice_combinations)):
            if (sum(dice_combinations[i])==x):
                a+=1

        return (Fraction(a,s))
    return (0)