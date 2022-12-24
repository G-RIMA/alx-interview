#!/usr/bin/python3
'''
Pascals triangle
'''


def pascal_triangle(n):
    '''returns a list of integers in pascals triangle form'''
    arr = []
    if n <= 0:
        return arr
    arr = [[1]]
    for i in range(1, n):
        tmp = [1]
        for j in range(len(arr[i - 1]) - 1):
            current = arr[i - 1]
            tmp.append(arr[i - 1][j] + arr[i - 1][j + 1])
            tmp.append(1)
            arr.append(tmp)
    return arr
