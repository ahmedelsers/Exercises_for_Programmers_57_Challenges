#!/usr/bin/env python3


import datetime


current_age = int(input("What is your current age? "))
retirement_age = int(input("At what age would you like to retire? "))

current_date = datetime.date.today()
current_year = datetime.date.today().year

years_to_retirement = retirement_age - current_age
years_to_retirement_in_days = years_to_retirement * 365

retirement_date = current_date + datetime.timedelta(days=years_to_retirement_in_days)
retirement_year = retirement_date.year


if years_to_retirement < 0:
    print("You could retire {} years ago if you want!".format(abs(years_to_retirement)))
else:
    print("You have {} years left until you can retire.\n"
          "It's {}, so you can retire in {}.".format(years_to_retirement,current_year,retirement_year))
