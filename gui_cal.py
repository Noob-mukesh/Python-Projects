# python

# Simple python GUI calculator.

from tkinter import *
from tkinter import messagebox
top=Tk()
top.geometry('10x40')
top['bg']="red"
uname = Label(top, text="This is a Simple GUI Calculator",bg='green' ,height=2).place(x=150, y=10)
firstnum=IntVar()
secondnum=IntVar()
def add():
    f=firstnum.get()
    s=secondnum.get()
    messagebox.showinfo('Sum is',(f+s))

num1= Label(top, text="First Number" ).place(x=50, y=150)
ent1= Entry(top,bg='white',textvariable=firstnum).place(x=300, y=150)



num2= Label(top, text="Second Number" ).place(x=50, y=250)
ent2= Entry(top,bg='white',textvariable=secondnum).place(x=300, y=250)



btn= Button(top, text="SUM",command=add).place(x=250, y=400)


top.mainloop()
