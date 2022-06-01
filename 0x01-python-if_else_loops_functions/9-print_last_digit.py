#!/usr/bin/bash
def print_last_digit(number):
    if number < 0:
        number = number * -1
    else:
        number = number * 1
    print(number % 10)
