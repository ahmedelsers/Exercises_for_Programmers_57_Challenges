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
        return feet_to_meter(length) * feet_to_meter(width)
    if feet_or_meter == 'm':
        return meter_to_feet(length) * meter_to_feet(width)


try:
    feet_or_meter = input("Your inputs will be in Feet or Meter? f or m: ")
    if feet_or_meter == 'f':
        length = float(input("What is the length of the room in feet? "))
        width = float(input("What is the width of the room in feet? "))
        print("The area is:\n"
              "{} square feet\n"
              "{} square meters".format((length*width),
                                        round(square_area(length, width, feet_or_meter), 3))
              )
    elif feet_or_meter == 'm':
        length = float(input("What is the length of the room in meter? "))
        width = float(input("What is the width of the room in meter? "))
        print("The area is:\n"
              "{} square meters\n"
              "{} square feet".format((length * width),
                                        round(square_area(length, width, feet_or_meter), 3))
              )
    else:
        print("So, f for feet, m for meter, is it clear now?")
except:
    print("Please enter numbers only.")
