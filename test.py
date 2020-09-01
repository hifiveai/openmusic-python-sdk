# -*- coding: utf-8 -*-
'''
Created on 2012-7-3

@author: lihao
'''
import top.api


appkey = '5216d02806d5464b943492838b7e4390'
secret = '2d241e8f934d47d5'
sessionkey = '6100210dd2cab1586a1a2d7c7a35c5b9102fbad0dab255f2270467557'
url = "https://hifive-openapi-qa.hifiveai.com"
port = 80


def hifiveHQListenRequestTest(url, port,appkey, secret):
    req = top.api.HifiveHQListenRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.musicId = "B7B810AABADF"
    req.audioFormat = "mp3"
    req.audioRate = "128"
    resp = req.getResponse()
    return resp;

def HifiveTrafficDownloadRequestTest(url, port,appkey, secret):
    req = top.api.HifiveTrafficDownloadRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.musicId = "B7B810AABADF"
    req.audioFormat = "mp3"
    req.audioRate = "128"
    resp = req.getResponse()
    return resp;

def HifiveTrafficTagMusicRequestTest(url, port,appkey, secret):
    req = top.api.HifiveTrafficTagMusicRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.tagId = "5440"
    resp = req.getResponse()
    return resp;

def HifiveTrafficSearchMusicRequestTest(url, port,appkey, secret):
    req = top.api.HifiveTrafficSearchMusicRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.keyword = "a"
    resp = req.getResponse()
    return resp;


def HifiveOrderSearchMusicRequestTest(url, port,appkey, secret):
    req = top.api.HifiveOrderSearchMusicRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.keyword = "a"
    resp = req.getResponse()
    return resp;

def HifiveTrafficListenMixedRequestTest(url, port,appkey, secret):
    req = top.api.HifiveTrafficListenMixedRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.musicId = "B7B810AABADF"
    req.audioFormat = "mp3"
    req.audioRate = "128"
    resp = req.getResponse()
    return resp;

def HifiveOrderListenMixedRequestTest(url, port,appkey, secret):
    req = top.api.HifiveOrderListenMixedRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.musicId = "B7B810AABADF"
    req.audioFormat = "mp3"
    req.audioRate = "128"
    resp = req.getResponse()
    return resp;

def HifiveTrafficListenSliceRequestTest(url, port,appkey, secret):
    req = top.api.HifiveTrafficListenSliceRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.musicId = "B7B810AABADF"
    req.audioFormat = "mp3"
    req.audioRate = "128"

    req.isMixed = "TRUE"
    req.auditionBegin = "2"
    req.auditionEnd = "100"
    resp = req.getResponse()
    return resp;


def HifiveOrderListenSliceRequestTest(url, port,appkey, secret):
    req = top.api.HifiveOrderListenSliceRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.musicId = "B7B810AABADF"
    req.audioFormat = "mp3"
    req.audioRate = "128"

    req.isMixed = "TRUE"
    req.auditionBegin = "2"
    req.auditionEnd = "100"
    resp = req.getResponse()
    return resp;

def HifiveTrafficListenRequestTest(url, port,appkey, secret):
    req = top.api.HifiveTrafficListenRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.musicId = "B7B810AABADF"
    req.audioFormat = "mp3"
    req.audioRate = "128"
    resp = req.getResponse()
    return resp;

def HifiveOrderListenRequestTest(url, port,appkey, secret):
    req = top.api.HifiveOrderListenRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.musicId = "B7B810AABADF"
    req.audioFormat = "mp3"
    req.audioRate = "128"
    resp = req.getResponse()
    return resp;


def HifiveOrderSheetMusicRequestTest(url, port,appkey, secret):
    req = top.api.HifiveOrderSheetMusicRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.sheetId = "1203"
    req.language = "1"
    resp = req.getResponse()
    return resp;

def HifiveTrafficSheetMusicRequestTest(url, port,appkey, secret):
    req = top.api.HifiveTrafficSheetMusicRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.sheetId = "1203"
    req.language = "1"
    resp = req.getResponse()
    return resp;

def HifiveOrderGroupSheetRequestTest(url, port,appkey, secret):
    req = top.api.HifiveOrderGroupSheetRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.groupId = "csa0t86qv24"
    req.language = "1"
    req.recoNum = "10"
    req.page="1"
    req.pageSize="10"
    resp = req.getResponse()
    return resp;

def HifiveTrafficGroupSheetRequestTest(url, port,appkey, secret):
    req = top.api.HifiveTrafficGroupSheetRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.groupId = "csa0t86qv24"
    req.language = "1"
    req.recoNum = "10"
    req.page="1"
    req.pageSize="10"
    resp = req.getResponse()
    return resp;

def HifiveOrderTagSheetRequestTest(url, port,appkey, secret):
    req = top.api.HifiveOrderTagSheetRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.recoNum = "2"
    resp = req.getResponse()
    return resp;

def HifiveTrafficTagSheetRequestTest(url, port,appkey, secret):
    req = top.api.HifiveTrafficTagSheetRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.recoNum = "2"
    resp = req.getResponse()
    return resp;

def HifiveOrderGroupRequestTest(url, port,appkey, secret):
    req = top.api.HifiveOrderGroupRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    resp = req.getResponse()
    return resp;

def HifiveTrafficGroupRequestTest(url, port,appkey, secret):
    req = top.api.HifiveTrafficGroupRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    resp = req.getResponse()
    return resp;

def HifiveTrafficTagRequestTest(url, port,appkey, secret):
    req = top.api.HifiveTrafficTagRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    resp = req.getResponse()
    return resp;

def HifiveOrderTagRequestTest(url, port,appkey, secret):
    req = top.api.HifiveOrderTagRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    resp = req.getResponse()
    return resp;

def HifiveOrderRefundRequestTest(url, port,appkey, secret):
    req = top.api.HifiveOrderRefundRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.orderId= "1434556569145"
    resp = req.getResponse()
    return resp;

try:
    resp = HifiveOrderRefundRequestTest(url,port,appkey,secret)
    print(resp)

except Exception as e:
    print(e)



