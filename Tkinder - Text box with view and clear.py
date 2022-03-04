#TEXT BOX WITH VIEW AND CLEAR BUTTON

from tkinter import *
t=Tk()
t.geometry('300x240')

tx=Text(height=10,width=34)
tx.place(x=12,y=10)

words='Lorem Ipsum is simply dummy text of the printing and typesetting industry.'

def show():
	tx.insert(INSERT,words)

Button(text='View',command=show).place(x=15,y=200)

def clr():
	tx.delete('1.0',END)
	
Button(text='Clear',command=clr).place(x=55,y=200)

t.mainloop()


