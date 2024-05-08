#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""


def pascal_triangle(n):
    """returns a list of lists of nums
    repr the pascal triangle"""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        triangle.append([])
        triangle[i].append(1)

        for j in range(1, i):
            x = triangle[i-1][j-1]
            y = triangle[i-1][j]
            triangle[i].append(x+y)

        if(n != 0 and i != 0):
            triangle[i].append(1)

    return triangle
