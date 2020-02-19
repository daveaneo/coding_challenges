# Project Euler Problem 20
# https://projecteuler.net/problem=20
# Feb 18 2020
# Description:
""" Find the sum of the digits in the number 100! (factorial """

import math

temp = math.factorial(3)
print(temp)
GIVEN = 100

def method_1():
    word_num = str(math.factorial(GIVEN))
    return sum([int(c) for c in word_num])

ans = method_1()
print(f'method 1 returns: {ans}')