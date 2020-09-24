# coding:utf-8
import requests
import json
import time
from get_target_value import GetTargetValue
class RunMain:

	def send_get(self, url, data=None):
		res = requests.get(url=url, data=data).json()
		return res
		
	def send_post(self,url,data):
		res = requests.post(url=url,data=data).json()
		return res

	def run_main(self,url,method,data=None):
		res = None
		if method == 'get':
			res = self.send_get(url,data)
		else:
			res = self.send_post(url,data)
		return res#json.dumps(res,ensure_ascii=False)

if __name__ == '__main__':
	t = (time.time())
	timec=int(round(t * 1000))

	#url = 'http://172.16.10.221/trade/payment?odds=9.80-9.80&st=az&sign=0940E3B3B4FA6289F696BD027F7FA017&lotteryId=32&userId=976022&token=959F10EDD89F583C6966B588F029A672&playId=1218-1218&timestamp=1559026681347&amount=100.00-2.00&playDetailId=885 886 887 888 890 891 892 893 894 895-895&addPeriodsStop=0&rebate=0.0-0.00&version=8.7.5&num=10-1&addPeriods=1&lotteryNo=20190528181&bettingValue=01|01|02|01|01|03|04|03|01|05-|||||||||08&debug=true'
	url='http://172.16.10.221/trade/payment?debug=true&userId=976025&lotteryId=40&lotteryNo=201905301191&playId=72&playDetailId=172&bettingValue=08&odds=48.75&rebate=0&num=1&amount=10&addPeriods=1&version=8.7.7&timestamp=%s'%timec
	url2='http://172.16.10.221/common/getLotteryList?debug=true&timestamp=1559027821253'
	url3='http://172.16.10.221/common/playExplainByLotteryId?timestamp=1559205952095&lotteryId=2&debug=true'
	url4="http://172.16.10.221/common/getLotteryList?userId=976022&timestamp=1560481120529&debug=true&startTime=2017-01-01&endTime=2019-06-14"
	url5="http://172.16.10.221/common/getNewLotterResultList?st=az&timestamp=1560764641501&lotteryIds=24%2C26%2C37%2C2%2C60%2C33%2C28%2C6%2C41%2C29%2C27%2C34%2C39%2C38%2C40&sign=3381AD13AFB825DD03B7290AD51EE382"
	url6="http://172.16.10.221/common/getLotteryList?userId=976022&timestamp=1560765477148&debug=true&startTime=2017-01-01&endTime=2019-06-17"
	#u='http://172.16.10.221/comment/login?account=test9527&password=123456&timestamp=1559027821253&debug=true'
	run = RunMain()
	get_target_value=GetTargetValue()
	#a=run.run_main(url,'get')
	b=run.run_main(url,'get')
	c=run.run_main(url3,"get")
	d=run.run_main(url4,"get")
	e=run.run_main(url5,"get")
	f=run.run_main(url6,"get")
	#u1=run.run_main(u,'get')
	#print(b)
	#print (c)
	#json_dict = json.dumps(b)
	#for item in b['data']['lotteryList']:
		#name = item['name']
		#id=item['id']
		#print('%s ' % (name))
	print(len(get_target_value.get_target_value("name",f,[])))
	print(get_target_value.get_target_value("name",f,[]))
	'''for item in c['data']:
		name = item['name']
		print('%s ' % (name))

	for item3 in c['data'][0]['sencondPlayArray']:
		name = item3['name']
		#id=item['id']
		playId=['playId']
		print('%s ' % (name))

	a=len(c["data"])-1
	i=0
	while i<a:
		i+=1
		for item3 in c['data'][i]['sencondPlayArray']:
			name = item3['name']
			#id=item['id']
			print('%s ' % (name))
			#print(item)

	#print(u1)

	#unittest
	#print run.run_main(url,'GET',data)'''


