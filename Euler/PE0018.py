# Project Euler Problem 18
# https://projecteuler.net/problem=18
# Feb 7 2020
# Description:
"""Find total path (greatest sum) """
'''top line at pos x can travel to the next line at either x or x+1'''

import functools
import time

TRIANGLE = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

SHOW_PROGRESSION = False

def method_1():
    words = TRIANGLE.splitlines()
    rows = []
    for i in range(0, len(words)):
        rows.append([int(j) for j in words[i].split()])

    height = len(rows)
    while height > 1:
        for i in range(len(rows[height-2])):
            if rows[height-1][i] > rows[height-1][i+1]:
                rows[height-2][i] += rows[height-1][i]
            else:
                rows[height-2][i] += rows[height-1][i+1]
        rows = rows[:-1] # drop last
        if SHOW_PROGRESSION:
            for i in range(len(rows)):
                print(rows[i])
            print("-"*10)
        height -=1
    return rows[0][0]


def method_2():
    t = list(map(lambda x: list(map(int, x.split())), TRIANGLE.split('\n')))
    ans = functools.reduce(method_2_helper, t[::-1])
    return ans

def method_2_helper(summy, line):
    a = list(map(lambda x: x[0]+x[1], zip(summy, line)))
    b = list(map(lambda x: x[0]+x[1], zip(summy[1:], line)))
    ret = list(map(max, zip(a, b)))
    return ret

ans = method_1()
print(f'\nMethod 1 -- The answer is: {ans}')

ans = method_2()
print(f'\nMethod 2 -- The answer is: {ans[0]}')

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

speed_race()