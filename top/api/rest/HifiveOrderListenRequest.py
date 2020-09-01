'''
Created by yong.huang on 2016.11.04
'''
from top.api.base import RestApi


class HifiveOrderListenRequest(RestApi):
    def __init__(self, domain='hifive-gateway-test.hifiveai.com', port=80):
        RestApi.__init__(self, domain, port)
        self.clientId = None
        self.musicId = None
        self.audioFormat = None
        self.audioRate = None

    def getapiname(self):
        return 'OrderListen'