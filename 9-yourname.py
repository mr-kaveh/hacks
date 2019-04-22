#! /usr/bin/env python3.6

'''
    The first line contains
    the first name, and
    the second line contains
    the last name.
'''


def print_full_name(a, b):
    output = 'Hello ', a, ' ', b, '! You just delved into python.'
    print(''.join(output))


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
