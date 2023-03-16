
sub1 = int(input("Marks of subject 1  : \n"))
sub2 = int(input("Marks of subject 2 : \n "))
sub3 = int(input ("Marks of subject 3 : \n")) 

total = sub1 + sub2 + sub3
if( total >= 120 and sub1> 33 or sub2 > 33 or sub3 > 33 ):
 print ("Passs")

else : 
 print ("Failures")