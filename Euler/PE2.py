# Project Euler Problem 2
# https://projecteuler.net/problem=2
# Jan 30 2020
# Description:
'''By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms..'''

import time
import matplotlib.pyplot as plt
import seaborn as sns

MAX_FIB = 4*10**6

def generator_1():
    a = 1
    b = 2
    while True:
        yield a
        a, b = b, a+b

def method_1():
    total = 0
    for next_fib in generator_1():
        if next_fib > MAX_FIB:
            break
        else:
            if next_fib % 2 == 0:
                total += next_fib
    return total

def method_2():
    a = 1
    b = 2
    sum_even = 2
    while b < MAX_FIB:
        a, b = b, a+b
        if b % 2 == 0:
            sum_even += b
    return sum_even

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

    # print(f'Method {fastest_method} was {ratio} times faster.')
    return ratio, fastest_time, fastest_method

##############
# Speed Test #
##############

print(method_1())
print(method_2())


X = []
y1 = []
y2 = []
y3 = []
for i in range(10):
    ratio, fastest_time, fastest_method = speed_race()
    y1.append(ratio)
    y2.append(fastest_time)
    y3.append(fastest_method)
    X.append(i)
    MAX_FIB = MAX_FIB * 10000

# Plot Results
fig, ax = plt.subplots()
ax.plot(X, y1)
plt.title("Speed Ration (faster/slower)")
plt.legend()
plt.show()

