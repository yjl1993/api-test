# coding:utf-8
from util.operation_excel import OperationExcel
import data_config, time
from util.operation_json import OperetionJson
from util.connect_db import OperationMysql


class GetData:
    def __init__(self):
        self.opera_excel = OperationExcel()

    def get_case_lines(self):
        '''	去获取excel行数,就是我们的case个数	'''
        return self.opera_excel.get_lines()

    def get_is_run(self, row):
        '''获取是否执行'''
        flag = None
        col = int(data_config.get_run())
        run_model = self.opera_excel.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    def is_header(self, row):
        '''是否携带header'''
        col = int(data_config.get_header())
        header = self.opera_excel.get_cell_value(row, col)
        if header != '':
            return header
        else:
            return None

    def get_request_method(self, row):
        '''获取请求方式'''
        col = int(data_config.get_run_way())
        request_method = self.opera_excel.get_cell_value(row, col)
        return request_method

    def get_request_url(self, row):
        '''获取url'''
        col = int(data_config.get_url())
        url = self.opera_excel.get_cell_value(row, col)
        return url

    def get_request_data(self, row):
        '''获取请求数据字段'''
        col = int(data_config.get_data())
        data = self.opera_excel.get_cell_value(row, col)
        if data == '':
            return None
        return data

    def get_data_for_json(self, row):
        '''通过获取关键字拿到data数据'''
        opera_json = OperetionJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data

    def get_expcet_data(self, row):
        '''获取预期结果'''
        col = int(data_config.get_expect())
        expect = self.opera_excel.get_cell_value(row, col)
        if expect == '':
            return None
        return expect

    def get_expcet_data_for_mysql(self, row):
        '''通过sql获取预期结果'''
        op_mysql = OperationMysql()
        sql = self.get_expcet_data(row)
        res = op_mysql.search_one(sql)
        return res.encode('unicode-escape')

    def write_result(self, row, value):
        '''写入测试结果'''
        col = int(data_config.get_result())
        self.opera_excel.write_value(row, col, value)

    def is_depend(self, row):
        '''判断是否有case依赖'''
        col = int(data_config.get_case_depend())
        depend_case_id = self.opera_excel.get_cell_value(row, col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id

    def get_data_hierarchy(self, row):
        '''获取依赖返回数据的层级'''
        col = int(data_config.get_data_hierarchy())
        data_hierarchy = self.opera_excel.get_cell_value(row, col)
        return data_hierarchy

    def get_depend_data_key(self, row):
        '''获取数据依赖字段'''
        col = int(data_config.get_depend_data_key())
        depend_data_key = self.opera_excel.get_cell_value(row, col)
        if depend_data_key == "":
            return None
        else:
            return depend_data_key

    def get_depend_respond_data_key(self, row):
        '''获取依赖返回数据的key. 如order = {"code":200,data":{"key":...}}'''
        col = int(data_config.depend_respond_data_key())
        data = self.opera_excel.get_cell_value(row, col)
        if data == "":
            return None
        else:
            return data

    def get_depend_respond_data(self, row):
        '''获取依赖的返回数据'''
        col = int(data_config.depend_respond_data())
        data = self.opera_excel.get_cell_value(row, col)
        if data == "":
            return None
        else:
            return data

    def get_timestamp(self):
        '''获取毫秒级时间戳'''
        return int(round(time.time() * 1000))

    def get_time(self):
        '''获取年月日'''
        return time.strftime('%Y-%m-%d', time.localtime(time.time()))


if __name__ == '__main__':
    opear = GetData()
    print(opear.get_timestamp())
