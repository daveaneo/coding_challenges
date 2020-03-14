# Project Euler Problem 34
# https://projecteuler.net/problem=34
# Mar 5 2020
# Description:
''' Digit Factorials '''

import math
from timelines import time_check

UPPER_BOUND = 2540160 # (7*9!)--Calc upper bound -- n*9! = 10**n -1 -- where these cross, exists the highest

dic_facts = {i:math.factorial(i) for i in range(10)}

"""
 # Discover Upper Bound
for n in range(1000):
    if 10**n - 1 > n*dic_facts[9]:
        print(f'n: {n}, max: {n*dic_facts[9]}')
        UPPER_BOUND = n*dic_facts[9]
        break
"""

def fac_of_digits(num):
        return sum(dic_facts[int(c)] for c in str(num))

def method_1():
    digit_factorial_list = []
    for i in range(10, UPPER_BOUND):
        # print(f'{i}   |   {fac_of_digits(i)}')
        if i == fac_of_digits(i):
            digit_factorial_list.append(i)
    return sum(digit_factorial_list)

def method_2():
    list_of_values = [math.factorial(i) for i in range(10)]
    digit_factorial_list = []
    for i in range(10, UPPER_BOUND):
        # print(f'{i}   |   {fac_of_digits(i)}')
        if i == sum(list_of_values[int(c)] for c in str(i)): #fac_of_digits(i):
            digit_factorial_list.append(i)
    return sum(digit_factorial_list)

def method_3():
    # map out linear range of facttorials 0-9

    list_of_values = [math.factorial(i) for i in range(10)]
    winning_nums = []
    list_of_lists = [(i, list_of_values[i]) for i in range(1, 10)] #[[i] for i in list_of_values]
    dic_path_to_value = {i: list_of_values[i] for i in range(1,10)}
    for i in range(2,8): # 8
        temp_dic = dic_path_to_value.copy()
        for num, l in temp_dic.items():
            for pos, value in enumerate(list_of_values):
                new_single = l + value
                new_num = 10*num + pos
                if new_num > UPPER_BOUND:
                    break
                dic_path_to_value[new_num] = new_single
                if num < 10:
                    if num in dic_path_to_value: # in case it has already been removed by someting similar
                        del dic_path_to_value[num]
                if new_single == new_num:
                    print(f'appending: {new_num}')
                    winning_nums.append(new_num)
                if num in dic_path_to_value: # in case it has already been removed by someting similar
                    del dic_path_to_value[num]
        # cleanup keys ?
        # any dictionary item with same value can be removed -- true or not? NOT. i think.
        # any larger than this and there are memory problems
        # could probably start with larger numbers and eliminate impossible ones (which wont ever reach target)

    return sum(winning_nums)




"""
time_check()
ans = method_1()
print(f'method_1 returns {ans}')
time_check()
"""

"""
ans = method_2()
print(f'method_2 returns {ans}')
time_check()

"""

time_check()
ans = method_3()
print(f'method_3 returns {ans}')
time_check()
