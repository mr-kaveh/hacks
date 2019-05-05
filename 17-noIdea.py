#!/usr/bin/env python3.6
'''
No Idea!
Sample Input:
3 2
1 5 3
3 1
5 7
'''
if __name__ == '__main__':
    # Reading 2 inetegers from input
    n, m = map(int, input().split())

    # Best Practice to read a
    # list of integers From input
    arr = input().split()
    A = set(input().split())
    B = set(input().split())
    print(sum([(i in A) - (i in B) for i in arr]))
