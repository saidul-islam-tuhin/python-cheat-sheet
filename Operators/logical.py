
True and True # OUTPUT: True
1==1 and 2==2 # OUTPUT: True

True and False # OUTPUT: False
1==1 and 1==2 # OUTPUT: False

False and False # OUTPUT: False
1==2 and 2==3 # OUTPUT: False


True or True # OUTPUT: True
1==1 or 2==2 # OUTPUT: True

True or False # OUTPUT: True
1==1 or 1==2 # OUTPUT: True

False or False # OUTPUT: False
1==2 or 2==3 # OUTPUT: False



False and True or True # OUTPUT: True
False and True and True # OUTPUT: False


not False  # OUTPUT: True
not True # OUTPUT: False

# SIMILAR: True and True
True and not False # OUTPUT: True