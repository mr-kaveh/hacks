#!/usr/bin/env python3.6
'''
    str.isalnum()
    str.isalpha()
    str.isdigit()
    str.islower()
    str.isupper()
'''

if __name__ == '__main__':
    s = input()
    alphanum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for i in range(len(s)):
        if s[i].isalnum():
            alphanum = True
        if s[i].isalpha():
            alpha = True
        if s[i].isdigit():
            digit = True
        if s[i].islower():
            lower = True
        if s[i].isupper():
            upper = True
    print(alphanum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)
