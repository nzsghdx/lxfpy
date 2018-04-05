# 导入sqllite3,因为是内置的,可以直接这样导入
import sqlite3

# 创建连接并指定要连接的数据库文件
conn=sqlite3.connect('test.db')

# 创建游标,通过游标来操作数据库
cursor=conn.cursor()

# 创建数据表,sql语句貌似都是通用的
# cursor.execute('create table user(id varchar(20) primary key,name varchar(20))')

# 通过游标的execute方法进行执行的操作
cursor.execute('insert into user(id,name) values (\'1\',\'Dalao\')')

# 打印受影响的行数
print('insert line numberes:',cursor.rowcount)

# 操作结束后关闭游标cursor
cursor.close()
# 提交事务,恩,简单,没有创建事务啥的,默认的,有意思interesting!
conn.commit()
# 最后关闭conn
conn.close()
