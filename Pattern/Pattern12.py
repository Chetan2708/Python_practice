n = 10 
for i in range(n):
    for j in range(n):
        if i == 0 or  j == 0 or i == n-1:
            print("*",end= " ")

    print()