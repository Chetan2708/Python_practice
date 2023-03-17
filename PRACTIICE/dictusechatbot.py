d={"hi":"hello" ,"how are you" :"I am fine how are you","Hows life":"dude common , its boring u know that"}

while True:
       con=input("chat with bot")
       if con not in d.keys():
           print("wrong input")
       print("Bot replied -> ",d[con])