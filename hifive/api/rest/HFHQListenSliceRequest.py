'''
Created by yong.huang on 2016.11.04
'''
from hifive.api.base import RestApi


class HFHQListenSliceRequest(RestApi):
    def __init__(self, domain=None, port=80):
        domain = domain or 'hifive-gateway-test.hifiveai.com';
        RestApi.__init__(self, domain, port)
        self.clientId = None
        self.musicId = None
        self.audioFormat = None
        self.audioRate = None
        self.auditionBegin = None
        self.auditionEnd = None
        self.isMixed = None

    def getapiname(self):
        return 'TrafficHQListenSlice'
