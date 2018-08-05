
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