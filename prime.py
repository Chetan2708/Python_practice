def even_odd(x):
    flag= 0
    for i in range(2 , x):
        if x%i == 0:
            flag += 1
        return flag 
x = int(input("Enter the number: "))
if even_odd(x) == 0:
    print ("prime")
else: 
    print("Non Prime")
