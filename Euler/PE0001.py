# Project Euler Problem 1
# https://projecteuler.net/problem=1
# Jan 30 2020
# Description:
'''If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.'''

def method_1():
    multiples = [i for i in range(1,1000) if i%5 == 0 or i%3 == 0]
    return sum(multiples)

sum = method_1()
print(f'Sum of multiples: {sum}')


