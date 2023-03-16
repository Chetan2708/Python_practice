def fun(x):
       newx_x=x[::-1]  #reverse string
       if x==newx_x:
        return True
       else:
        return False

x = input()
print(fun(x))