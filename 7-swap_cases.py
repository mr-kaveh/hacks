#! /usr/bin/env python3.6
'''
    You are given a string and
    your task is to swap cases.
    In other words, convert all
    lowercase letters to uppercase
    letters and vice versa.
'''

def swap_case(s):
    output = []
    for i in range(len(s)):
        if s[i].isupper():
            output.insert(i , s[i].lower())
        else:
            output.insert(i, s[i].upper())
    return ''.join(output)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)