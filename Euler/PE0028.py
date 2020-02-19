# Project Euler Problem 28
# https://projecteuler.net/problem=28
# Feb 19 2020
# Description:
""" What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way? """

UPPER_LEN_THRESH = 1001

def method_1():
    total = 1 # first square
    # sum over corners of increasingly larger squares
    for i in range(1, 1 + ((UPPER_LEN_THRESH-1) >> 1)):
        s = 2*i+1 # length of each side
        sum_of_corners = 4*s**2 - 3*(2*s-2)
        print(f'{i} --> yields length: {s}, perimiter: {sum_of_corners}')
        total += sum_of_corners
    return total


ans = method_1()
print(f'method_1 returns: {ans}')