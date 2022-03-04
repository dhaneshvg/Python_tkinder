# the pgm is not working
import pymysql

x = pymysql.connect(db="avodha", user="root", passwd="dhanesh", host="localhost")
cur = x.cursor()

print('-----------------Previewing Data set----------------')
cur.execute('select * from sample1')
# data=cur.fetchall()
data = cur.fetchone()
for i in data:
    print(i)

nm = input('Enter the name that you want to delete:')
cur.execute('select * from  sample1 where name=%s', nm)
da_nm = cur.fetchone()
print(da_nm)
x.commit()

cur.execute('delete * from sample1 where name=%s', nm)

cur.execute('select * from sample1')
nw_data = cur.fetchone()
for i in nw_data:
    print(i)

x.commit()
x.close()
