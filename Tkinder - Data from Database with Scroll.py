from tkinter import *
import pymysql

x=pymysql.connect(host='localhost',user='root',password='dhanesh',db='avodha')
cur = x.cursor()
t = Tk()
t.title('Home Database')
t.geometry('500x350')

sc = Scrollbar()
sc.pack(side=RIGHT, fill=Y)

tx = Text(height=15, width=58, yscrollcommand=sc.set)
tx.place(x=10, y=10)
sc.config(command=tx.yview)


def view():
    cur.execute('select * from sample1')
    v = cur.fetchall()
    vn = [','.join(map(str, xd)) for xd in v]  # new variable xd
    tx.insert(INSERT, ('Data sets are\n--------------\n'))
    for i in vn:
        tx.insert(INSERT, ('%s\n' % i))


Button(text='View Data', bg='indigo', fg='white', command=view).place(x=10, y=280)
