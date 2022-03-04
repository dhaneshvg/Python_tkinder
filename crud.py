import pymysql

x=pymysql.connect(db="avodha",user="root",passwd="dhanesh",host="localhost")
cur=x.cursor()

print('-----------------Previewing Data set----------------')
cur.execute('select * from sample1')
#data=cur.fetchall()
data=cur.fetchone()
for i in data:
    print(i)

nm=input('Enter the name that you are searching for:')
cur.execute('select * from  sample1 where name=%s',nm)
da_nm=cur.fetchone()
print(da_nm)

pl=input('Enter updated location: ')
cur.execute('update sample1 set place=%s where name=%s',(pl,nm))

cur.execute('select * from  sample1 where name=%s',nm)
da_nm=cur.fetchone()
print(da_nm)

x.commit()
x.close()
