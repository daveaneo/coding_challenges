# Project Euler Problem 6
# https://projecteuler.net/problem=6
# Jan 30 2020
# Find the 100,001 th prime

import time

# Should choose better const name MAX_N_PRIME ???
MAX_PRIME = 10001



def get_primes():
    yield 2
    num = 3
    while True:
        prime_flag = 1
        for i in range(2, num):
            if num % i == 0:
                prime_flag = 0
        if prime_flag:
            yield num
        num += 1


def method_1():
    for i, prime in enumerate(get_primes()):
        if (i+1) == MAX_PRIME:
            return prime


# Taken from Stack Overflow ( sieve of Erathostenes)
def method_2():
    n = MAX_PRIME
    numbers = set(range(n, 1, -1))  # speed difference?
    primes = []
    i = 1
    step_size = 100
    while len(primes) <= MAX_PRIME:
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
    primes.sort()
    return primes[MAX_PRIME-1]


def speed_race():
    beg = time.time()
    total = method_1()
    end = time.time()
    time_1 = end - beg

    beg = time.time()
    total = method_2()
    end = time.time()
    time_2 = end - beg

    fastest_method = 2
    ratio = time_1/time_2
    fastest_time = time_2
    if time_2 > time_1:
        fastest_method = 1
        ratio = time_2/time_1
        fastest_time = time_1

    print(f'Method {fastest_method} was {ratio} times faster.')
    return ratio, fastest_time, fastest_method


# Method 2 was MUCH faster

#ans_1 = method_1()
ans_2 = method_2()

#print(f'The {MAX_PRIME}th is: {ans_1}')
#print(f'Method 1 -- The {MAX_PRIME}th is: {ans_1}')
print(f'Method 1 -- The {MAX_PRIME}th is: {ans_2}')


# ratio, fastest_time, fastest_method = speed_race()