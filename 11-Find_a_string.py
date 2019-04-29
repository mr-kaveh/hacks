#!/usr/bin/env python3.6
'''
    With Regular Expression
    we can count substring
    repetitions in a string
'''

import re

def count_substring(string, sub_string):
     count = re.findall('(?='+sub_string+')',string)
     '(?='+sub_string+')'
     return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
