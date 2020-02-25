#!/usr/bin/python3
"""Python implementation of the square middle method seen in class"""

def generator(seed_value: str):
    """method that contains the formula to obtain a randomized value via the
    square middle method"""

    print(seed_value)
    seed_value_squared = str(int(seed_value)**2)

    elems_to_crop = int((len(seed_value_squared)-len(seed_value))//2)
    result = 0
    if int(seed_value) != 0:
        if len(seed_value_squared)%2 != 0:
            result = int(seed_value_squared[elems_to_crop:-elems_to_crop])
        else:
            result = int(seed_value_squared[elems_to_crop:-elems_to_crop-1])

    return str(result)

def main():
    """main method for the class"""

    seed_value = 154    #initialization value for the method

    for _ in range(13):
        seed_value = generator(str(seed_value))

if __name__ == "__main__":
    main()
