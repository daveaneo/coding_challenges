# Project Euler Problem 15
# https://projecteuler.net/problem=15
# Feb 6 2020
# Description:
'''How many such routes are there through a 20×20 grid?'''

import math
import time

dic_terms = {}

DIM_X = 20
DIM_Y = 20

def speed_race():
    beg = time.time()
    total = method_1(DIM_X, DIM_Y)
    end = time.time()
    time_1 = end - beg

    beg = time.time()
    total = method_2(DIM_X, DIM_Y)
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


# recursion
def method_1(x,y):
    if x == 0 or y == 0:
        return 1
    coords = (x, y)
    if coords in dic_terms:
        paths = dic_terms[coords]
    else:
        paths = method_1(x-1, y) + method_1(x, y-1)
        dic_terms[coords] = paths
    return paths


# mathy
def method_2(x, y):
    return math.factorial(x + y)/math.factorial(x)/math.factorial(y)


#for i in range(1, 21):
#    temp = method_1(i, i)
#    print(f'({i},{i}) --> {temp}')

ans = method_1(DIM_X, DIM_Y)
print(f'\nMethod 1 --- The answer is: {ans}')

ans = int(method_2(DIM_X, DIM_Y))
print(f'\nMethod 2 --- The answer is: {ans}')


# method 1 was faster until dimension equal 21
ratio, fastest_time, fastest_method = speed_race()
print(f'The fastest method was #{fastest_method}. It was {ratio}x faster!')

