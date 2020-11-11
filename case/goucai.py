# coding:utf-8
import sys, re

sys.path.append(r"..\PycharmProjects\api-test")
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DependdentData
from util.send_email import SendEmail
from util.operation_header import OperationHeader
from util.operation_json import OperetionJson
from operation_excel import OperationExcel
from get_target_value import GetTargetValue
from demo import RunMain


class GouCai:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.send_mai = SendEmail()
        self.operation_excel = OperationExcel()
        self.run = RunMain()
        self.get_target_value = GetTargetValue()

    '''def lotteryId(self):
        ''返回彩票一级玩法编号''
        url="http://172.16.10.221/common/getLotteryList?debug=true"
        return_data=self.run.run_main(url,"get")
        #data=return_data["data"]["lotteryList"][i]
        #print(self.get_target_value.get_target_value("id",data,[])[0])
        #return self.get_target_value.get_target_value("id",data,[])[0]
        #print(return_data["data"]["lotteryList"])
        count_id=len(return_data["data"]["lotteryList"])
        for a in range(count_id):
            data = return_data["data"]["lotteryList"][a]
            id=self.get_target_value.get_target_value("id",data,[])
            return id
            #print(data)'''

    def lotteryId_list(self):
        '''返回彩票一级玩法编号列表'''
        url = "http://172.16.10.221/common/getLotteryList?debug=true"
        return_data = self.run.run_main(url, "get")
        lotteryId_list = []
        count_id = len(return_data["data"]["lotteryList"])
        for a in range(count_id):
            data = return_data["data"]["lotteryList"][a]
            # print(data)
            # print(data["id"])
            lotteryId_list.append(data["id"])
        with open("..\dataconfig\lotteryId.txt", "w") as f:
            for list_mem in lotteryId_list:
                f.write(str(list_mem) + "\n")

    def lotteryNo(self):
        '''返回彩票期号'''
        lotteryNo_list = []
        with open("..\dataconfig\lotteryId.txt", "r") as f:
            for line in f.readlines():
                line = line.strip('\n')  # 去掉列表中每一个元素的换行符
                url = "http://172.16.10.221/common/getNewLotteryNo?debug=true&lotteryId=" + str(line)
                return_data = self.run.run_main(url, "get")
                data = return_data["data"]
                m = re.search(r'(?:[, ])"lotteryNo":("\d+")', data).group(1)  # 正则表达式查找字符串内容
                a = lotteryNo_list.append(m)
        with open("..\dataconfig\lotteryNo_list.txt", "w") as f:
            for list_mem in lotteryNo_list:
                f.write(str(list_mem) + "\n")
        # print(lotteryNo_list)
        # return lotteryNo_list

    def get_playId(self):
        '''返回彩票二级玩法编号'''
        playId_list = []

        with open("..\dataconfig\lotteryId.txt", "r") as f:
            for line in f.readlines():
                line = line.strip('\n')  # 去掉列表中每一个元素的换行符
                url = "http://172.16.10.221/common/getLotteryDetail?debug=true&lotteryId=" + str(line) + ""
                LotteryDetail_data = self.run.run_main(url, "get")  # 彩票的所有信息数据
                data = LotteryDetail_data["data"]
                count_erjiwanfa = len(data)
                for b in range(count_erjiwanfa):
                    data1 = data[b]
                    list = []
                    for c in data1["erjiwanfa"]:
                        data2 = c["playExplain"]
                        list.append(get_target_value.get_target_value("playId", data2, []))
                        print(list)
                        # playId_list.append(get_target_value.get_target_value("playId", data2, []))
                # print(playId_list)
        with open("..\dataconfig\playId_list.txt", "w") as f:
            for list_mem in playId_list:
                f.write(str(list_mem) + "\n")
        # print(lotteryNo_list)
        # print(playDetailId_list)

    def playDetailId(self):
        '''返回彩票玩法明细编号'''
        playDetailId_list = []
        with open("..\dataconfig\lotteryId.txt", "r") as f:
            for line in f.readlines():
                line = line.strip('\n')  # 去掉列表中每一个元素的换行符
                url = "http://172.16.10.221/common/getLotteryDetail?debug=true&lotteryId=" + str(line) + ""
                return_data = self.run.run_main(url, "get")
                data = return_data["data"]
                count_erjiwanfa = len(data)
                for b in range(count_erjiwanfa):
                    data1 = data[b]
                    playDetailId = get_target_value.get_target_value("playDetailId", data1, [])
                    value = get_target_value.get_target_value("value", data1, [])
                    for c in range(len(playDetailId)):
                        # print(playDetailId[c])
                        playDetailId_value = str(playDetailId[c]) + ":" + value[c]
                        playDetailId_list.append(playDetailId_value)
        with open("..\dataconfig\playDetailId_list.txt", "w") as f:
            for list_mem in playDetailId_list:
                f.write(str(list_mem) + "\n")

    def goucai(self):
        count_id = len(self.lotteryId_list())
        for a in range(count_id):  # 根据lotteryId的数量来执行
            Id = self.lotteryId_list()[a]
            url = "http://172.16.10.221/common/getLotteryDetail?debug=true&lotteryId=" + str(Id) + ""
            LotteryDetail_data = self.run.run_main(url, "get")  # 彩票的所有信息数据
            data = LotteryDetail_data["data"]
            count_erjiwanfa = len(data)
            for b in range(count_erjiwanfa):
                data1 = data[b]
                for c in data[b]["erjiwanfa"]:
                    data1 = c["playExplain"]
                    print(get_target_value.get_target_value("playId", data1, []))
                playDetailId = get_target_value.get_target_value("playDetailId", data1, [])
                value = get_target_value.get_target_value("value", data1, [])
                playId = get_target_value.get_target_value("playId", data1, [])
                # print(playId)
                for c in range(len(playDetailId)):
                    print(playDetailId[c])
                    print(value[c])

    def login_api(self):
        '''登录接口'''
        with open("..\dataconfig\login_user.txt", "r") as f:
            for line in f.readlines():
                line = line.strip('\n')  # 去掉列表中每一个元素的换行符
                url = "http://172.16.10.221/common/login?debug=true&password=123456&wssid=138%3A%5B172-16-10-223%5D&account=" + str(
                    line)
                return_data = self.run.run_main(url, "get")
                print(return_data)
                print("lo")


