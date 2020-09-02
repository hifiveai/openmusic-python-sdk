'''
Created by yong.huang on 2016.11.04
'''
from top.api.base import RestApi
class HifiveAuthorizationRequest(RestApi):
	def __init__(self,domain='hifive-gateway-test.hifiveai.com',port=80):
		RestApi.__init__(self,domain, port)
		self.clientId = None
		self.companyName = None
		self.projectName = None
		self.brand = None
		self.period = None
		self.area = None
		self.orderIds = None

	def getapiname(self):
		return 'OrderAuthorization'