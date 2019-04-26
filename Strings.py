#!/usr/bin/env python3.6
'''
    Strings chapter
'''

website = 'http://www.python.org'
print(website[:11] + 'redhat' + website[-4:])

text = 'Hello %s'  # The %s parts of the format string are called conversion specifiers
print(text % 'Hossein')

text2 = 'Hello world, i am %s , it is %s'
values = ('Hossein', 'Friday')  # Tuple of values
print(text2 % values)

print('{1} is {0}'.format('my name', 'Hossein'))

from math import pi

print("{name} is approximately {value:.2f}.".format(value=pi, name="π"))

from math import e

print(f"Euler's constant is roughly {e}.")
print(e)


def calc():
    return 4 ** 4


print(f'calc function returns {calc()}')
'''
    The expressions that are extracted 
    from the string are evaluated in the
     context where the f-string appeared.
      This means the expression has full
       access to local and global variables.
        Any valid Python expression can be used,
         including function and method calls.
'''

print('{0} {1} {2}'.format('hello', 'my', 'friend'))

print('{0} {1} {name}'.format('hello', 'my', name='friend'))

print('the number is {num:f}'.format(num=48))
print('the number is {num:b}'.format(num=48))
print('the number is {num:o}'.format(num=48))
print('the number is {num:x}'.format(num=1600))
print('the number is {num:.2f}'.format(num=48))
print('the number is {num:.2f}'.format(num=pi))