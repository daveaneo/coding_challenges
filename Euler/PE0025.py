# Project Euler Problem 25
# https://projecteuler.net/problem=25
# Feb 18 2020
# Description:
""" What is the index of the first term in the Fibonacci sequence to contain 1000 digits? """

DIVISOR = 10**999 # 10**(k-1), where k is number of digits

def method_1():
    a = 1
    b = 1
    n = 1
    while a // DIVISOR == 0:
        a, b = b, a + b
        n+=1

    return n

ans = method_1()
print(f'method_1 returns {ans}')


