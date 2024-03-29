'''
Created by yong.huang on 2016.11.04
'''
from hifive.api.base import RestApi


class HFSearchMusicRequest(RestApi):
    def __init__(self, domain=None, port=80, method=None):
        domain = domain or 'hifive-gateway-test.hifiveai.com';
        method = method or 'POST';
        RestApi.__init__(self, domain, port, method)
        self.clientId = None
        self.keyword = None
        self.language = None
        self.priceToCent = None
        self.priceFromCent = None
        self.bpmTo = None
        self.bpmFrom = None
        self.durationTo = None
        self.durationFrom = None
        self.tagIds = None
        self.duration = None
        self.page = None
        self.pageSize = None
        self.levels = None

    def getapiname(self):
        return 'SearchMusic'
