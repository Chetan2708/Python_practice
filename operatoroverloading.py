class complex:
    def __init__(self,re,img):
        self.real =re
        self.imag = img
    def __add__(self,other):
        a,b = self.real + other.real , self.imag + other.imag
        return a , b
    def display(self):
        if self.imag<0:
            print(f"{self.real}{self.imag}i" )
        else:    
            print(f"{self.real}+{self.imag}i" )
a=complex(-2,-4)
b=complex(1,3)
a.display()
b.display()

c,d = a+b
if d<0:
    print(f"{c}{d}i" )
else:    
    print(f"{c}{d}i" )






