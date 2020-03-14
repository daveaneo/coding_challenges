# Project Euler Problem 31
# https://projecteuler.net/problem=31
# Feb 19 2020
# Description:
from timelines import time_check


"""  How many different ways can £2 be made using any number of coins?"""

# Coin Types: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

import copy
import itertools
import numpy as np

MAX_VALUE = 200
coin_types = {1, 2, 5, 10, 20, 50, 100, 200}
dic_coin_amount_to_paths = {}
solution_set = set()

def return_num_paths_given_number(value): # pass in coin_type???
    list_of_lists = []
    if value == 0:
        return [0]
    elif value < 0:
        return []
    elif value in dic_coin_amount_to_paths:
        return dic_coin_amount_to_paths[value]
    for coin in coin_types:
        if coin > value:
            continue
        elif value - coin == 0: # evenly divide
            temp_val = [] # check for empty set?
        elif value - coin in dic_coin_amount_to_paths:
            temp_val = dic_coin_amount_to_paths[value - coin]
        else:
            temp_val = return_num_paths_given_number(value - coin) # return array
            if not temp_val: # if there is NOT a working path
                dic_coin_amount_to_paths[value - coin] = []
            elif temp_val == [0]:
                print(f'    Something was gone awry!')

        #print(f'  value: {value},  temp_val : {temp_val}')

        # append coin to the list of values
        if not temp_val:
            temp_val = [[coin]]
        elif type(temp_val[0]) == int:  # if not a list of lists --- doesn't happen ever?
            #print(f'  before: {temp_val}')
            temp_val += [coin]
            #print(f'  after: {temp_val}')
        else:
            for i, list_of_coins in enumerate(temp_val):
                #print(f'before: {temp_val[i]}')
                if type(list_of_coins) is int:
                    temp_val[i] = [list_of_coins]
                temp_val[i].append(coin)
                #print(f'after: {temp_val[i]}')

        #print(f'temp_val: {temp_val}')
        for listy in temp_val:
            listy.sort()
            #print(f'  listy: {listy}')
            if listy not in list_of_lists:
                list_of_lists.append(listy)

    #        list_of_lists.append(temp_val)
    dic_coin_amount_to_paths[value] = copy.deepcopy(list_of_lists)  # ToDo avoid too many embedded lists
    #print(f'\nValue of {value} has produced this list: {list_of_lists}')
    #print(f'dictionary: {dic_coin_amount_to_paths}')
    print(f'Computed dictionary for {value}')

    return list_of_lists

# so long and difficult...
def method_1():
    answer = len(return_num_paths_given_number(200))
    print(f'{i} --> {answer}')
    return answer


def method_2():
    change_of_two_hundred = set()
    full_domain = [range(1, MAX_VALUE//i + 1) for i in coin_types]
    print(full_domain)
    for var_list in itertools.product(*full_domain):

        # may need to add one somewhere
        total_change = sum([var_list[i]*coin_types[i] for i in range(8)])
        if total_change == MAX_VALUE:
            change_of_two_hundred.add(var_list)
            print(f'\n{var_list} added')
            print(f'{len(change_of_two_hundred)} possibilities found.')
    return len(change_of_two_hundred)

# too big
def method_3():
    change_of_two_hundred = set()
    MAX_VALUE = 16
    full_domain = [range(0, MAX_VALUE//i + 1) for i in coin_types[0:2]]
    print(full_domain)
    np_coin_types = np.array(coin_types)
    set_of_ans = set([num_list for num_list in list(itertools.product(*full_domain)) if np.dot(num_list, coin_types[0:2])==MAX_VALUE])
    #    print(np_coin_types*coin_types)

    return len(set_of_ans)

def method_4():
    coin_table = [1]*(MAX_VALUE+1)
    # coin_table[0] = 1
    for coin in coin_types - {1}:
        for i in range(coin, MAX_VALUE+1):
            coin_table[i] += coin_table[i-coin] # add one for every divergence
    return coin_table[MAX_VALUE]

# ans = method_1()
# print(f'method_1 returns: {ans}')

# ans = method_2()
# print(f'method_2 returns: {ans}')

# time_check()

# ans = method_3()
# print(f'method_3 returns: {ans}')

time_check()
ans = method_4()
print(f'method_4 returns: {ans}')
time_check()

# Correct answer : 73682
# 71898 (MAV_VAL -1)