#!/usr/bin/env python3.6
'''
    Check Strict Superset Of A Set
'''
if __name__ == '__main__':
    A = set([int(x) for x in input().split()])
    T = int(input())
    for i in range(0, T):
        B = set([int(x) for x in input().split()])
        c = A.issuperset(B)
        if c:
            continue
        else:
            break

    print(c)
