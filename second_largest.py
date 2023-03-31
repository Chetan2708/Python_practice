def scndlrge(arr):  
    lar = arr[0]
    scl= None
    for x in arr[1:]:
        if x> lar:
            scl = lar 
            lar = x
        elif x != lar:
            if scl ==None or scl<x:
                scl =x
    return scl
arr =[]
n = int(input())
for i in range(n):
    f = int(input())
    arr.append(f)
print(f"scndmax val is: {scndlrge(arr)}")