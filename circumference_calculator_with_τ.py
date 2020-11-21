#!/usr/bin/env python3

# Created by Jonathan Pasco-Arnone
# Created on November 2020
# This program calculates the circumference of a circle

import math
import constants


def main():
    print("This program calculates the circumference of a circle.")
    radius_str = input("Please enter a radius measurement: ")
    radius = int(radius_str)
    print("")
    print("If a circle has a radius of " + radius_str + "mm ")
    circumference = constants.TAU*radius
    print("Then the Area is {:.2f}mm".format(circumference))


if __name__ == "__main__":
    main()
