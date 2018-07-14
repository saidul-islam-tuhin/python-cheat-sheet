
""" ----------------------- Equal To ----------------------------- """
1 == 1 # OUTPUT: True
1 == 2 # OUTPUT: False
1 == '1' # OUTPUT: False
'same' == 'same' # OUTPUT: True

""" ----------------------- Less than ----------------------------- """
2 < 3 # OUTPUT: True
2 < 2 # OUTPUT: False
2 < 1 # OUTPUT: False

""" ----------------------- Less than equal ----------------------------- """
2 <= 3 # OUTPUT: True
2 <= 2 # OUTPUT: True
2 <= 1 # OUTPUT: False

""" ----------------------- Greater than ----------------------------- """
4 > 3 # OUTPUT: True
4 > 4 # OUTPUT: False
4 > 5 # OUTPUT: False

""" ----------------------- Greater than equal ----------------------------- """
4 >= 3 # OUTPUT: True
4 >= 4 # OUTPUT: True
4 >= 5 # OUTPUT: False

""" ----------------------- Not equal ----------------------------- """
1 != 1 # OUTPUT: False
1 != 2 # OUTPUT: True
1 != '1' # OUTPUT: True

""" ----------------------- is operator ----------------------------- """
1 is 1 # OUTPUT: True
1 is '1' # OUTPUT: False

""" ----------------------- is not operator ----------------------------- """
1 is not '1' # OUTPUT: True
1 is not 1 # OUTPUT: False

""" ----------------------- is vs equal(==) ----------------------------- """
# Output true because they are equal
[1,2] == [1,2] # OUTPUT: True

# Output false because their identity difference 
# Check id([1,2]); they are different
[1,2] is [1,2] # OUTPUT: False

""" ----------------------- in operator ----------------------------- """
'lo' in 'hello' # OUTPUT: True
'ol' in 'hello' # OUTPUT: False
2 in [1,2] # OUTPUT: True

""" ----------------------- in operator(case sensitive) ----------------------------- """
'hello' in 'hello' # OUTPUT: True
'Hello' in 'hello' # OUTPUT: False


""" ----------------------- not in operator ----------------------------- """
3 not in [1,2] # Output: True
'o' not in 'hello' # OUTPUT: False
