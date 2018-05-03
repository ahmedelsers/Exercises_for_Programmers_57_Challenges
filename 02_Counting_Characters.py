#!/usr/bin/env python3

string = input("What is the input string? ")

if string:
    print("{} has {} characters".format(string, len(string)))
else:
    print("You must enter something to count!")