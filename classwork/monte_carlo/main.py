#!/usr/bin/python3
"""Main for the monte carlo pi approximation method seen in class"""

from sys import argv
from components import monte_carlo

def main():
    """main method for the class"""
    length = len(argv)
    if length == 2:
        print(monte_carlo(int(argv[1])))
    else:
        print("Usage: python3 main.py \"number of points to generate\"")

if __name__ == "__main__":
    main()
