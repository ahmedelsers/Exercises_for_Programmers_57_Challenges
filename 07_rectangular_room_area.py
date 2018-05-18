#!/usr/bin/env python3

import math

CF = 0.09290304


def square(var):
    return var**2

def feet_to_meter(feet):
    return math.sqrt(square(feet) * CF)

def meter_to_feet(meter):
    return math.sqrt(square(meter) / CF)

def square_area(length, width, feet_or_meter):
    if feet_or_meter == 'f':
        print("The area is:\n"
              "{} square feet\n"
              "{} square meters".format((length * width),
                                        round(feet_to_meter(length) * feet_to_meter(width), 3))
              )
    if feet_or_meter == 'm':
        print("The area is:\n"
              "{} square meters\n"
              "{} square feet".format((length * width),
                                      round(meter_to_feet(length) * meter_to_feet(width), 3))
              )


feet_or_meter = input("Your inputs will be in Feet or Meter? f or m: ")
if feet_or_meter not in ['f', 'm']:
    print("f for feet, m for meter, is it clear now?")
    exit(0)
else:
    try:
        length = float(input("What is the length of the room? "))
        width = float(input("What is the width of the room? "))
        square_area(length, width, feet_or_meter)
    except:
        print("Please enter numbers only.")
