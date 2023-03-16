
from tkinter import *
root = Tk()
root.title('Python')
root.geometry("500x500") #width x height 
root.minsize(300,200) #width , height
label = Label(root, text = "python hai yeh" ).grid(column = 1)
# # label.grid(row = 0 , column = 1) 
# # label1.grid(row = 0 , column = 1) 

def fun():
    list = []
    n = 2
    for i in range(1, 11):
        list.clear()
        x = n,"*",i,"=",n*i 
        str(x)
        list.append(x)
        label= Label(root,text=f"{list}").grid(row = i, column = 2)
mybutton= Button(root , text ="What is this ?",padx= 30, pady = 30,command = fun)
mybutton.grid(row = 1,column = 1)
root.iconbitmap("cal.ico")#add any icon
# # photo = PhotoImage(image = "cal.ico")
# # label2 = Label(image=photo).pack()
text = Entry(root,width ='40').grid(column = 1)
root.mainloop()