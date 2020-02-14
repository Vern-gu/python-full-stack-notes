import pymysql


# Connection对象
# 用于建立与数据库的连接
# 创建对象：调用connect()方法
# conn=connect(参数列表)
# 参数host：连接的mysql主机，如果本机是'localhost'
# 参数port：连接的mysql主机的端口，默认是3306
# 参数db：数据库的名称
# 参数user：连接的用户名
# 参数password：连接的密码
# 参数charset：通信采用的编码方式，默认是'gb2312'，要求与数据库创建时指定的编码一致，否则中文会乱码

# Connection对象的方法  (默认是开启事务的)
# close()关闭连接
# commit()事务，所以需要提交才会生效
# rollback()事务，放弃之前的操作
# cursor()返回Cursor对象，用于执行sql语句并获得结果
# ===========================================================================================================

# Cursor对象
# 执行sql语句
# 创建对象：调用Connection对象的cursor()方法
# cursor1=conn.cursor()

# Cursor对象的方法
# close()关闭
# execute(operation [, parameters ])执行语句，返回受影响的行数
# fetchone()执行查询语句时，获取查询结果集的第一个行数据，返回一个元组
# next()执行查询语句时，获取当前行的下一行
# fetchall()执行查询时，获取结果集的所有行，一行构成一个元组，再将这些元组装入一个元组返回
# scroll(value[,mode])将行指针移动到某个位置
#   mode表示移动的方式
#   mode的默认值为relative，表示基于当前行移动到value，value为正则向下移动，value为负则向上移动
#   mode的值为absolute，表示基于第一条数据的位置，第一条数据的位置为0

# Cursor对象的属性
# rowcount只读属性，表示最近一次execute()执行后受影响的行数
# connection获得当前连接对象
# ===========================================================================================================

# sql语句参数化，将一些关键的参数放到列表中在传入sql语句中：
# sql = 'insert into table(name) value(%s)'
# cursol.execute(sql, [name])

class Mysql(object):
    def __init__(self, users, password, host='localhost', port=3306, database='mydata', charset='utf8'):
        try:
            self.conn = pymysql.connect(
                host=host,
                port=port,
                user=users,
                passwd=password,
                db=database,
                charset=charset
            )
        except Exception as e:
            print(e)
        else:
            print('连接成功')
            self.cur = self.conn.cursor()

    @staticmethod
    def input():
        sql = input('input sql command...')
        return sql

    def create_table(self):
        # sql = 'create table testtb(id int, name varchar(10),age int)'
        sql = self.input()
        res = self.cur.execute(sql)
        print(res)

    def close(self):
        self.cur.close()
        self.conn.close()

    def add(self):  # 增
        sql = 'insert into pytest value(null,"pear",18),(null,"peach",16),(null,"pineapple",24)'
        res = self.cur.execute(sql)
        if res:
            self.conn.commit()
        else:
            self.conn.rollback()
        print(res)

    def rem(self):  # 删
        sql = 'delete from pytest where id=1'
        res = self.cur.execute(sql)
        if res:
            self.conn.commit()
        else:
            self.conn.rollback()
        print(res)

    def mod(self):  # 改
        sql = 'update pytest set name="Tom Ding" where id=2'
        res = self.cur.execute(sql)
        if res:
            self.conn.commit()
        else:
            self.conn.rollback()
        print(res)

    def show(self):  # 查
        num = int(input('num'))
        sql = 'select * from pytest where id="%s"'
        self.cur.execute(sql,[num])  # sql语句参数化
        res = self.cur.fetchall()
        for i in res:
            print(i)


if __name__ == "__main__":
    mysql = Mysql(users='root', password='1110')
    # mysql.create_table()
    # mysql.add()
    # mysql.mod()
    # mysql.rem()
    mysql.show()
    mysql.close()
