# Project Euler Problem 24
# https://projecteuler.net/problem=24
# Feb 18 2020
# Description:
""" What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9? """

import itertools
import math

TARGET_NUM = 10 ** 6
#TARGET_NUM = math.factorial(9) + 1


def method_1():
    num_list = [i for i in range(10)]
    length = len(num_list)
    #    print(num_list)
    dic_facts = {}
    for i in range(length + 1):
        dic_facts[i] = math.factorial(i)

    last_permutation = []
    remaining_permutations = TARGET_NUM - 1

    for i in range(0, length):
        quotient = remaining_permutations // dic_facts[length - i - 1]

        if i == length-1:
            chosen = int(num_list[0]) # why? is something implemented wrongly?
        else:
            chosen = int(num_list[quotient])
        last_permutation.append(chosen)
        num_list.remove(chosen)
        remaining_permutations -= dic_facts[10-i - 1]*quotient

    return "".join([str(i) for i in last_permutation])


ans = method_1()
print(f'method_1 returns: {ans}')
