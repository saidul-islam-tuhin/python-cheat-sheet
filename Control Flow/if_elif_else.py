
""" ******************************** if-block ********************************** """

# Single line code
# OUTPUT: 1 is smaller number
if 1<2 : print('1 is smaller number') 


# Use indent block
# OUTPUT: 1 is smaller number
if 1<2:
    print('1 is smaller number')


""" ******************************** if-else-block ********************************** """
a = 6
b = 5
res = 'Even' if a%2==0 else 'Odd' # OUTPUT: Even
res = 'Even' if b%2==0 else 'Odd' # OUTPUT: Odd


if a%2 == 0:
    res = 'Even'
else:
    res = 'Odd'
print(res) # OUTPUT: Even

""" ******************************** if-elif-else-block ********************************** """

