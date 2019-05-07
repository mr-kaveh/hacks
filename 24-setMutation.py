#!/usr/bin/env python3.6

'''
    Set Difference Operation
    .update() or |=
    Update the set by updateing elements from an iterable/another set.

    .intersection_update() or &=
    Update the set by keeping only the elements found in it and an iterable/another set.

    .difference_update() or -=
    Update the set by removing elements found in an iterable/another set.

    .symmetric_difference_update() or ^=
    Update the set by only keeping the elements found in either set, but not in both.
'''


def mutations(A: list, m: int) -> int:
    '''
    Creating Mutations
    :param A: Input Set which supposed to be mutated
    :param m: Number of the commands that should be executed
    :return: Mutated Set
    '''

    for i in range(m):
        cmd = input().split()
        set_input = [int(x) for x in input().split()]
        if cmd[0] == 'update':
            A.update(set_input)
        elif cmd[0] == 'intersection_update':
            A.intersection_update(set_input)
        elif cmd[0] == 'difference_update':
            A.difference_update(set_input)
        elif cmd[0] == 'symmetric_difference_update':
            A.symmetric_difference_update(set_input)

    return A


if __name__ == '__main__':
    n = int(input())
    s = set([int(i) for i in input().split()])
    m = int(input())
    print(sum(mutations(s, m)))
