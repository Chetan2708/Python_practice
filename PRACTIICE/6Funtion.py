# def fact(n):
#    fact=1
#    for i in range(1,n+1):
#         if n >=10 :
#             break
#         else:
#             fact=fact*i
#    return fact
    
# n = int(input("Enterthe number:"))
# print(fact(n))
# pt = 3.14
# def add():
#     a = 10   # local variable 
#     b = 20 
#     c = 30
#     pi = 2
#     d =a+b+c
#     print(pi)
#     print(f"The addition is:{d} ")
  
# ADD 
# add()

# def add1(x, y):
#     print(" adding ",x+y)

# add1(10, 10)



# def func(x):
#     for i in range(1 , x):
#         if i%5==0 and x >0:
#             print(" multiple of 5")
#         elif i%5!=0 and x>0:
#             # print( " not a multiple of 5")
#             pass
# x = int(input("Please   enter a number: "))
# func(x)
def powe(x,y):
    result = 1
    for i in range(y+1):
        result=result*x
    print(result)    

x = int(input("Please enter a number: "))
y = int(input("Please enter a number: "))   
powe(x, y)

