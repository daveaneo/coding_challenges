# Project Euler Problem 5
# https://projecteuler.net/problem=5
# Jan 30 2020
# Description:
'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

# Factor all numbers
# Have Corresponding Power

# Taken From Stack Overflow
def get_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def method_1():
    dic_factors = {}
    for num in range(1, 21):
        factors = get_prime_factors(num)
        # Create a dictionary of factor -> power
        for factor in factors:
            count = factors.count(factor)
            if factor not in dic_factors:
                dic_factors[factor] = count
            else:
                if dic_factors[factor] < count:
                    dic_factors[factor] = count
    print(f'Dictionary: {dic_factors}')

    # Multiply all Factors
    lowest_multiple = 1
    for factor, count in dic_factors.items():
        lowest_multiple = lowest_multiple * (factor ** count)

    return lowest_multiple


lowest_multiple = method_1()

print(f'Lowest Possible Multiple: {lowest_multiple}')
