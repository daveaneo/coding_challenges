# Project Euler Problem 35
# https://projecteuler.net/problem=35
# Mar 5 2020
# Description:
''' Circular Primes '''

from timelines import time_check
import itertools

MAX_PRIME = 10 ** 6


def get_rotations(num):
    listy = []
    num = str(num)
    length = len(num)

    for i in range(length):
        num = num[1:] + num[0]
        listy.append(int(num))
    return listy


def method_1():
    n = MAX_PRIME
    numbers = set(range(n, 1, -1))  # speed difference?
    primes = []
    i = 1
    step_size = MAX_PRIME
    while i == 1 or primes[-1] < MAX_PRIME:
        # Create sieve chunk
        numbers = set(range(2 + step_size * (i - 1), 2 + step_size * i))  # speed difference?
        # remove non-primes from new chunk
        for p in range(2, 2 + step_size * i):
            numbers.difference_update(set(range(p * 2, 2 + step_size * i, p)))  # remove all multiples of p

        # append primes with new primes from chunk
        while numbers:
            p = numbers.pop()
            primes.append(p)
            numbers.difference_update(set(range(p * 2, 2 + step_size * i, p)))  # remove all multiples of p
        i += 1

    primes.sort()

    # remove extras at end
    while (primes[-1] > MAX_PRIME):
        primes.pop()

    # print(primes)
    print(f'total primes found: {len(primes)}, biggest prime: {primes[-1]}')

    primes = set(primes)

    count = 0
    for prime in primes:
        is_circular = True
        for perm in get_rotations(prime): # originally used permutations by mistake
            if perm not in primes:
                is_circular = False
                break
        if is_circular:
            count += 1
            print(f'{prime} is circular.')

    return count


time_check()
ans = method_1()
print(f'method_1 returns {ans}')
time_check()
