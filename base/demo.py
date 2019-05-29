import requests
import json
class RunMain:

	def send_get(self,url,data):
		res = requests.get(url=url,data=data).json()
		return res
		
	def send_post(self,url,data):
		res = requests.post(url=url,data=data).json()
		return res

	def run_main(self,url,method,data=None):
		res = None
		if method == 'GET':
			res = self.send_get(url,data)
		else:
			res = self.send_post(url,data)
		return res

if __name__ == '__main__':
	#url = 'http://172.16.10.221/trade/payment?odds=9.80-9.80&st=az&sign=0940E3B3B4FA6289F696BD027F7FA017&lotteryId=32&userId=976022&token=959F10EDD89F583C6966B588F029A672&playId=1218-1218&timestamp=1559026681347&amount=100.00-2.00&playDetailId=885 886 887 888 890 891 892 893 894 895-895&addPeriodsStop=0&rebate=0.0-0.00&version=8.7.5&num=10-1&addPeriods=1&lotteryNo=20190528181&bettingValue=01|01|02|01|01|03|04|03|01|05-|||||||||08&debug=true'
	url='http://172.16.10.221/user/userSignIn?st=az&timestamp=1559027821253&sign=C92BECCC52A222C61D12A3451865951A&userId=976022&token=959F10EDD89F583C6966B588F029A672'
	data={

	}
	run = RunMain()
	a=run.run_main(url,'GET')
	print(a)
	#unittest
	#print run.run_main(url,'GET',data)

