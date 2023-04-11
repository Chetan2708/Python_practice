class err(Exception):
    pass
try:
    def chec(n):
        if n>len(l):
            raise err
        for i in range(len(l)):
            if l[i]==n:
                return i
except err:
    print("ERROR")
l = [1,2,3,4,5,6,7,8]
n = int(input)
print(chec(n))