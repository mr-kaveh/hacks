#!/usr/bin/env python3.6
'''
    Using List Comprehensions in Python
    to Solve a Math Problem
'''
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    S = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(S)
