#!/usr/bin/python3
"""Defines function primeFactorization"""


def primeFactorization(x):
    """Returns prime factorial elements of x"""
    div = 2
    array = list()
    while (div <= x):
        if x % div == 0:
            array.append(div)
            x /= div
        else:
            div += 1

    return array


def minOperations(n):
    """Calc the fewest num of operations needed
        to result in exactly n H characters in file"""
    min = 0
    factors = [x for x in primeFactorization(n)]
    occurences = {item: factors.count(item) for item in factors}
    for k, v in occurences.items():
        min += k * v
    return min
