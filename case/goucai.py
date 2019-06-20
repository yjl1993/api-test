# coding:utf-8
import sys,re
sys.path.append(r"C:\Users\Administrator\PycharmProjects\api-test")
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
        self.get_target_value=GetTargetValue()


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
        url="http://172.16.10.221/common/getLotteryList?debug=true"
        return_data=self.run.run_main(url,"get")
        lotteryId_list=[]
        count_id=len(return_data["data"]["lotteryList"])
        for a in range(count_id):
            data = return_data["data"]["lotteryList"][a]
            #print(data)
            #print(data["id"])
            lotteryId_list.append(data["id"])
        return lotteryId_list

    def lotteryNo(self):
        '''返回彩票期号'''
        count_id=len(self.lotteryId_list())
        lotteryNo_list=[]
        for a in range(count_id):
            Id=self.lotteryId_list()[a]
            url="http://172.16.10.221/common/getNewLotteryNo?debug=true&lotteryId="+str(Id)
            return_data=self.run.run_main(url,"get")
            data=return_data["data"]
            m = re.search(r'(?:[, ])"lotteryNo":("\d+")', data).group(1)#正则表达式查找字符串内容
            a=lotteryNo_list.append(m)
        print(lotteryNo_list)
        return lotteryNo_list

    def playId(self):
        '''返回彩票二级玩法编号'''
        count_id=len(self.lotteryId_list())
        for a in range(count_id):
            lotteryNo_list = []
            Id=self.lotteryId_list()[a]
            url="http://172.16.10.221/common/getLotteryDetail?debug=true&lotteryId="+str(Id)
            return_data = self.run.run_main(url, "get")
            data=return_data["data"]
            count_wanfa = len(data)
            for a in range(count_wanfa):
                data1 = data[a]
                playId=get_target_value.get_target_value("playId", data1, [])
                lotteryNo_list.append(playId)
            print(lotteryNo_list)
            return lotteryNo_list

    def playDetailId(self):
        '''返回彩票玩法明细编号'''
        count_id=len(self.lotteryId_list())
        lotteryNo_list = []
        for a in range(count_id):
            Id=self.lotteryId_list()[a]
            url="http://172.16.10.221/common/getLotteryDetail?debug=true&lotteryId="+str(Id)+""
            return_data = self.run.run_main(url, "get")
            data=return_data["data"]
            count_wanfa = len(data)
            for b in range(count_wanfa):
                data1 = data[b]
                playDetailId=get_target_value.get_target_value("playDetailId", data1, [])
                value=get_target_value.get_target_value("value", data1, [])
                lotteryNo_list.append(playDetailId+value)
                #lotteryNo_list.append(value)
        for c in range(len(lotteryNo_list)):
            print(c,lotteryNo_list[c])

        #print(lotteryNo_list)
        return lotteryNo_list

    def goucai(self):
        count_id=len(self.lotteryId_list())
        lotteryNo_list = []
        for a in range(count_id):
            url="http://172.16.10.221/trade/payment/odds=9.80&st=az&userId=976022&amount=6.00&addPeriodsStop=0&rebate=0.0&version=9.5.5&num=3&addPeriods=1"
            #lotteryId= 39 &playId=1053&timestamp=1561014634583&playDetailId=683%20704%20705&lotteryNo=201906200912&bettingValue=9%7C9%7C9


if __name__ == '__main__':
    goucai=GouCai()
    get_target_value=GetTargetValue()
    #goucai.lotteryId_list()
    #goucai.lotteryNo()
    #goucai.playId()
    goucai.playDetailId()

    data={"code":200,"data":[{"defaultt": 0, "erjiwanfa": [
        {"calType": "1", "cid": 8, "formula": "n1+n2+n3", "id": 1053, "isBase": 0, "isOnly": 0, "isShowOdds": 0,
         "itemMaxAmount": 999999, "maxRebate": 10, "name": "定位胆", "noSplit": 1, "noteMaxAmount": 999999,
         "noteMinAmount": 0.01, "odds": 9.8,
         "playExplain": {"example": "选号：十位 3，开奖号：* 3 *。", "id": 343, "playCue": "任选1个位置并选1个号码组成一注。", "playId": 1053,
                         "winningCue": "所选号与相同位置上的开奖号一致，即为中奖。"}, "rules": "3-1|1", "sanjiwanfa": [
            {"id": 683, "name": "百位",
             "playValueList": [{"id": 8539, "orderId": 0, "playDetailId": 683, "type": 1, "value": "0"},
                               {"id": 8548, "orderId": 9, "playDetailId": 683, "type": 1, "value": "9"}],
             "sortName": "B", "valueType": 1}, {"id": 704, "name": "十位", "playValueList": [
                {"id": 8770, "orderId": 0, "playDetailId": 704, "type": 1, "value": "0"},
                {"id": 8779, "orderId": 9, "playDetailId": 704, "type": 1, "value": "9"}], "sortName": "S","valueType": 1},
            {"id": 705, "name": "个位", "playValueList": [
                {"id": 8780, "orderId": 0, "playDetailId": 705, "type": 1, "value": "0"},
                {"id": 8789, "orderId": 9, "playDetailId": 705, "type": 1, "value": "9"}], "sortName": "G","valueType": 1}],
         "showMaxOdds": 1, "showNum": 6}],"id": 1048, "name": "定位胆", "playDetail": 1},


          {"defaultt": 0, "erjiwanfa": [
              {"calType": "1", "cid": 8, "formula": "n1+n2+n3", "id": 1054, "isBase": 0, "isOnly": 0, "isShowOdds": 0,
               "itemMaxAmount": 999999, "maxRebate": 10, "name": "定位胆", "noSplit": 1, "noteMaxAmount": 999999,
               "noteMinAmount": 0.01, "odds": 9.8,
               "playExplain": {"example": "选号：十位 3，开奖号：* 3 *。", "id": 343, "playCue": "任选1个位置并选1个号码组成一注。",
                               "playId": 1053,
                               "winningCue": "所选号与相同位置上的开奖号一致，即为中奖。"}, "rules": "3-1|1", "sanjiwanfa": [
                  {"id": 683, "name": "百位",
                   "playValueList": [{"id": 8539, "orderId": 0, "playDetailId": 684, "type": 1, "value": "0"},

                                     {"id": 8548, "orderId": 9, "playDetailId": 684, "type": 1, "value": "9"}],
                   "sortName": "B", "valueType": 1}, {"id": 704, "name": "十位", "playValueList": [
                      {"id": 8770, "orderId": 0, "playDetailId": 705, "type": 1, "value": "0"},

                      {"id": 8779, "orderId": 9, "playDetailId": 705, "type": 1, "value": "9"}], "sortName": "S",
                                                      "valueType": 1}, {"id": 705, "name": "个位", "playValueList": [
                      {"id": 8780, "orderId": 0, "playDetailId": 706, "type": 1, "value": "0"},

                      {"id": 8789, "orderId": 9, "playDetailId": 706, "type": 1, "value": "9"}], "sortName": "G",
                                                                        "valueType": 1}], "showMaxOdds": 1,
               "showNum": 6}],
           "id": 1048, "name": "定位胆", "playDetail": 1}]}

    '''count_wanfa=len(data)
    for a in range(count_wanfa):
        data1=data[a]
        print("id",get_target_value.get_target_value("playDetailId",data1,[]))'''