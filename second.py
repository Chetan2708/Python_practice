n =int(input())
for i in range(n):
    name = input()
    score = float(input())
    records=[]
    records.append([name,score])
 
second_largest=[]
for name,score in records:
    print("second largest score: " )
    records=sorted(set(records))
    if records[score]<max(records[score]):
        second_largest.append(name)
print(second_largest)
