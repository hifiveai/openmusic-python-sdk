'''
Created by yong.huang on 2016.11.04
'''
from top.api.base import RestApi


class HifiveOrderRefundRequest(RestApi):
    def __init__(self, domain='hifive-gateway-test.hifiveai.com', port=80):
        RestApi.__init__(self, domain, port)
        self.clientId = None
        self.orderId = None

    def getapiname(self):
        return 'OrderRefund'