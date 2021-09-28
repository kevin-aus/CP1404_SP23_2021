"""Testing functions."""
# import math
from math import *
import string

# initialize constants
COUNTRIES = ['Australia', 'China', 'India', 'Singapore', 'Quit']


def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32.0


def count_letters(text):
    """Count the number of letters in text."""
    count = 0
    for character in text:
        if character.lower() in string.ascii_letters:
            count += 1
    return count


def display_menu():
    """Diplay a list of countries"""
    print("\nCountries")
    print("========")
    # print("1. Australia")
    # print("2. China")
    # print("3. India")
    # print("4. Singapore")
    # print("5. Quit")
    for i in range(len(COUNTRIES)):
        print(str(i + 1) + '. ' + COUNTRIES[i])


def main():
    my_num = 5
    print("Square root of {} is {:.2f}".format(my_num, sqrt(my_num)))
    print(celsius_to_fahrenheit(30))
    print(count_letters("jc123456"))
    display_menu()
    option = int(input("Enter 1-4 for country. Enter 5 to quit: "))
    while option != 5:
        if 0 < option < 5:
            print(COUNTRIES[option - 1])
        else:
            print("Invalid choice.")
        display_menu()
        option = int(input("Enter 1-4 for country. Enter 5 to quit: "))
    print("Bye!")


# start the program
main()
