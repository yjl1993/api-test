#coding:utf-8
import sys,re
import json
sys.path.append(r'..\PycharmProjects\api-test')
from util.operation_excel import OperationExcel
from base.runmethod import RunMethod
from data.get_data import GetData
from get_target_value import GetTargetValue
from jsonpath_rw import jsonpath,parse
class DependdentData:
	def __init__(self,case_id):
		self.case_id = case_id
		self.opera_excel = OperationExcel()
		self.data = GetData()

	def get_case_line_data(self):
		'''通过case_id去获取该case_id的整行数据'''
		rows_data = self.opera_excel.get_rows_data(self.case_id)
		return rows_data

	def run_dependent(self):
		'''执行依赖case测试，获取结果'''
		run_method = RunMethod()
		row_num  = self.opera_excel.get_row_num(self.case_id)
		request_data = self.data.get_data_for_json(row_num)
		request_data['userId'] = "976022"
		request_data["timestamp"] = self.data.get_timestamp()
		request_data["debug"]="true"
		#header = self.data.is_header(row_num)
		method = self.data.get_request_method(row_num)
		url = self.data.get_request_url(row_num)
		res = run_method.run_main(method,url,request_data)
		return json.loads(res)


	def get_data_for_key(self,row):
		'''根据依赖的key去获取执行依赖测试case的响应,然后返回'''
		depend_respond_data_key = self.data.get_depend_respond_data_key(row)
		depend_respond_data=self.data.get_depend_respond_data(row)
		data_hierarchy=self.data.get_data_hierarchy(row)
		response_data = self.run_dependent()
		if data_hierarchy=="":#{"code":200,"data":{"drawList":[{"id":69552}]}}
			data_list=response_data["data"][depend_respond_data_key]
			for data in data_list:
				return (data[depend_respond_data])

		elif data_hierarchy == 1:#{"data":"289470"}
			data1=response_data[depend_respond_data]
			return data1

		elif data_hierarchy == 2:#{"code":200,"data":[{"code":"960200"}]}
			data_list=response_data[depend_respond_data_key]
			for data2 in data_list:
				return (data2[depend_respond_data])

		elif data_hierarchy == 3:#适用该数据结构{"code":200,"data":{"activeId":"61"}}
			data_list=response_data[depend_respond_data_key]
			data2=data_list[depend_respond_data]
			return data2

		elif data_hierarchy == 4:#{"code":200,"data":[{"id":7728,"lottery":{"id":"30","a":"1"}}]}
			data_list = response_data["data"]
			for data4 in data_list:
				return (data4[depend_respond_data_key][depend_respond_data])

		elif data_hierarchy == 5:#{"code":200,"data":{"feedback":{"id":700}}}
			data_list = response_data["data"][depend_respond_data_key]
			data5=data_list[depend_respond_data]
			return data5

		elif data_hierarchy == 6:
			get_target_value = GetTargetValue()
			data6=get_target_value.get_target_value(depend_respond_data,response_data,[])
			return data6[0]

		elif data_hierarchy == "正则":
			data = response_data["data"]
			m = re.search(r'(?:[, ])"lotteryNo":("\d+")', data).group(1)
			return m


		'''else:
				data = response_data["data"][depend_respond_data]
				return (data)'''
		#json_exe = parse(depend_data)
		#madle = json_exe.find(data)
		#return [math.value for math in madle][0]

if __name__ == '__main__':
	order={"code":200,"data":{"feedback":{"id":700}}}
	data1={"code":200,"data":[{"id":7728,"lottery":{"id":"30","a":"1"}}]}
	data2=(data1["data"])
	data_list = order["data"]["feedback"]
	print(data_list["id"])
	x=data1.get("data")
	print(x)
	#for data in data_list:
		#print (data["id"])
#index = data.index('id') if ('id' in data) else -1
#print(index)
#res = "id"
#json_exe = parse(res)
#madle = json_exe.find(data)
#print ([math.value for math in madle][0])