
# 导入之前首先安装mysql驱动:pip install mysql-connector-python --allow-external mysql-connector-python

import mysql.connector
# 事先设置好数据库
conn=mysql.connector.connect(user='test',password='1234',database='test')

# 同样是通过游标来操作数据库,应该是python提供的接口啥的
cursor=conn.cursor()

# 执行在指定数据库中创建表的语句
# cursor.execute('create table userdemo(id varchar(20) primary key,name varchar(20))')

# 在新建的表中插入数据
# cursor.execute('insert into userdemo(id,name) values (%s,%s)',['6','Dalao6'])

# 打印受影响的行数
print('insert line numbers:',cursor.rowcount)

# 提交事务,本来在搞sqlite3的时候以为那个事务是自带的呢,原来是python3封装好了的吗,不用自己写事务了?
conn.commit()

# 我说明明插入进去了为什么查询不到,原来我是从user表里查询的..
cursor.execute('select * from userdemo where id=%s',['5'])

values=cursor.fetchall()

print(values)

# 最后关闭游标cursor和连接conn
cursor.close()
conn.close()
