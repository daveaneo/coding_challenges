# Project Euler Problem 10
# https://projecteuler.net/problem=10
# Feb 5 2020
# Description:
'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.'''

MAX_PRIME = 2*10**6

# Taken from Stack Overflow ( sieve of Erathostenes)
def method_1():
    n = MAX_PRIME
    numbers = set(range(n, 1, -1))  # speed difference?
    primes = []
    i = 1
    step_size = MAX_PRIME
    while i == 1 or primes[-1] <= MAX_PRIME:
        first = 0
        # Create sieve chunk
        numbers = set(range(2 + step_size*(i-1), 2 + step_size * i))  # speed difference?

        # remove non-primes from new chunk
        for p in range(2, 2+step_size*i):
            numbers.difference_update(set(range(p * 2, 2 + step_size * i, p)))  # remove all multiples of p

        # append primes with new primes from chunk
        while numbers:
            p = numbers.pop()
            primes.append(p)
            numbers.difference_update(set(range(p * 2, 2+step_size*i, p)))  # remove all multiples of p
        i += 1
    primes = [p for p in primes if p < MAX_PRIME]
    primes.sort()
    print(f'---{MAX_PRIME} primes---')
    print(f'{primes[:MAX_PRIME]} --> {sum(primes[:MAX_PRIME])}')
    return sum(primes[:MAX_PRIME])

ans = method_1()

print(f'method_1 -- ans: {ans}')
