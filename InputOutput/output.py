
print(5) # OUTPUT: 5

print('The result is: ', 4**2) # OUTPUT: The result is: 16

# we don't need convert int to string and default space add around variable
print('My name:','tuhin','and Age:',24) # OUTPUT: My name: tuhin and Age: 24

# we must be convert int to string and default space not added around variable
print('My name:'+' tuhin' +' and Age:' +str(24)) # OUTPUT: My name: tuhin and Age: 24


print('My name: %s and Age: %d'%('tuhin',24)) # OUTPUT: My name: tuhin and Age: 24

print('Total amount: %f and %.2f'%(23.123455,23.123455)) # OUTPUT: Total amount: 23.123455 and 23.12


li = ['I', 'am', 'a', 'Python', 'Developer']
print(' '.join(li)) # OUTPUT: I am a Python Developer



