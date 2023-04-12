class complex:
    def __init__(self,re , im):
        self.real = re
        self.imag = im
    
    def __add__(self,other):
        return self.real + other.real , self.imag + other.imag
    def display(self):
        print(self.real , "+" , self.imag,"j")
    
obj = complex(5,8)
obj2= complex(2,3)
obj.display()
obj2.display()
c,d=obj+obj2 
print(c,"+",d,"j")
