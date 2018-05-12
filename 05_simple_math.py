#!/usr/bin/env python3

while True:
    try:
        num1 = input("What is the first number? ")
        num2 = input("What is the second number? ")

        num1 = int(num1)
        num2 = int(num2)

        def sum(num1, num2):
            return num1 + num2


        def diff(num1, num2):
            return num1 - num2


        def product(num1, num2):
            return num1 * num2


        def div(num1, num2):
            return num1 // num2


        print(num1, " + ", num2, " = ", sum(num1, num2), "\n",
              num1, " - ", num2, " = ", diff(num1, num2), "\n",
              num1, " * ", num2, " = ", product(num1, num2), "\n",
              num1, " / ", num2, " = ", div(num1, num2))

    except (ValueError, TypeError):
        print("Please enter numbers only!")
    except ZeroDivisionError:
        print("Please enter numbers greater than 0")
    except (KeyboardInterrupt, EOFError):
        print()
        print("Bye, Bye!")
        exit(0)
