n = 5 
for i in range (n):
    for j in range(n-i):
        print(" ",end =" ")
    for k in range(i+1):
        print("*",end =" ")
    for f in range(1,i+1):
         print("*",end =" ")
    print()

#                * 
#              * * * 
#            * * * * * 
#          * * * * * * * 
#        * * * * * * * * * 