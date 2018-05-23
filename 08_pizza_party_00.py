#!/usr/bin/env python3


def slices_per_person(number_of_people, number_of_pizzas, number_of_slices_per_pizza):
    return (number_of_pizzas * number_of_slices_per_pizza) // number_of_people

def leftOver(number_of_people, number_of_pizzas, number_of_slices_per_pizza):
     return (number_of_pizzas * number_of_slices_per_pizza) % number_of_people

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
    number_of_pizzas = int(input("How many pizzas do you have? "))
    number_of_slices_per_pizza = int(input("How many slices per pizza? "))

    print("{0} people with {1} pizza{2}".format(number_of_people, number_of_pizzas, plural(number_of_pizzas)))
    print("each person gets {0} piece{1} of pizza".format(slices_per_person(number_of_people, number_of_pizzas, number_of_slices_per_pizza),
                                                          plural(slices_per_person(number_of_people, number_of_pizzas, number_of_slices_per_pizza))
                                                          )
          )
    print("There are {0} leftover piece{1}".format(leftOver(number_of_people, number_of_pizzas, number_of_slices_per_pizza),
                                                   plural(leftOver(number_of_people, number_of_pizzas, number_of_slices_per_pizza))
                                                   )
          )

except:
    print("Please enter numbers only")
