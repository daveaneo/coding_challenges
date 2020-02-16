# Project Euler Problem 19
# https://projecteuler.net/problem=19
# Feb 7 2020
# Description:
""" details """

# Python program to Find day of
# the week for a given date
'''How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?'''

import datetime
import calendar


def method_1():
    # need to rewrite all of this (some of this)

    start_date = datetime.datetime.strptime("1901-01-01", "%Y-%m-%d")
    end_data = datetime.datetime.strptime("2000-12-31", "%Y-%m-%d")
    interval = datetime.timedelta(days=7)
    date = start_date
    born = date.weekday()
    count = 0

    while calendar.day_name[date.weekday()] != "Sunday":
        date += datetime.timedelta(days=1)

    # check if first of the month is sunday
    while date < end_data:
        print(f'date: {date} and date.day: {date.day}')
        if date.day == 1:
            count += 1
            print(f'Found a match: {date}')
        date += interval


    #    return calendar.day_name[born]

    return count


ans = method_1()
print(f'\nMethod 1 -- The answer is: {ans}')
