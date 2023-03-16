from tkinter import *

root = Tk()


def show(n):
    global opr
    opr = opr+n
    val.set(opr)


def cal():
    global opr
    exp = eval(opr)
    val.set(exp)
    opr = str(exp)


def allClear():
    global opr
    val.set("")
    opr = ""


val = StringVar()
opr = ""
txt = Entry(root, textvariable=val).grid(row=0, column=0, columnspan=6)

btn1 = Button(root, text="AC", width=4,
              command=lambda: allClear()).grid(row=1, column=1)
btn1 = Button(root, text="<-", width=4).grid(row=1, column=2)
btn1 = Button(root, text="%", width=4,
              command=lambda: show("%")).grid(row=1, column=3)
btn1 = Button(root, text="÷", width=4,
              command=lambda: show("/")).grid(row=1, column=4)

btn1 = Button(root, text="7", width=4,
              command=lambda: show('7')).grid(row=2, column=1)
btn1 = Button(root, text="8", width=4,
              command=lambda: show("8")).grid(row=2, column=2)
btn1 = Button(root, text="9", width=4,
              command=lambda: show("9")).grid(row=2, column=3)
btn1 = Button(root, text="x", width=4,
              command=lambda: show("*")).grid(row=2, column=4)

btn1 = Button(root, text="4", width=4,
              command=lambda: show("4")).grid(row=3, column=1)
btn1 = Button(root, text="5", width=4,
              command=lambda: show("5")).grid(row=3, column=2)
btn1 = Button(root, text="6", width=4,
              command=lambda: show("6")).grid(row=3, column=3)
btn1 = Button(root, text="-", width=4,
              command=lambda: show("-")).grid(row=3, column=4)

btn1 = Button(root, text="1", width=4,
              command=lambda: show("1")).grid(row=4, column=1)
btn1 = Button(root, text="2", width=4,
              command=lambda: show("2")).grid(row=4, column=2)
btn1 = Button(root, text="3", width=4,
              command=lambda: show("3")).grid(row=4, column=3)
btn1 = Button(root, text="+", width=4,
              command=lambda: show("+")).grid(row=4, column=4)

btn1 = Button(root, text="0", width=12, command=lambda: show("0")
              ).grid(row=5, column=1, columnspan=2)
# btn1 = Button(root, text = ".").grid(row = 5, column = 2)
btn1 = Button(root, text=".", width=4,
              command=lambda: show(".")).grid(row=5, column=3)
btn1 = Button(root, text="=", width=4,
              command=lambda: cal()).grid(row=5, column=4)

root.mainloop()
