class MathOperation:
    """ A basic example of math operation """

    # class attribute
    b = 2
    c = 3

    # initialized / instance attribute
    def __init__(self, a):
        self.a = a
        self.c = MathOperation.c+1

    def add_a_b(self):
        """ Return a+b """
        return self.a+MathOperation.b
    
    def mul_a_c(self):
        """ Return a*c """
        return self.a*self.c

res = MathOperation(6)

print('Third Number: ',res.c) # OUTPUT: 4
print('Third Number: ',MathOperation.c) # OUTPUT: 3
print("Summation:", res.add_a_b()) # OUTPUT: 8
print("Multiplication:", res.mul_a_c()) # OUTPUT: 24


print(res.__dict__) # OUTPUT: {'a': 6, 'c': 4}


# SIMILAR: res.c
print(getattr(res, 'c') # OUTPUT: 4

print(getattr(res,'d')) # AttributeError: 'MathOperation' object has no attribute 'd'
getattr(res,'d', 'default') # OUTPUT: default


print(hasattr(res,'a')) # OUTPUT: True
delattr(res, 'a') # SIMILAR: del(res.a)
print(hasattr(res,'a')) # OUTPUT: False


setattr(res, 'a', 2)
print(res.a) # OUTPUT: 2

setattr(res, 'e', 'None') # 'e' variable didn't declare in class so we set 'e' value by setattr()
print(res.e) # OUTPUT: None

