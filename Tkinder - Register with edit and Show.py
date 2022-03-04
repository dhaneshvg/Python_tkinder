from tkinter import *
import pymysql

x=pymysql.connect(host='localhost',user='root',password='dhanesh',db='avodha')
cur=x.cursor()

t=Tk()
t.title('Home Database')
t.geometry('800x350')

Label(text='Register',fg='red',bg='black',font=('times new roman',24,'bold')).place(x=10,y=1)

Label(text='Name:').place(x=10,y=50)
nm=Entry()
nm.place(x=55,y=52)

Label(text='Age:').place(x=10,y=75)
ag=Entry()
ag.place(x=55,y=77)

def abcd():
	n=nm.get()
	a=ag.get()
	cur.execute('insert into sample1 values(%s,%s)',(n,a))
	x.commit()
	

Button(text='Submit',bg='Blue',fg='white',command=abcd).place(x=200,y=60)

Label(text='UPDATE',fg='red',bg='black',font=('times new roman',24,'bold')).place(x=10,y=125)

Label(text='Enter name to update:',fg='white',bg='black').place(x=10,y=185)
un=Entry()
un.place(x=150,y=187)

Label(text='Enter new age:',fg='white',bg='black').place(x=10,y=220)
ul=Entry()
ul.place(x=150,y=220)

def upd():
	unw=un.get()
	ulw=ul.get()
	cur.execute('update sample1 set age=%s where name=%s',(ulw,unw))
	x.commit()
	

Button(text='Apply',bg='Blue',fg='white',command=upd).place(x=205,y=260)

sc=Scrollbar()
sc.pack(side=RIGHT,fill=Y)

tx=Text(height=15,width=60,yscrollcommand=sc.set)
tx.place(x=300,y=10)
sc.config(command=tx.yview)

def view():
        cur.execute('select * from sample1')
        v=cur.fetchall()
        vn=[','.join(map(str,xd))for xd in v]       #new variable xd    
        for i in vn:
                tx.insert(INSERT,('%s\n'%i))
                
Button(text='View Data',bg='indigo',fg='white',command=view).place(x=500,y=280)
    
 	
t.mainloop()
	
