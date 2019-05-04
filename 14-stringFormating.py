#!/usr/bin/env python3.6
'''
    Outputs
        Decimal
        Octal
        Hexadecimal (capitalized)
        Binary
'''


def print_formatted(number):
    width = len(bin(n)) - 2
    for _ in (i + 1 for i in range(number)):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(_, width=width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
