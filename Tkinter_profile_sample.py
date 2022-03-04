import tkinter
import tkinter.messagebox
import pymysql
from PIL import ImageTk, Image
from subprocess import call

t = tkinter.Tk()
t.title("profile")
t.geometry("500x500")

p = Image.open("F:\\F Drive Backup\Avodha Python\Tkinter_sample\\La_ferrrai.jpg")
p = p.resize((500, 500))
p = ImageTk.PhotoImage(p)
pic = tkinter.Label(t, image=p)
pic.place(x=0, y=0)

a = tkinter.Label(text="Profile creation", bg="Green", fg="white", font=("times new roman", 35, "bold"))
a.place(x=80, y=0)

b = tkinter.Label(text="First name", bg="blue", fg="white", font=("bradly hand itc", 25, "bold"))
b.place(x=55, y=100)
c = tkinter.Entry(width=30)
c.place(x=275, y=120)

d = tkinter.Label(text="Last name", bg="blue", fg="white", font=("bradly hand itc", 25, "bold"))
d.place(x=55, y=170)
e = tkinter.Entry(width=30)
e.place(x=275, y=190)


def abcd():
    name = c.get()
    last = e.get()
    if (name == "" or last == ""):
        tkinter.messagebox.showerror("Error", "Please complete fields")
    else:

        x = pymysql.connect(db='avodha', user='root', passwd='dhanesh', host='localhost')
        cur = x.cursor()
        cur.execute("insert into profile values('" + name + "','" + last + "')")
        x.commit()
        x.close()

        tkinter.messagebox.showinfo("Thank you", "Tnaks for Visting")
        t.destroy()
        call(["python", "next_page.py"])


f = tkinter.Button(text="submit", bg="red", fg="yellow", font=("bradly hand itc", 20, "bold"), command=abcd)
f.place(x=200, y=250)

t.mainloop()
