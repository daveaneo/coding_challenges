# Project Euler Problem 27
# https://projecteuler.net/problem=27
# Feb 18 2020
# Description:
""" Find the product of the coefficients, a
and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.  """

import itertools

MAX_PRIME = 1000 * 1000 + 1000

def method_1():

    n = MAX_PRIME
    numbers = set(range(n, 1, -1))  # speed difference?
    primes = set()
    i = 1 # redundant. Previously had a loop
    step_size = MAX_PRIME
    flag = 0

    # Create sieve chunk
    numbers = set(range(2 + step_size * (i - 1), 2 + step_size * i))  # speed difference?

    # remove non-primes from new chunk
    for p in range(2, 2 + step_size * i):
        numbers.difference_update(set(range(p * 2, 2 + step_size * i, p)))  # remove all multiples of p

    # append primes with new primes from chunk
    while numbers:
        p = numbers.pop()
        primes.add(p)
        numbers.difference_update(set(range(p * 2, 2 + step_size * i, p)))  # remove all multiples of p

    #    primes = set(primes)
    #print(f' number of primes found: {len(primes)}')

    best_vals = (0, 0)
    best_n = -1
    for a in range(-1000, 1000):
        print(f'a = {a}')
        for b in range(-1000, 1000):
            for n in itertools.count(0):
                if (n**2 + a*n + b) not in primes:
                    if n > best_n:
                        best_n = n
                        best_vals = (a, b)
                    break
    print(f'vals: {best_vals} yielded: {best_n}')
    print(f'their product is: {best_vals[0] * best_vals[1]}')

    return best_vals[0] * best_vals[1]

ans = method_1()
print(f'method_1 returns: ')
