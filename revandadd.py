def rev(n):
    rev = 0
    while n != 0:
        rev = rev*10 + n % 10
        n = n//10
    return rev
def check(n):
    if rev(n)== n:
        return True
    else:
        return False
def reverseandadd(n):
    rev_n = rev(n)
    add =rev_n+n
    print(n ,"+",rev_n,"=",add)
    while(check(add)==False):
        n = add
        rev_n = rev(n)
        add =rev_n+n
        print(n ,"+",rev_n,"=",add)
    else:
        print("Its possible")
n =int(input("Please enter a number: "))
reverseandadd(n)