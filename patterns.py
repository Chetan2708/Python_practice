
n = 5
""""
square pattern
"""
# for i in range(1,n):
#     for j in range(1,n):
#         print("*",end=" ")
#     print(" ")
"""
left pattern
"""

# for i  in range(1,n):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print(" ")

"""
decrease left """
    
# for i in range(1,n):
#     for j in range(1,n-i):
#         print("*",end=" ")
#     print(" \n")
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i , end=" ")
#     print(" ")

"""Mixing left and decreasing left pattern"""
# for i in range(1,n):
#     for j in range(1,i+1):
#         print("*" , end=" ")
#     print(" ")

# for i in range(1,n):
#     for j in range(1,n-i+1):
#         print("*" , end=" ")
#     print(" ")
"""
Reverse loop"""
# for i in range(n,0,-1):
#     for j in range(i+1,1,-1):
#         print("*" , end=" ") 
#     print(" ")