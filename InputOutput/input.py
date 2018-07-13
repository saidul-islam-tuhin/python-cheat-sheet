"""
Default input() function take value as string data type format
If we need other data type format like integer then we use data type conversion 
For example: a = int(input())

"""

input()

input('Enter a number: ')

int(input('Enter a number: '))

# Enter two number with a single space: 3 5
# a = 3
# b = 5
a, b = input('Enter two number with a single space: ').split(' ')

# Input two value as integer format
x, y = map(int, input('Enter two number with a single space: ').split(' '))