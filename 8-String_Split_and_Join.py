#! /usr/bin/env python3.6

'''
    You are given a string.
    Split the string on a ' ' (space)
    delimiter and join using a - hyphen.
'''


def split_and_join(line):
    splitted = line.split(' ')
    return '-'.join(splitted)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
