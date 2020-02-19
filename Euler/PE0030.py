# Project Euler Problem 30
# https://projecteuler.net/problem=30
# Feb 19 2020
# Description:
"""  Find the sum of all the numbers that can be written as the sum of fifth powers of their digits. """

import math

UPPER_THRESH = 6*9**5  # after this value, sums of power-five integers can't catch up
LOWER_THRESH = 10

def get_upper_thresh():
    power = 9**5
    for i in range(15):
        print(f'{i} -- > max_number_sum: {power*i}')
        if 10**i > power*i:
            print(f'  exceeded at i = {i}')
    print(f'guess value 1: {power*6} ')
    #  UPPER_THRESH = 6*9**5
    """ Mathematically, we could solve 10^i=i*9^5, rounding up for (not so?) obvious reasons. i represents the number of digits."""

    return 0

def method_1():
    values = set()
    for i in range(LOWER_THRESH, UPPER_THRESH+1):
        temp_sum = sum([int(c)**5 for c in str(i)])
        # check if equal then add to set
        if temp_sum == i:
            values.add(i)
            print(f'Adding {i} -- > {temp_sum}')

    return sum(values)

ans = method_1()
print(f'method_1 returns: {ans}')
