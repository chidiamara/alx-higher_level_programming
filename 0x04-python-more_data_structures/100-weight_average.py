#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weight = 0
    n = 0
    for elem in my_list:
        n += elem[0] * elem[1]
        weight += elem[1]
    return n / weight
