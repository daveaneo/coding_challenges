# Project Euler Problem 16
# https://projecteuler.net/problem=16
# Feb 6 2020
# Description:
"""What is the sum of the digits of the number 2**1000?"""

import time

BIG_NUM = 2**1000

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

    # print(f'Method {fastest_method} was {ratio} times faster.')
    return ratio, fastest_time, fastest_method


def method_1():
    num_string = str(BIG_NUM)
    total = 0
    for letter in num_string:
        total += int(letter)
    return total

def method_2():
    num_string = str(BIG_NUM)
    return sum(int(i) for i in num_string)

def method_3():
    return sum(map(int, str(BIG_NUM)))

# method 3 was fastest!

ans = method_1()
print(f'\nMethod 1 -- The answer is: {ans}')

ans = method_2()
print(f'\nMethod 2 -- The answer is: {ans}')

ans = method_3()
print(f'\nMethod 2 -- The answer is: {ans}')

# compares only method 1 and 2
speed_race()
ratio, fastest_time, fastest_method = speed_race()
print(f'The fastest method was #{fastest_method}. It was {ratio} X faster!')
