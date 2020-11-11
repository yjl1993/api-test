# coding:utf-8
import MySQLdb.cursors
import json, datetime


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


class OperationMysql:
    def __init__(self):
        self.conn = MySQLdb.connect(
            host='172.16.10.230',
            user='test',
            passwd='2008alpha',
            db='ceshi',
            port=3306,
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor
        )
        self.cur = self.conn.cursor()

    # 查询一条数据
    def search_one(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        result = json.dumps(result)
        return result

    def select(self, value=None):
        sql = "select * from u_user where %s" % (value)
        self.cur.execute(sql)  # 执行查询语句
        # data = self.cur.fetchall()  # 返回结果（元组）
        data = self.cur.fetchone()
        data = json.dumps(data, cls=DateEncoder)
        print(data)
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    op_mysql = OperationMysql()
    res = op_mysql.select(value='id = "921972"')
    print(res)
