# coding:utf-8
import sys, re, time, threading, multiprocessing, requests

sys.path.append(r"..\PycharmProjects\api-test")
from demo import RunMain
from time import sleep, ctime


class Login:

    def __init__(self):
        self.run = RunMain()

    def login_api(self):
        '''登录接口-批量执行login_user文件里的登录账号'''
        start_time = int(round(time.time() * 1000))
        with open("..\dataconfig\login_user.txt", "r") as f:
            for line in f.readlines():
                line = line.strip('\n')  # 去掉列表中每一个元素的换行符
                time1 = int(round(time.time() * 1000))
                url = "http://172.16.10.221/common/login?debug=true&password=123456&wssid=138%3A%5B172-16-10-223%5D&account=" + str(
                    line)
                self.run.run_main(url, "get")
                time2 = int(round(time.time() * 1000))
                # print("登录接口响应速度/ms：",time2-time1)
        end_time = int(round(time.time() * 1000))
        print(end_time - start_time)

    def payment(self):
        """购彩接口"""
        start_time = int(round(time.time() * 1000))
        timestamp = round(time.time() * 1000)
        url1 = "http://172.16.10.221/common/getNewLotteryNo?debug=true&lotteryId=30"
        return_data = self.run.run_main(url1, "get")
        data = return_data["data"]
        m = re.search(r'(?:[, ])"nextNo":("\d+")', data).group(1)  # 正则表达式查找字符串内容
        for i in range(101):
            time1 = int(round(time.time() * 1000))
            url = "http://172.16.10.221/trade/payment"
            data = {"st": "az", "lotteryId": "30", "userId": "976022",
                    "lotteryNo": "20190624214", "playId": "72-72", "playDetailId": "127-127",
                    "bettingValue": "04-03", "amount": "10.00-10.00", "addPeriodsStop": "0",
                    "rebate": "0.0-0.00", "version": "9.6.0", "num": "1-1", "addPeriods": "1",
                    "odds": "48.80-48.80", "debug": "true", "timestamp": "1561363847058"
                    }
            self.run.run_main(url, "post", data)
            time2 = int(round(time.time() * 1000))
            print("登录接口响应速度/ms：", time2 - time1)
        end_time = int(round(time.time() * 1000))
        print(end_time - start_time)

    def login(self):
        print("开始循环：", ctime())
        url = "http://172.16.10.221/common/login?debug=true&password=123456&wssid=138%3A%5B172-16-10-223%5D&account=testtg526"
        requests.get(url)
        print("结束循环：", ctime())


if __name__ == '__main__':
    login = Login()
    threads = []
    for line in range(100):
        print(line)
        t = threading.Thread(target=login.login())
        t.start()
