# coding:utf-8
import json


class OperetionJson:

    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = '../dataconfig/user.json'
        else:
            self.file_path = file_path
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        '''	读取json文件'''
        with open(self.file_path, "rb") as fp:
            data = json.load(fp)
            return data

    def get_data(self, id):
        '''根据关键字获取数据'''
        return self.data[id]

    # 写json
    def write_data(self, data):
        '''写json'''
        with open('../dataconfig/cookie.json', 'w') as fp:
            fp.write(json.dumps(data))


if __name__ == '__main__':
    opjson = OperetionJson()
    print(opjson.get_data('shijianchuo'))
