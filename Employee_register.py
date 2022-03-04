from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
import pymysql

x = pymysql.connect(host='localhost', user='root', password='dhanesh', db='employeedb')
cur = x.cursor()

t = Tk()
t.title('Employee Database')
t.geometry('800x480')

p = Image.open("F:\\Assig\\Employee_register.png")
p = p.resize((800, 550))
p = ImageTk.PhotoImage(p)
pic = tkinter.Label(t, image=p)
pic.place(x=0, y=0)

Label(text='REGISTER', fg='red', bg='black', font=('times new roman', 24, 'bold')).place(x=10, y=10)

Label(text='Name:', fg='white', bg='black').place(x=10, y=60)
nm = Entry()
nm.place(x=65, y=65)

Label(text='Age:', fg='white', bg='black').place(x=10, y=95)
ag = Entry()
ag.place(x=65, y=97)


def abcd():
    n = nm.get()
    a = ag.get()
    cur.execute('insert into employee values(%s,%s)', (n, a))
    x.commit()
    tkinter.messagebox.showinfo("Thank you", "Register Success")
    t.destroy()


Button(text='Submit', bg='green', fg='white', command=abcd).place(x=210, y=75)

Label(text='UPDATE', fg='red', bg='black', font=('times new roman', 24, 'bold')).place(x=10, y=140)

Label(text='Enter name to update:', fg='white', bg='black').place(x=10, y=205)
un = Entry()
un.place(x=150, y=207)

Label(text='Enter new age:', fg='white', bg='black').place(x=10, y=240)
ul = Entry()
ul.place(x=150, y=245)


def upd():
    unw = un.get()
    ulw = ul.get()
    cur.execute('update employee set age=%s where name=%s', (ulw, unw))
    x.commit()
    tkinter.messagebox.showwarning("Thank you", "Details Updated")
    t.destroy()


Button(text='Apply', bg='cyan', fg='white', command=upd).place(x=205, y=280)

sc = Scrollbar()
sc.pack(side=RIGHT, fill=Y)

tx = Text(height=15, width=55, yscrollcommand=sc.set)
tx.place(x=300, y=10)
sc.config(command=tx.yview)


def view():
    cur.execute('select * from employee')
    v = cur.fetchall()
    vn = [','.join(map(str, xd)) for xd in v]  # new variable xd
    for i in vn:
        tx.insert(INSERT, ('%s\n' % i))


Button(text='View Data', bg='indigo', fg='white', command=view).place(x=500, y=280)

Label(text='DELETE', fg='red', bg='black', font=('times new roman', 24, 'bold')).place(x=10, y=310)

Label(text='Enter name to Delete:', fg='white', bg='black').place(x=10, y=365)
dn = Entry()
dn.place(x=150, y=365)

Label(text='Enter age:', fg='white', bg='black').place(x=10, y=400)
da = Entry()
da.place(x=150, y=400)


def dele():
    dna = dn.get()
    dag = da.get()
    cur.execute('delete from employee where name=%s && age =%s', (dna, dag))
    x.commit()
    tkinter.messagebox.showerror("Thank you", "Deleted")
    t.destroy()


Button(text='Delete', bg='red', fg='white', command=dele).place(x=205, y=430)

Label(text='EMPLOYEE \n \t DATABASE', bg='green', fg='white', font=('times new roman', 24, 'bold')).place(x=380, y=340)

t.mainloop()
