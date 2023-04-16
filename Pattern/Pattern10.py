n = 5 
for i in range(n):
    for j in range(i+1):     #increasing space
        print(" ",end= " ")
    for k in range(1,n-i):     #1st line 1-4
        print("*",end= " ")
    for f in range(n-i):   #1st line 5-9
        print("*",end= " ")
    print()


#       * * * * * * * * * 
#         * * * * * * * 
#           * * * * * 
#             * * * 
#               * 