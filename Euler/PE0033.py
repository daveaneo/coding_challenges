# Project Euler Problem 33
# https://projecteuler.net/problem=33
# Mar 5 2020
# Description:
''' Digit cancelling fractions '''

from timelines import time_check

from fractions import Fraction


def method_1():
    list_of_pairs = []
    for i in range(12, 99):
        for j in range(12, i):
            # j / i
            # cancel a number
            if i == j or i % 10 == 0:
                continue
            digits_num = set(int(c) for c in str(j))
            digits_den = set(int(c) for c in str(i))
            digits_shared = digits_den & digits_num
            if len(digits_shared) == 2:  # impossible to  work out (53/35)
                continue
            if len(digits_shared) == 1:
                # print(f'i: {i}, j: {j}, digits_shared: {digits_shared}')

                if 0 in digits_shared:  # trivial examples
                    continue
                new_num = digits_num - digits_shared
                new_den = digits_den - digits_shared
                if not new_num:  # if there were two digits of same
                    new_num = digits_shared
                if not new_den:  # if there were two digits of same
                    new_den = digits_shared

                if new_num.pop() / new_den.pop() == j / i:
                    list_of_pairs.append((j, i))
                # problem -- multiple digits in number

    print(f'list_of_pairs: {list_of_pairs}')
    numerator = 1
    denominator = 1
    for num, den in list_of_pairs:
        numerator *= num
        denominator *= den
    return Fraction(numerator, denominator).denominator


# concept taken from euler forums
def method_2():
    # solve d1*d2/(d2*d3) = d1/d3 = (d1*10 + d2) / (d2*10 + d3)
    # d2 = 9*d1d3/(10d1 - d3)

    tot_fraction = Fraction(1,1)
    for d_one in range(0, 10):
        for d_three in range(d_one + 1, 10):
            if 10 * d_one == d_three or d_one*d_three == 0:
                continue
            d_two = 9 * d_one * d_three / (10 * d_one - d_three)
            if d_two > 9:
                continue
            if d_two == int(d_two):
                tot_fraction *=  Fraction(int(d_one*10+d_two), int(d_two*10 + d_three))


    return tot_fraction.denominator


time_check()
ans = method_1()
print(f'method_1 returns: {ans}')
time_check()

ans = method_2()
print(f'\nmethod_2 returns: {ans}')
time_check()
