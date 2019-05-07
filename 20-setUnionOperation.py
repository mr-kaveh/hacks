#!/usr/bin/env python3.6
'''
    Set Union Operation
'''

if __name__ == '__main__':
    n = int(input())
    set1 = set(map(int, input().split()))
    m = int(input())
    set2 = set(map(int, input().split()))
    print(len(set1.union(set2)))
