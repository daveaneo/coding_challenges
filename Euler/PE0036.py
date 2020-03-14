# Project Euler Problem 36
# https://projecteuler.net/problem=36
# Mar 6 2020
# Description:
"""Double-base palindromes"""

from timelines import time_check

MAX_NUM = 10**6
double_palindromes = {0, 1}
MAX_BIN_LEN = len(bin(MAX_NUM))-2


def is_int_palindrome(num):
    num = str(num)
    if num == num[::-1]:
        return True
    else:
        return False


def method_1():
    fill_set("11")
    fill_set("00")
    fill_set("0")
    fill_set("1")

    return sum(double_palindromes)


def fill_set(b):
    # starting number
    # convert to int, check for palindrome
    # add to total
    global double_palindromes


    int_val = int(b, 2)
    if int_val > MAX_NUM:
        return
    elif "1" not in b:
        if int("1" + b, 2) > MAX_NUM:
            return

    if b[-1] == "1": # ignore right 0s, since we must ignore left 0s
        if is_int_palindrome(int_val):
            double_palindromes |= {int_val}

    #go 0
    fill_set("0" + b + "0")

    #go 1
    fill_set("1" + b + "1")



def method_2():
    return sum([i for i in range(1, MAX_NUM) if bin(i)[2:] == bin(i)[2:][::-1] and str(i) == str(i)[::-1]])


time_check()
ans = method_1( )
print(f'method_1 returns: {ans}')
time_check()

ans = method_2( )
print(f'method_2 returns: {ans}')
time_check()

