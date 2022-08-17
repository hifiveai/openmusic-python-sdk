'''
Created by yong.huang on 2016.11.04
'''
from hifive.api.base import RestApi
class HFSheetDetailRequest(RestApi):
	def __init__(self,domain=None,port=80, method=None):
		domain = domain or 'hifive-gateway-test.hifiveai.com';
		method = method or 'POST';
		RestApi.__init__(self,domain, port , method)
		self.clientId = None
		self.sheetId = None

	def getapiname(self):
		return 'SheetDetail'
