import keyword
print(keyword.kwlist)
# n= int(input("enter the value for for loop"))
# for i in range(0,n,4):
#     print(i)
num = int(input())
# n= int(input("enter the value for for loop"))
# for i in range(1,n+1):
#     print(num ,"X" , i ,"=", num * i  )

for i in range(0,num):
      if i % 5 == 0 and i % 7!=0:
            print(i,end=" ")