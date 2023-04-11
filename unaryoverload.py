class complex:
    def __init__(self,re):
        self.real = re
    def __neg__(self):
        print(-self.real)
b=complex(1)
-b
