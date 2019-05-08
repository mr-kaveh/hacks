#!/usr/bin/env python3.6
'''
    Finding Subset Of A Set
'''
if __name__ == '__main__':
    T = int(input())
    for i in range(0, T):
        a = int(input())
        A = set([int(x) for x in input().split()])
        b = int(input())
        B = set([int(x) for x in input().split()])
        print(A.issubset(B))
