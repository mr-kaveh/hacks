#! /usr/bin/env python3.6
'''
    The first line contains the integer, , the total number of plants.
    The second line contains the  space separated heights of the plants.
    Sample Input:
                10
                161 182 161 154 176 170 167 171 170 174
    Expected Output:
                169.375
'''


def average(array) -> float:
    '''

    :param array: list of integers
    :return float: Average of set
    '''
    return sum(set(array)) / len(set(array))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
