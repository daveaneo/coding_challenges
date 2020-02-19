# Project Euler Problem 23
# https://projecteuler.net/problem=23
# Feb 18 2020
# Description:
"""  Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers. """

UPPER_THRESH = 28123


def get_proper_divisors(num):
    divs = [i for i in range(1, int(num ** 0.5 + 1)) if num % i == 0]
    quot = [int(num / i) for i in divs]
    return list(set(divs + quot) - {num})


def method_1():
    abundant_numbers = []
    for i in range(UPPER_THRESH):
        divisors = get_proper_divisors(i)
        if sum(divisors) > i:
            abundant_numbers.append(i)
    all_nums = set(i for i in range(UPPER_THRESH))
    sums = set()
    for i, num in enumerate(abundant_numbers):
        for j in range(i, len(abundant_numbers)):
            sums.add(num + abundant_numbers[j])
    return sum(list(set(all_nums) - sums))

ans = method_1()
print(f'method_1 returns: {ans}')
