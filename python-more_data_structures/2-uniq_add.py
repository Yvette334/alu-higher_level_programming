#!/usr/bin/python3
def uniq_add(my_list=[]):
    nlist = set(my_list)
    n = 0

    for i in nlist:
        n += i

    return (n)
