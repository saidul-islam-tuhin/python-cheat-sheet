"""
Method: capitalize, casefold, lower, title, upper, center, encode
"""


example = 'an example for capitalize()'
print(example) # OUTPUT: an example for capitalize()
example.capitalize() # OUTPUT: An example for capitalize()

casefold_exmp = 'Sample String'
print(casefold_exmp) # OUTPUT: Sample String
casefold_exmp.casefold() # OUTPUT: sample string

print(casefold_exmp) # OUTPUT: Sample String
casefold_exmp.lower() # OUTPUT: sample string


"""----------------- casefold() vs lower() ----------------"""
a = 'Fluß'
a.lower() # OUTPUT: fluß
a.casefold() # OUTPUT: fluss


name = 'md. sadiul islam tuhin'
print(name) # OUTPUT: md. sadiul islam tuhin

name.title() # OUTPUT: Md. Sadiul Islam Tuhin

name.upper() # OUTPUT: MD. SADIUL ISLAM TUHIN

center_exmp = 'An example of center()'
print(center_exmp) # OUTPUT: An example of center()
print(center_exmp.center(50)) # OUTPUT:               An example of center()              
print(center_exmp.center(50), '-') # OUTPUT: --------------An example of center()--------------


encode_exmp = '$encöde!'
print(encode_exmp) # OUTPUT: $encöde!

# Default encode to utf-8
encode_exmp.encode() # OUTPUT: '$enc\xc3\xb6de!'
      
encode_exmp.encode('ascii') # UnicodeEncodeError: 'ascii' codec can't encode character '\xf6' in position 4
encode_exmp.encode('ascii','ignore') # OUTPUT: b'$encde!'
encode_exmp.encode('ascii','replace') # OUTPUT: b'$enc?de!'
encode_exmp.encode('ascii','backslashreplace') # OUTPUT: b'$enc\\xf6de!'



test = 'a sample string.'

# string.index(substring, start, end)
# If sunstring found then return result otherwise raise ValueError
test.index('sam') # OUTPUT: 2
test.index('smple') # ValueError: substring not found

test.index('sam', 1) # OUTPUT: 2
test.index('sam', 3) # ValueError: substring not found

test.index('ple', 3, 8) # OUTPUT: 5
test.index('ple', 3, 5) # ValueError: substring not found


test.startswith('a') # OUTPUT: True
test.startswith('A') # OUTPUT: False

test.startswith('s', 2) # OUTPUT: True
test.startswith('s', 0) # OUTPUT: False

test.startswith('sam', 2, 7) # OUTPUT: True



test.endswith('string.') # OUTPUT: True
test.endswith('string') # OUTPUT: False

test.endswith('string.', 9) # OUTPUT: True
test.endswith('string.', 10) # OUTPUT: False

test.endswith('str',9,12) # OUTPUT: True
test.endswith('str',9,14) # OUTPUT: False




