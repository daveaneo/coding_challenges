# Project Euler #4
# https://projecteuler.net
# Calculate largest 3-digit set of multiplicands (?) that produce a palindrome
# Jan 28 2020

import numpy as np
import time

def is_palindrome(num):
    word = str(int(num))
    flag = 1
    for i in range((len(word)//2)):
        # print(f'i: {i}')
        if(word[i] != word[-i-1]):
            flag = 0
    return flag


def method_1():
    pals= []
    for x in range(1,DIM):
        for y in range(1,DIM):
            if is_palindrome(x*y):
                pals.append((x,y, x*y))
    biggest_pair = max(pals,key=lambda item: item[2])
    return biggest_pair

def method_2():
    # Create left
    A = np.zeros((DIM, DIM)).astype(int)
    for i in range(0, len(A)):
        A[i][i] = i + 1

    # create right
    B = np.ones((DIM, DIM)).astype(int)
    for i in range(0, len(B)):
        B[0][i] = i + 1
    for i in range(0, len(B)):
        B[i] = B[0]

    C = np.matmul(A, B)

    big_list = C.flatten()
    big_list[::-1].sort()
    biggest_pal = -1

    for num in big_list:
        if is_palindrome(num):
            biggest_pal = num
            break

    if biggest_pal == -1:
        print(f'no palindrome found.')
    else:
        multiplicands = np.where(C == biggest_pal)

    if len(multiplicands[0] > 1):
        # print(f'There are multiple answers. Choosing the first.')
        biggest = (multiplicands[0][0] + 1, multiplicands[0][1] + 1, biggest_pal)
    else:
        biggest = (multiplicands[0] + 1, multiplicands[0] + 1, biggest_pal)

    return biggest

############
# METHOD 2 #
############

DIM = 1000

start = time.time()
biggest = method_1()
end = time.time()
print(f'Time for method 1: {end - start}, biggest: {biggest}')

start = time.time()
biggest = method_2()
end = time.time()
print(f'Time for method 2: {end - start}, biggest: {biggest}')

print(f'biggest: {biggest}')
# print(f'The biggest item: {biggest[2]}')
