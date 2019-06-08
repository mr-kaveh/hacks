#!/usr/bin/env python3.6


def minion_game(str_input) -> None:
    '''
    The Minion Game Implementation.
    :param str_input: Input String on which players , play the game
    :return: Nothing, The output will be printed
    '''

    n = len(str_input)

    stuart = 0  # consonents

    kevin = 0  # vowels

    for i in range(n):
        if str_input[i] in ('A', 'E', 'I', 'O', 'U'):
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print('Kevin', kevin)
    elif stuart > kevin:
        print('Stuart', stuart)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input('Please Input A String: ')
    minion_game(s.upper())
