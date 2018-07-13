
int('2') # OUTPUT: 2
int(3.4) # OUTPUT: 3

int('11', 2) # OUTPUT: 3
int('11', 8) # OUTPUT: 3
int('A', 16) # OUTPUT: 10

float(2) # OUTPUT: 2.0

str('1') # OUTPUT: '1'

chr(97) # OUTPUT: 'a'

ord('a') # OUTPUT: 97

list('abc') # OUTPUT: ['a', 'b', 'c']

tuple('abc') # OUTPUT: ('a', 'b', 'c')

dict((('name','tuhin'),('age',23))) # OUTPUT: {'age': 23, 'name': 'tuhin'}
dict([('name','tuhin'),('age',23)]) # OUTPUT: {'age': 23, 'name': 'tuhin'}

# remove duplicate value
set('abbc') # OUTPUT: {'a', 'b', 'c'}

bin(12) # OUTPUT: '0b1100'

oct(10) # OUTPUT: '0o12'

hex(12) # OUTPUT: '0xc'
