# Project Euler Problem 12
# https://projecteuler.net/problem=12
# Feb 5 2020
# Description:
'''Find the greatest product of a line of 4 numebers'''

from functools import reduce

MAX = 5
THRESHOLD = 500


def get_prime_factors(num):
    """Returns a diction of prime_factors:power"""
    i = 2
    factors = {}
    n = num
    while i*i <= num and i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
    if n != 1:
        if n in factors:
            factors[n] += 1
        else:
            factors[n] = 1
    return factors

def get_num_factors_via_helper(n):
    return len(set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))))


def method_1():
    n = 1
    factors = []
    high = 0
    num_factors = 0
    while num_factors < THRESHOLD:
        # calculate sum mathematically
        sum_num = int(n*(n+1)/2)
        num_factors = get_num_factors_via_helper(sum_num)
        if num_factors > high:
            high = num_factors
#            print(f'{n}th triangle ({sum_num}): --> {high}')
        print(f'{n}th triangle ({sum_num}): --> {num_factors}')
        n += 1
    return sum_num


def method_2():
    tri_val = 1
    total_factors = 1
    high = 1
    while total_factors < THRESHOLD:
        tri_val += 1
        prime_factors = get_prime_factors(tri_val*(tri_val+1)/2)
        total_factors = 1
        facts = []
        for factor, exp in prime_factors.items():
            total_factors *= (1+exp)
            for i in range(exp):
                facts.append(factor)
#        print(f'Triangle({tri_val}) has factors: {facts}, and total factors: {total_factors}')
        if total_factors > high:
            high = total_factors
            print(f'{tri_val}th triangle ({total_factors}): --> {high}')

    return tri_val * (tri_val + 1) / 2

def method_3():
    tri_val = 1
    total_factors = 1
    high = 1
    while total_factors < THRESHOLD:
        tri_val += 1
        if tri_val %2 ==0:
            dic_1 = get_prime_factors(tri_val/2)
            dic_2 = get_prime_factors(tri_val+1)
        else:
            dic_1 = get_prime_factors(tri_val)
            dic_2 = get_prime_factors((tri_val+1)/2)
        dic_1.update(dic_2)
        total_factors = 1
        facts = []
        prime_factors = dic_1
        for factor, exp in prime_factors.items():
            total_factors *= (1+exp)
            for i in range(exp):
                facts.append(factor)
#        print(f'Triangle({tri_val}) has factors: {facts}, and total factors: {total_factors}')
        if total_factors > high:
            high = total_factors
            print(f'{tri_val}th triangle ({total_factors}): --> {high}')

    return tri_val * (tri_val + 1) / 2

def method_4():
    # bottom up approach
    # start with even n, calculate n/2 and n divisors
    # check for solution, increase n if not found
    # ToDo ---
    total_factors = 1
    n = 1
    while total_factors < THRESHOLD:
        n += 2
        evens = get_prime_factors(n/2)
        odds = get_prime_factors((n+1)/2)


ans = method_4()

print(f'method 2 -- ans: {ans}')