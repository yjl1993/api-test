# coding:utf-8
"""
@author:Miko.yu
@file: get_target_value.py
@time: 2019/6/12
"""
class GetTargetValue:
    def get_target_value(self,key, dic, tmp_list):
        """
        :param key: 目标key值
        :param dic: JSON数据
        :param tmp_list: 用于存储获取的数据
        :return: list
        """
        if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
            return 'argv[1] not an dict or argv[-1] not an list '

        if key in dic.keys():
            tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list
        else:
            for value in dic.values():  # 传入数据不符合则对其value值进行遍历
                if isinstance(value, dict):
                    self.get_target_value(key, value, tmp_list)  # 传入数据的value值是字典，则直接调用自身
                elif isinstance(value, (list, tuple)):
                    self._get_value(key, value, tmp_list)  # 传入数据的value值是列表或者元组，则调用_get_value
        return tmp_list


    def _get_value(self,key, val, tmp_list):
        for val_ in val:
            if isinstance(val_, dict):
                self.get_target_value(key, val_, tmp_list)  # 传入数据的value值是字典，则调用get_target_value
            elif isinstance(val_, (list, tuple)):
                self._get_value(key, val_, tmp_list)   # 传入数据的value值是列表或者元组，则调用自身

if __name__=="__main__":
    order = {"code": 200, "data": {"feedback": {"id": 700}}}
    data1 = {"code": 200, "data": [{"id": 7728, "lottery": {"id": "30", "a": "1"}}]}
    cb={'code': 200, 'data': '{"addTime":1560848700000,"beginTime":1560848640000,"closeTime":15699,"endTime":1560848689000,"lottery":{"addTime":1530943200000,"beginTime":0,"cid":8,"code":"js3d","color":"#000000","cycleType":1,"endTime":10,"id":39,"isHot":0,"isPrivate":1,"level":1,"logo":{"filename":"1219js3d.png","fileurl":"upload/logo/lottery/20181219/js3d.png","id":1232,"imgSize":"","lastTime":1545189750,"status":1,"type":0,"uploadSize":6000},"logoId":1232,"name":"极速3D","noType":1,"orderId":10,"pid":0,"remark":"1分钟一期","resultLotteryCode":"js3d","shortNoLength":4,"showType":3,"status":1,"type":11},"lotteryId":39,"lotteryNo":"201906181026","nextNo":"201906181027","nextTime":1560848760000,"queryHistory":false,"remainTime":15699,"result":"9,9,6","shortNextNo":"1027","shortNo":"1026","type":1}', 'message': '成功', 'version': '9.4.1'}
    get_target_value=GetTargetValue()
    a={"code":200,"data":{"lotteryList":[{"logo":{"filename":"1219bjpks.png","imgSize":"","resultLotteryCode":"bjpks","typeName":""}},
                                   {"logo":{"filename":"1219ffssc.png","imgSize":"","resultLotteryCode":"ffssc","typeName":""}}]}}
    data=(get_target_value.get_target_value("lotteryNo",cb,[]))
    print(data)
