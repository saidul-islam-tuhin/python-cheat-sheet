
class Math:
    """" Parent class """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b


class ExtendMathClass(Math):
    """ Child class """

    def mul(self):
        return self.a * self.b


#obj = ExtendMathClass(6,2)

#print(obj.mul())
#print(obj.sum())



"""
super(): 
Example: If we want to use extra variable in ExtendMathClass.
"""

class ExtendMathClass1(Math):
    """ Child class """
    def __init__(self, a, b):
        super().__init__(a, b)
        self.sum_res = super().sum()

    def calculate(self):
       return self.a * self.sum_res


obj1 = ExtendMathClass1(6,2)

print(obj1.sum())
print(obj1.sum_res)
print(obj1.calculate())



""" Multiple Inheritance """