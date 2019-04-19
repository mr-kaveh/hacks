#!/usr/bin/env python3.6
'''
    Finding The Second Maximum in List
'''
if __name__ == '__main__':
    arr = map(int, input().split())
    my_set = set(arr)
    desc_sorted_lst = list(sorted(my_set, reverse=True))
    print(desc_sorted_lst[1])
