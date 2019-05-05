#!/usr/bin/env python3.6
'''
    Symmetric Difference
'''
if __name__ == '__main__':
    m = int(input())
    set1 = set(map(int, input().split()))

    n = int(input())
    set2 = set(map(int, input().split()))

    set3 = sorted(set1.symmetric_difference(set2))
    for i in set3:
        print(int(i))
