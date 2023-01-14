#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    klist = []
    for k, v in a_dictionary.items():
        if v == value:
            klist.append(k)
    for i in klist:
        del a_dictionary[i]
    return a_dictionary
