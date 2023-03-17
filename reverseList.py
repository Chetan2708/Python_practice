def rev(l,start , end):
    while start<end:
        l[start], l[end]=l[end],l[start]
        start+=1
        end-=1

def rever(l,k):
    k=k%len(l)
    rev(l,0,k-1)
    rev(l,k,(len(l)-1))
    rev(l,0,len(l)-1)
l=[1,2,3,4,5]
k=int(input())
rever(l,k)
print(l)
