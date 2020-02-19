# Project Euler Problem 20
# https://projecteuler.net/problem=20
# Feb 18 2020
# Description:
""" Evaluate the sum of all the amicable numbers under 10000. """

UPPER_THRESHOLD = 10000


def get_proper_divisors(num):
    divs = [i for i in range(1, int(num ** 0.5 + 1)) if num % i == 0]
    quot = [int(num / i) for i in divs]
    return list(set(divs + quot) - {num})


def method_1():
    amicable_numbers = []
    dic_d = {}
    # create dictionary
    for i in range(UPPER_THRESHOLD):
        divisors = get_proper_divisors(i)
        dic_d[i] = sum(divisors)
    # compare values in dictionary for match
    for key, value in dic_d.items():
        if value in dic_d and key == dic_d[value] and key != value:
            amicable_numbers += [value, key]
    return sum(list(set(amicable_numbers)))



ans = method_1()
print(f'method_1 returns: {ans}')