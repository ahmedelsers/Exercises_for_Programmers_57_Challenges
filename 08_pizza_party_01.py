#!/usr/bin/env python3

import math

def pizza_needed(number_of_people, number_of_slices_for_each, number_of_slices_per_pizza):
    return math.ceil((number_of_people * number_of_slices_for_each) / number_of_slices_per_pizza)

def plural(num):
    if num == 0:
        add_s = 's'
    if num == 1:
        add_s = ''
    if num > 1:
        add_s = 's'
    return add_s


try:
    number_of_people = int(input("How many people? "))
    number_of_slices_per_pizza = int(input("How many slices per pizza? "))
    number_of_slices_for_each = int(input("How many slices each person wants? "))

    print("You need to purchase {0} full pizza{1}".format(pizza_needed(number_of_people, number_of_slices_for_each, number_of_slices_per_pizza),
                                                          plural(pizza_needed(number_of_people, number_of_slices_for_each, number_of_slices_per_pizza))))


except:
    print("Please enter numbers only")