if __name__ == '__main__':
    goucai = GouCai()
    get_target_value = GetTargetValue()
    # goucai.lotteryId_list()
    # goucai.lotteryNo()
    # goucai.get_playId()
    # goucai.playDetailId()
    # goucai.goucai()
    goucai.login_api()

    data = {"code": 200, "data": [{"defaultt": 0, "erjiwanfa": [
        {"calType": "1", "cid": 8, "formula": "n1+n2+n3", "id": 1053, "isBase": 0, "isOnly": 0, "isShowOdds": 0,
         "itemMaxAmount": 999999, "maxRebate": 10, "name": "定位胆", "noSplit": 1, "noteMaxAmount": 999999,
         "noteMinAmount": 0.01, "odds": 9.8,
         "playExplain": {"example": "选号：十位 3，开奖号：* 3 *。", "id": 343, "playCue": "任选1个位置并选1个号码组成一注。", "playId": 1053,
                         "winningCue": "所选号与相同位置上的开奖号一致，即为中奖。"}, "rules": "3-1|1", "sanjiwanfa": [
            {"id": 683, "name": "百位",
             "playValueList": [{"id": 8539, "orderId": 0, "playDetailId": 683, "type": 1, "value": "0"}],
             "sortName": "B", "valueType": 1}, {"id": 704, "name": "十位", "playValueList": [
                {"id": 8779, "orderId": 9, "playDetailId": 704, "type": 1, "value": "9"}], "sortName": "S",
                                                "valueType": 1},
            {"id": 705, "name": "个位", "playValueList": [
                {"id": 8789, "orderId": 9, "playDetailId": 705, "type": 1, "value": "9"}], "sortName": "G",
             "valueType": 1}],
         "showMaxOdds": 1, "showNum": 6}], "id": 1048, "name": "定位胆", "playDetail": 1},

                                  {"defaultt": 0, "erjiwanfa": [
                                      {"calType": "1", "cid": 8, "formula": "n1+n2+n3", "id": 1054, "isBase": 0,
                                       "isOnly": 0, "isShowOdds": 0,
                                       "itemMaxAmount": 999999, "maxRebate": 10, "name": "定位胆", "noSplit": 1,
                                       "noteMaxAmount": 999999,
                                       "noteMinAmount": 0.01, "odds": 9.8,
                                       "playExplain": {"example": "选号：十位 3，开奖号：* 3 *。", "id": 343,
                                                       "playCue": "任选1个位置并选1个号码组成一注。",
                                                       "playId": 1054,
                                                       "winningCue": "所选号与相同位置上的开奖号一致，即为中奖。"}, "rules": "3-1|1",
                                       "sanjiwanfa": [{"id": 683, "name": "百位",
                                                       "playValueList": [
                                                           {"id": 8539, "orderId": 0, "playDetailId": 684, "type": 1,
                                                            "value": "0"}],
                                                       "sortName": "B", "valueType": 1},
                                                      {"id": 704, "name": "十位", "playValueList": [
                                                          {"id": 8779, "orderId": 9, "playDetailId": 705, "type": 1,
                                                           "value": "9"}], "sortName": "S", "valueType": 1},
                                                      {"id": 705, "name": "个位", "playValueList": [
                                                          {"id": 8789, "orderId": 9, "playDetailId": 706, "type": 1,
                                                           "value": "9"}], "sortName": "G",
                                                       "valueType": 1}], "showMaxOdds": 1, "showNum": 6}],
                                   "id": 1048, "name": "定位胆", "playDetail": 2}]}

    count_wanfa = len(data["data"])
    # print(data["data"][0]["erjiwanfa"])
    for a in range(count_wanfa):
        for b in data["data"][a]["erjiwanfa"]:
            B = b["playExplain"]
            # print(get_target_value.get_target_value("playId",B,[]))

        # print(data1)

        # sanjiwanfa=data1['erjiwanfa'][14]
        # print(sanjiwanfa)
        # sanjiwanfa=get_target_value.get_target_value("sanjiwanfa",data1,[])
    # print(get_target_value.get_target_value("id",sanjiwanfa,[]))
    # list = [[1,2,66,58,64],[12],[22],[13],[14],[45],[6],]
    # with open(r"C:\Users\Administrator\PycharmProjects\api-test\dataconfig\lotteryId.txt", "w") as f:
    # for list_mem in list:
    #  f.write(str(list_mem)+"\n")
# with open(r"C:\Users\Administrator\PycharmProjects\api-test\dataconfig\lotteryId.txt", "r") as f:
# for line in f.readlines():
#  line = line.strip('\n')  # 去掉列表中每一个元素的换行符
# print(line)
