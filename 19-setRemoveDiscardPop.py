#!/usr/bin/env python3.6
'''
    Sets Remove
'''
if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    m = int(input())
    lst_output, cmd = [], []
    for i in range(m):
        cmd = input().split()
        if cmd[0] == 'pop':
            s.pop()
        elif cmd[0] == 'remove':
            s.remove(int(cmd[1]))
        elif cmd[0] == 'discard':
            s.discard(int(cmd[1]))
        else:
            print('invalid command')

    print(sum(s))
