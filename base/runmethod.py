#coding:utf-8
import requests
import json
class RunMethod:
	def post_main(self,url,data,header=None):
		res = None
		if header !=None:	
			res = requests.post(url=url,data=data,headers=header)
		else:
			res = requests.post(url=url,data=data)
		return res.json()

	def get_main(self,url,data=None,header=None):
		res = None
		if header !=None:	
			res = requests.get(url=url,data=data,headers=header,verify=False)
		else:
			res = requests.get(url=url,data=data,verify=False)
		return res.json()

	def run_main(self,method,url,data=None,header=None):
		res = None
		if method == 'post':
			res = self.post_main(url,data,header)
		else:
			res = self.get_main(url,data,header)
		return json.dumps(res,ensure_ascii=False)
		#return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)

if __name__ == '__main__':
	run = RunMethod()
	url="172.16.10.221/trade/payment"
	data1="debug=true&odds=5880000.00&lotteryId=37&userId=976022&playId=1306&timestamp=1559645963493&amount=10.00&playDetailId=956%20957&addPeriodsStop=0&rebate=0.0&version=8.8.7&num=1&addPeriods=1&lotteryNo=2019064&bettingValue=01%2010%2021%2022%2028%2029%7C04"
	data={
		"debug":"true",
"odds"	:"5880000.00",
"st"	:"	az",
"lotteryId	"	:37,
"userId"	:	976022,
"playId"	:"	1306",
"timestamp"	:	1559645963493,
"amount	"	:"10.00",
"playDetailId	"	:"956 957",
"addPeriodsStop"	:"	0",
"rebate"	:"	0.0",
"version	"	:"8.8.7",
"num"	:"	1",
"addPeriods"	:1,
"lotteryNo	"	:"2019064",
"bettingValue"	:"	01|04"}

	print(run.run_main('post',"http://"+url,data))
