#!/usr/bin/env python3.6
'''
    Using Lists in Python
'''
if __name__ == '__main__':
    N = int(input())
    lst_output, cmd = [], []
    for i in range(N):
        cmd = input().split(' ')
        if cmd[0] == 'insert':
            lst_output.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'print':
            print(lst_output)
        elif cmd[0] == 'remove':
            lst_output.remove(int(cmd[1]))
        elif cmd[0] == 'append':
            lst_output.append(int(cmd[1]))
        elif cmd[0] == 'sort':
            lst_output.sort()
        elif cmd[0] == 'pop':
            lst_output.pop()
        elif cmd[0] == 'reverse':
            lst_output.reverse()
        else:
            print('invalid command')
