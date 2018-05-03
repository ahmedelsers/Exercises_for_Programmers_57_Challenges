#!/usr/bin/env python3

quote = input("What is the quote? ")
who_said_it = input("Who said it? ")

print(who_said_it + " says, " + quote)

# Challenge

quotes = {"Obi-Wan Kenobi": "These aren't the droids you're looking for."}

for who, quote in quotes.items():
    print(who + " says, " + quote)