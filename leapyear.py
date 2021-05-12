#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on May 2021
# This program runs the leap year program

import string


def main():
    # this function runs the leap year program

    # input
    print("Welcome!")
    num_year = str(input("Please enter the year: "))

    # process and output
    try:
        num_year = int(num_year)
        if num_year % 4 == 0:
            if num_year % 100 == 0:
                if num_year % 400 == 0:
                    print("{} is a leap year!".format(num_year))
        else:
            print("{} is not a leap year!".format(num_year))
    except Exception:
        print("{} is invalid data.".format(num_year))
    finally:
        print("Thanks for participating!")


if __name__ == "__main__":
    main()
