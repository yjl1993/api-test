# coding:utf-8
import sys
import threading

sys.path.append(r"C:\Users\Administrator\PycharmProjects\api-test")
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DependdentData
from util.send_email import SendEmail
from util.operation_header import OperationHeader
from util.operation_json import OperetionJson
from operation_excel import OperationExcel


class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.send_mai = SendEmail()
        self.operation_excel = OperationExcel()

    # 程序执行的
    def go_on_run(self):
        res = None
        pass_count = []
        fail_count = []
        # 10  0,1,2,3
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url_dizhi = self.data.get_request_url(i)
                url_yuming = "http://172.16.10.211/"
                url = self.data.get_request_url(i)
                # url = url_dizhi + "&timestamp=" + str(self.data.get_timestamp())
                method = self.data.get_request_method(i)
                request_data = self.data.get_data_for_json(i)
                request_data['userId'] = "976022"
                request_data["timestamp"] = self.data.get_timestamp()
                request_data["debug"] = "true"
                request_data["startTime"] = "2017-01-01"
                request_data["endTime"] = self.data.get_time()
                # expect = self.data.get_expcet_data_for_mysql(i)
                expect = self.data.get_expcet_data(i)
                header = self.data.is_header(i)
                depend_case = self.data.is_depend(i)
                if depend_case != None:
                    self.depend_data = DependdentData(depend_case)
                    # 获取的依赖响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    # 获取依赖的key
                    depend_data_key = self.data.get_depend_data_key(i)
                    request_data[depend_data_key] = str(depend_response_data)

                if header == 'write':
                    res = self.run_method.run_main(method, url, request_data)
                    op_header = OperationHeader(res)
                    op_header.write_cookie()

                elif header == 'yes':
                    op_json = OperetionJson('../dataconfig/cookie.json')
                    cookie = op_json.get_data('apsid')
                    cookies = {
                        'apsid': cookie
                    }
                    res = self.run_method.run_main(method, url, request_data, cookies)
                else:
                    res = self.run_method.run_main(method, url, request_data)

                # if self.com_util.is_equal_dict(expect,res) == 0:
                # if self.com_util.is_contain(expect, res) :
                if expect in res:
                    self.data.write_result(i, 'pass')
                    pass_count.append(i)
                else:
                    print('失败Id:', self.operation_excel.get_cell_value(i, 0), res)
                    self.data.write_result(i, 'fail')
                    fail_count.append(i)
        print("成功:", len(pass_count), "失败:", len(fail_count))
    # self.send_mai.send_main(pass_count,fail_count)


# 将执行判断封装
# def get_cookie_run(self,header):


if __name__ == '__main__':
    run = RunTest()
    # run.go_on_run()
    threads = []
    for line in range(3):
        print(line)
        t = threading.Thread(target=run.go_on_run())
        t.start()
