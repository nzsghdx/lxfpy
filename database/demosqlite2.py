import sqlite3

conn=sqlite3.connect('test.db')

cursor=conn.cursor()

cursor.execute('select * from user where id=?','1')

# 这里是查询的方法,返回通过上方sql语句执行之后得到的结果
values = cursor.fetchall()


print(values)

# 同样是关闭cursor和conn,因为是查询,所以不存在也没必要commit
cursor.close()
conn.close()
