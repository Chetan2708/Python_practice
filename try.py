class err(Exception):
    pass
try:

    num = int(input("Enter an even  number: "))

    if  num % 2 != 0:
        raise err
except err :
    print("Invalid")

else:
    reciprocal = 1/num 
    print(reciprocal)
finally:
    print("This is obv. ")
    