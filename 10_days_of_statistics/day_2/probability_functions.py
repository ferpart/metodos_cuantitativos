from itertools import product
from itertools import permutations
from fractions import Fraction
from math import pow

def dice_probability_fraction(n :int, x :int):
    if (n!=0):
        a=0
        s= int(pow(6, n))
        dice = [1,2,3,4,5,6]
        dice_combinations = list(product(dice, repeat=n))

        for i in range(s):
            if (sum(dice_combinations[i])<=x):
                a+=1

        return (Fraction(a,s))
    return (0)

def dice_probability(n :int,x :int):
    if (n!=0):
        a=0
        s= int(pow(6, n))

        dice = [1,2,3,4,5,6]
        dice_combinations = list(product(dice, repeat=n))

        for i in range(s):
            if (sum(dice_combinations[i])<=x):
                a+=1

        return (a/s)
    return (0)

def dice_probability_unique(n :int, x :int):
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

def dice_probability_unique_fraction(n :int, x :int):
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

def urn_probability(color :str, l :list):
    r = l.count("r")
    b = l.count("b")
    if (color == "r"):
        return (r/len(l))
    elif (color == "b"):
        return (b/len(l))
    else:
        return

def urn_probability_fraction(color :str, l :list):
    r = l.count("r")
    b = l.count("b")
    if (color == "r"):
        return (Fraction(r, len(l)))
    elif (color == "b"):
        return (Fraction(b, len(l)))
    else:
        return

def urn_probability_of_retrieval(chain_to_find : list, x :list, y :list, z:list):
    """Calculates the probability of a specific chain to be found within 3 lists
    """
    if (len(chain_to_find)!=0 or len(x)!=0 or len(y)!=0 or len(z)!=0):

        a= urn_probability_fraction(chain_to_find[0], x)
        b= urn_probability_fraction(chain_to_find[1], y)
        c= urn_probability_fraction(chain_to_find[2], z)

        final_probability = a*b*c
        return (final_probability)
    return (0)
