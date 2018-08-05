example = 'an example for capitalize()'
print(example) # OUTPUT: an example for capitalize()
print(example.capitalize()) # OUTPUT: An example for capitalize()

casefold_exmp = 'Sample String'
print(casefold_exmp) # OUTPUT: Sample String
print(casefold_exmp.casefold()) # OUTPUT: sample string

print(casefold_exmp) # OUTPUT: Sample String
print(casefold_exmp.lower()) # OUTPUT: sample string

"""----------------- casefold() vs lower() ----------------"""
a = 'Fluß'
print(a.lower()) # OUTPUT: fluß
print(a.casefold()) # OUTPUT: fluss

name = 'md. sadiul islam tuhin'
print(name) # OUTPUT: md. sadiul islam tuhin
print(name.title()) # OUTPUT: Md. Sadiul Islam Tuhin


print(name) # OUTPUT: md. sadiul islam tuhin
print(name.upper()) # OUTPUT: MD. SADIUL ISLAM TUHIN

center_exmp = 'An example of center()'
print(center_exmp) # OUTPUT: An example of center()
print(center_exmp.center(50)) # OUTPUT:               An example of center()              
print(center_exmp.center(50), '-') # OUTPUT: --------------An example of center()--------------


encode_exmp = '$encöde!'
print(encode_exmp) # OUTPUT: $encöde!

# Default encode to utf-8
print(encode_exmp.encode()) # OUTPUT: '$enc\xc3\xb6de!'
      
print(encode_exmp.encode('ascii')) # UnicodeEncodeError: 'ascii' codec can't encode character '\xf6' in position 4
print(encode_exmp.encode('ascii','ignore')) # OUTPUT: b'$encde!'
print(encode_exmp.encode('ascii','replace')) # OUTPUT: b'$enc?de!'
print(encode_exmp.encode('ascii','backslashreplace')) # OUTPUT: b'$enc\\xf6de!'
