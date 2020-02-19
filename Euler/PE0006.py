# Project Euler Problem 5
# https://projecteuler.net/problem=5
# Jan 30 2020
# Description:
'''Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.'''

import time
import numpy as np

MAX_RANGE = 100

def method_1():
    sum_1 = 0
    sum_2 = 0
    for i in range(MAX_RANGE+1):
        sum_1 += i*i
        sum_2 += i
    sum_2=sum_2**2

    return sum_2 - sum_1

def method_2():
    pass
    # is there a faster way?
    if MAX_RANGE % 2 == 0:
        sum_2 = int(MAX_RANGE*(MAX_RANGE/2 +1/2))**2
    else:
        sum_2 = ((MAX_RANGE+1)/2*MAX_RANGE)**2

    # Temp sum_1
    sum_1 = 0
    for i in range(MAX_RANGE + 1):
        sum_1 += i * i

    return sum_2 - sum_1

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



ans_1 = method_1()
ans_2 = method_2()
print(f'Answer 1: {ans_1}')
print(f'Answer 2: {ans_2}')

ratio, fastest_time, fastest_method = speed_race()
#print()
