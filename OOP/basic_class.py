class MathOperation:
    """ A basic example of math operation """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        """ Return two number summation """
        return self.a+self.b
    
    def mul(self):
        """ Return two number multiplication """
        return self.a*self.b

res = MathOperation(3,4)

print("Summation:", res.add())
print("Multiplication:", res.mul())


""" -------------------- Define __init__ vs without define __init__  ------------------- """

class MathOperation:
    """ A basic example of math operation without  __init__ """
    def set_value(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.b
    
    def mul(self):
        return self.a*self.b

obj = MathOperation()
obj.set_value(3,4) 

print("Summation:", obj.add())
print("Multiplication:", obj.mul())

