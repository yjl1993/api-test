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
    cb={"code":200,"data":
        {"lotteryDraw":
             {"lottery":
                  {"logo":{},
                   "typeName":""},"lotteryNo":"201906171021"}}}

    get_target_value=GetTargetValue()
    a={"code":200,"data":{"lotteryList":[{"logo":{"filename":"1219bjpks.png","imgSize":"","resultLotteryCode":"bjpks","typeName":""}},
                                   {"logo":{"filename":"1219ffssc.png","imgSize":"","resultLotteryCode":"ffssc","typeName":""}}]}}
    data=(get_target_value.get_target_value("lotteryNo",cb,[]))
    print(data[0])
