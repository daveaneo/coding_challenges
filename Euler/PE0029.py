# Project Euler Problem 29
# https://projecteuler.net/problem=29
# Feb 19 2020
# Description:
""" """

LOWER_THRESH = 2
UPPER_THRESH = 100


def method_1():
    set_of_powers = set()
    for i in range(LOWER_THRESH, UPPER_THRESH + 1):
        new_values = set(i ** j for j in range(LOWER_THRESH, UPPER_THRESH + 1))
        set_of_powers = new_values | set_of_powers
        print(f'{i} --> yields {len(set_of_powers)} unique results')
    return len(set_of_powers)


ans = method_1()
print(f'method_1 returns: {ans}')
