import pymysql

x=pymysql.connect(host='localhost',user='root',password='dhanesh',db='avodha')

cur=x.cursor()
cur.execute('select * from sample1')
mn=cur.fetchall()
for i in mn: 
	print(i)

x.close()
