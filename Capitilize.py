#!/bin/python3


def solve(full_name: list) -> str:
    cap_full_name = [str(i).capitalize() for i in full_name]
    return ' '.join(cap_full_name)


if __name__ == '__main__':
    s = input('Please enter a name:')

    result = solve(s)

    print(result)
