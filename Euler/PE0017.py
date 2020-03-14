# Project Euler Problem 17
# https://projecteuler.net/problem=17
# Feb 7 2020
# Description:
"""If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? """

import time

dic_num_words = {1: "one",
                 2: "two",
                 3: "three",
                 4: "four",
                 5: "five",
                 6: "six",
                 7: "seven",
                 8: "eight",
                 9: "nine",
                 10: "ten",
                 11: "eleven",
                 12: "twelve",
                 13: "thirteen",
                 14: "fourteen",
                 15: "fifteen",
                 16: "sixteen",
                 17: "seventeen",
                 18: "eighteen",
                 19: "nineteen"
                 }

dic_tens_dic = {2: "twenty",
                3: "thirty",
                4: "forty",
                5: "fifty",
                6: "sixty",
                7: "seventy",
                8: "eighty",
                9: "ninety"
                }

def int_num_to_str_word(num):
    num_word = [] # add in opposite order, then reverse
    # ones
    if num == 1000:
        return "one thousand"
    while num > 0:
        column = 1
        and_flag = 1
        first_two_digits = num % 100
        third_digit = (num%1000)//100
        if first_two_digits == 0:
            and_flag = 0
        elif 0 < first_two_digits < 20:
            num_word.append(dic_num_words[first_two_digits])
        else:
            if first_two_digits % 10 > 0:
                num_word.append("-" + dic_num_words[first_two_digits % 10])
            num_word.append(dic_tens_dic[first_two_digits//10])
        if third_digit >0:
            if and_flag:
                num_word.append("and")
            num_word.append("hundred")
            num_word.append(dic_num_words[third_digit])
        num_word =  " ".join(num_word[::-1])
        return num_word.replace(" -", "-") # broken up into two parts for clarity

def method_1():
    # generate words
    total = 0
    for i in range(1, 1001):
        # convert to word
        # count length of word
        # add to total
        word = int_num_to_str_word(i)
        total += sum([1 for i in word if i.isalpha()])
    return total

def method_2():
    one_chunk = "".join([int_num_to_str_word(i) for i in range(1,1001)])
    one_chunk = one_chunk.replace('-', '')
    one_chunk = one_chunk.replace(' ', '')
    return len(one_chunk)


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

ans = method_1()
print(f'\nMethod 1 -- The answer is: {ans}')

ans = method_2()
print(f'\nMethod 2 -- The answer is: {ans}')


ratio, fastest_time, fastest_method = speed_race()
print(f'The fastest method was #{fastest_method}. It was {ratio}x faster!')

