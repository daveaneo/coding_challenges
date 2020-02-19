# Project Euler Problem 22
# https://projecteuler.net/problem=22
# Feb 18 2020
# Description:
""" What is the total of all the name scores in the file? """

file_name = 'p022_names.txt'


def method_1():
    with open(file_name) as f:
        data = f.readline()

    data = data[1:-1]
    names = data.split('","')
    names.sort()

    total = 0
    for i, name in enumerate(names):
        for c in name:
            total += (i + 1) * (ord(c.lower()) - ord('a') + 1)
    return total


ans = method_1()
print(f'method_1 returns: {ans}')