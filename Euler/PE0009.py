# Project Euler Problem 9
# https://projecteuler.net/problem=9
# Feb 5 2020
# Description:
'''Meet the following conditions:
pythagorean tripliet: a**2 +b**2 = c**2;
sums to 1000: a + b +c = 1000
then, find the product'''

MAX_UPPER = 1000

def method_1():
    pass
    # create a list of empty answers
    answers = list()
    for a in range(1, MAX_UPPER -1):
        for b in range(1,MAX_UPPER - a): # this might be off by 1 (subtraction)
            c = MAX_UPPER - a - b
            if a**2 + b**2 == c**2:
                # These may be out of order
                to_add = [a, b, c]
                to_add.sort()
                answers.append((tuple(to_add)))
    answers = list(set([i for i in answers]))
    if (len(answers)>1):
        print("Multiple answers.")

    final_answers = []
    for answer in answers:
        final_answers.append(answer[0] * answer[1] * answer[2])
        print(f'{answer} --> {final_answers}')
    return final_answers

# returns a list of answer
ans = method_1()

print(f'Answer: {ans}')