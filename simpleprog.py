# for i in range(4):
#     for j in range(4-(i+1)):
#         print("*",end="")
#     # for k in range(i+1):
#     #     print("*",end="")
#     print()

space=4-1
for i in range(4):
    space-=1
    print(" "*space+'*'*i+1)