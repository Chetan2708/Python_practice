n = 5 
for i in range (1 , 2*n+1):
    if i>n:
        Col = 2*n - i     #  i = 6 ,   column = 10 - 6 = 4 
    else :
        Col = i
    for j in range (1, Col+1):
        print("*",end=" ")
    print()

#   * 
#   * * 
#   * * * 
#   * * * * 
#   * * * * * 
#   * * * * 
#   * 
#   * * * 
#   * * 