# Project Euler Problem 26
# https://projecteuler.net/problem=26
# Feb 18 2020
# Description:
""" Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part. """

import itertools
import time

UPPER_THRESH = 999

# taken  from forum
def recur_len(n):
    # digits for unit fraction 1/n
    r = 10  # initial remainder (10/n)/10
    seen = {}  # remainder -> first pos
    for i in itertools.count(0):
        if r == 0:
            return 0  # divides evenly.
        elif r in seen:
            return i - seen[r]  # curpos - firstpos
        seen[r] = i
        r = 10 * (r % n)

# taken from forum
def method_1():

    len, i = max((recur_len(i), i) for i in range(2, 1000))
    return(i)

def method_2():
    greatest_repetition = 0
    winning_digit = 2
    for i in range(2, UPPER_THRESH):
        digit_check = UPPER_THRESH + 10
        rem = (1 % i)
        digits = []  # igore initial 0
        num_digits = 0
        passes = 0
        repeater = False
        dic_remainder = {}
        while rem != 0:
            rem *= 10
            if rem in dic_remainder:
                repeater = True
                break
            else:
                dic_remainder[rem] = len(digits) # index of where the pattern started
            while rem < i:
                rem *= 10
                passes += 1
                digits.append(0)
                num_digits += 1

            quo = rem // i
            rem = rem % i

            digits.append(quo)
            if rem == 0:
#                print(f'non repeater')
                repeater = 0
                break
            elif num_digits == digit_check:
#                print(f'Exceeded checking limit without repeating.')
                break
            # check for repetition
        if repeater:
            num_reps = len(digits[dic_remainder[rem]:])
        else:
            num_reps = 0

        if num_reps > greatest_repetition:
            greatest_repetition = len(digits)
            winning_digit = i
    return winning_digit


def speed_race():
    beg = time.time()
    total = method_1()
    end = time.time()
    time_1 = end - beg

    beg = time.time()
    total = method_2()
    end = time.time()
    time_2 = end - beg

    fastest_method = 2
    ratio = time_1/time_2
    fastest_time = time_2
    if time_2 > time_1:
        fastest_method = 1
        ratio = time_2/time_1
        fastest_time = time_1

    print(f'Method {fastest_method} was {ratio} times faster.')
    return ratio, fastest_time, fastest_method



# ans = method_1()
# print(f'method_1 returns {ans}')

ans = method_2()
print(f'method_2 returns {ans}')

ratio, fastest_time, fastest_method = speed_race()
