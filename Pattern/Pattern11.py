n = 5
for i in range(n-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")    
    for f in range(i+1):
        print("*",end=" ")  
    print()
for  i in range(n):
    for k in range(i+1):   # 2nd line space starting 
        print(" ",end=" ")  
    for j in range(n-i):
        print("*",end=" ")    # 1-5 printing 1st line
    for k in range(1,n-i):   # 1-4
        print("*",end=" ")  
    print()

#           * 
#         * * * 
#       * * * * * 
#     * * * * * * * 
#   * * * * * * * * * 
#     * * * * * * * 
#       * * * * * 
#         * * * 
#           * 
