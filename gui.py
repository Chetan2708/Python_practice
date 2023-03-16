from tkinter import *
root = Tk()
root.geometry("500x500")
name = StringVar()
passw= StringVar()
label = Label(root, text = "Username").pack()
entry = Entry(root , textvariable = name, width = 20).pack()
label=Label(root, text = "Password").pack()
entry = Entry(root, width= 20 , textvariable = passw).pack()
def work():
    if name.get() == "chetan" and passw.get()=="wao":
         label = Label(root, text = "Success").pack()
    else:
        label = Label(root, text= "error").pack()
    name.set("")
    passw.set("")
mybutton = Button(root , padx = 10 , pady=10, text = "Submit" , command = lambda:work()).pack()
root.mainloop()