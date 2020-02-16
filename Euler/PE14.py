# Project Euler Problem 14
# https://projecteuler.net/problem=14
# Feb 6 2020
# Description:
'''Which starting number, under one million, produces the longest chain?'''
# todo (theoretically) save/load dictionary

THRESHOLD = 10 ** 6


def get_next_number(n):
    if n & 1 == 0:  # even
        return n >> 1 # speed bonus instead of type casting
    return 3 * n + 1


def method_1():
    dic_terms = {}
    i = 1
    largest_term_length = 1
    term_with_greatest_length = 1
    while i < THRESHOLD:
        terms = 1
        n = i
        while n != 1:
            # Check hash/dictionary
            if n in dic_terms:
                terms += dic_terms[n]
                n = 1
            else:
                n = get_next_number(n)
                terms += 1
        # Add term to dictionary
        if i not in dic_terms:
            dic_terms[i] = terms

        # check for new record
        if terms > largest_term_length:
            largest_term_length = terms
            term_with_greatest_length = i
            print(f'{term_with_greatest_length}: -> {largest_term_length} terms')
        i += 1
    return term_with_greatest_length


ans = method_1()
print(f'\nThe answer is: {ans}')
