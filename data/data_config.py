#coding:utf-8
class global_var:
	#case_id
	Id = '0'
	request_name = '1'
	url = '2'
	run = '3'
	request_way = '4'
	header = '5'
	case_depend = '6'
	data_hierarchy='7'
	depend_respond_data_key = '8'
	depend_respond_data='9'
	depend_data_key = '10'
	data = '11'
	expect = '12'
	result = '13'
#获取caseid
def get_id():
	'''获取caseid'''
	return global_var.Id

#获取url
def get_url():
	'''获取url'''
	return global_var.url

def get_run():
	'''是否运行该case'''
	return global_var.run

def get_run_way():
	'''请求类型'''
	return global_var.request_way

def get_header():
	'''是否携带header'''
	return global_var.header

def get_case_depend():
	'''case依赖'''
	return global_var.case_depend

def get_data_hierarchy():
	'''返回的依赖数据层级'''
	return global_var.data_hierarchy

def depend_respond_data_key():
	'''依赖返回数据的key. 如order = {"code":200,data":{"key":...}}'''
	return global_var.depend_respond_data_key

def depend_respond_data():
	'''依赖的返回数据'''
	return global_var.depend_respond_data

def get_depend_data_key():
	'''数据依赖字段'''
	return global_var.depend_data_key





def get_data():
	'''请求数据'''
	return global_var.data

def get_expect():
	'''预期结果'''
	return global_var.expect

def get_result():
	'''实际结果'''
	return global_var.result

def get_header_value():
	return global_var.header
