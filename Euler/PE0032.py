# Project Euler Problem 32
# https://projecteuler.net/problem=32
# Mar 2 2020
# Description:

from timelines import time_check
import itertools

"""  Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital."""

HIGHEST_NUM = 987654321
all_digits = set(range(1, 10))


def get_digits_a(number):
    return [int(c) for c in str(number)]


def get_all_factors(number):
    factor_list = []


time_check()


def method_1():
    product_set = set()
    product_list = []
    dic_left = {}
    for i in range(1, 10):
        perms = list(itertools.permutations(all_digits, i))
        for perm in perms:
            number_to_match = "".join([str(i) for i in perm])
            number_to_match = int(number_to_match)
            rem_digits = all_digits - set(perm)
            comp_perms = list(itertools.permutations(rem_digits, len(rem_digits)))
            for comp_perm in comp_perms:
                comp_perm = "".join([str(i) for i in comp_perm])
                for j in range(1, len(comp_perm) - 1):
                    left = int(comp_perm[:j])
                    right = int(comp_perm[j:])
                    if left * right == number_to_match:
                        product_list.append([left, right])
                        if right < left:
                            left, right = right, left
                        dic_left[left] = left * right
                        product_set = product_set | {right * left}
    # return sum([x for x in dic_left.values()]) # misunderstood problem
    return sum(product_set)


# tweaked version of meth 1
def method_2():
    product_set = set()
    product_list = []
    dic_left = {}
    for i in range(4, 5):
        perms = list(itertools.permutations(all_digits, i))
        for perm in perms:
            number_to_match = "".join([str(i) for i in perm])
            number_to_match = int(number_to_match)
            rem_digits = all_digits - set(perm)
            comp_perms = list(itertools.permutations(rem_digits, len(rem_digits)))
            for comp_perm in comp_perms:
                comp_perm = "".join([str(i) for i in comp_perm])
                for j in range(1, len(comp_perm) - 1):
                    left = int(comp_perm[:j])
                    right = int(comp_perm[j:])
                    if left * right == number_to_match:
                        product_list.append([left, right])
                        if right < left:
                            left, right = right, left
                        dic_left[left] = left * right
                        product_set = product_set | {right * left}
    # return sum([x for x in dic_left.values()]) # misunderstood problem
    return sum(product_set)


def pandigital(a, b):
    a = list(str(a) + str(b) + str(a * b))
    a.sort()
    if a == list("123456789"):
        return True
    return False

full_set = set(list("123456789"))

def pandigital_2(a,b):
    return full_set == set(list(str(a) + str(b) + str(a * b)))

# Taken from Euler Forum, augmented
def method_3():
    nummy = set()

    for a in range(2, 4938):  # 2 to 9876/2
        for b in range(2, 9876//a): # 1000//a to 9876//a (but the math made it too slow)
            temp_len = len(str(a)) + len(str(b)) + len(str(a * b))

            if temp_len > 9:
                break
            elif temp_len != 9:
                pass
            else:
                if pandigital_2(a, b): # and a * b not in nummy:
                    nummy = nummy | {a*b}
    return sum(nummy)


# time_check()
# ans = method_1()
# print(f'method 1 returns: {ans}')
time_check()

# ans = method_2()
# print(f'method 2 returns: {ans}')

time_check()


ans = method_3()
print(f'method 3 returns: {ans}')
time_check()
