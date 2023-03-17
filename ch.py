lst=[[2,3,4],[4,5,6]]
lst2=[2,3]
sum=0
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j] in lst2:
            lst[i][j]=0 
        sum +=lst[i][j]
print(lst)
print(sum)