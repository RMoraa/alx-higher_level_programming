#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """" a function that finds all multiples of 2 in a list. """

    new_list = [True for item in my_list]

    for i in range(len(my_list)):
        if my_list[i] % 2 != 0:
            new_list[i] = False

    return new_list
