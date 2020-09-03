# -*- coding: utf-8 -*-
'''
Created on 2012-7-3

@author: lihao
'''
import top.api


appkey = '5216d02806d5464b943492838b7e4390'
secret = '2d241e8f934d47d5'
token = '5a9a8a7b7a6c34b6cabbbace77808b67'
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

def HifiveOrderDetailRequestTest(url, port,appkey, secret):
    req = top.api.HifiveOrderDetailRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.orderId= "1434556569145"
    resp = req.getResponse()
    return resp;

def HifiveOrderPublishRequestTest(url, port,appkey, secret):
    req = top.api.HifiveOrderPublishRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.orderId= "1434556569145"
    req.workId= "uEC00xeWbExGNilHpSN7MoM3AalWqwUp1"
    resp = req.getResponse()
    return resp;

def HifiveOrderMusicRequestTest(url, port,appkey, secret):
    req = top.api.HifiveOrderMusicRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.orderId= "143455656914512"
    req.workId= "uEC00xeWbExGNilHpSN7MoM3AalWqwUp1"
    req.subject= "nYyple"
    req.music= "[{\"versionId\":\"B7B810AABADF\",\"price\":20,\"num\":1}]"
    req.totalFee ="1556"
    req.deadline ="50"
    req.language ="1"
    req.audioFormat="mp3"
    req.audioRate="320"

    resp = req.getResponse()
    return resp;


def HifiveHQListenSliceRequestTest(url, port,appkey, secret):
    req = top.api.HifiveHQListenSliceRequest(url, port)
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

def HifiveChannelSheetRequestTest(url, port,appkey, secret):
    req = top.api.HifiveChannelSheetRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.groupId = "csa0t86qv24"
    req.recoNum = "10"
    req.language = "1"

    req.Page = "1"
    req.PageSize = "10"

    resp = req.getResponse()
    return resp;


def HifiveChannelRequestTest(url, port,appkey, secret):
    req = top.api.HifiveChannelRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"

    resp = req.getResponse()
    return resp;

def HifiveAuthorizationRequestTest(url, port,appkey, secret):
    req = top.api.HifiveAuthorizationRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.companyName= "嗨翻屋d1g"
    req.projectName= "小嗨nbdb"
    req.brand= "HIFIVE音乐开放平台"
    req.period= "3"
    req.area= "2"
    req.orderIds= "14345565691451"

    resp = req.getResponse()
    return resp;

def HifiveSheetMusicRequestTest(url, port,appkey, secret):
    req = top.api.HifiveSheetMusicRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.sheetId= "1203"


    resp = req.getResponse()
    return resp;


def HifiveTagSheetRequestTest(url, port,appkey, secret):
    req = top.api.HifiveTagSheetRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.recoNum= "10"


    resp = req.getResponse()
    return resp;

def HifiveSheetTagRequestTest(url, port,appkey, secret):
    req = top.api.HifiveSheetTagRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"


    resp = req.getResponse()
    return resp;


def HifiveSearchMusicRequestTest(url, port,appkey, secret):
    req = top.api.HifiveSearchMusicRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.price = "1-100000"
    req.Page = "1"
    req.PageSize = "20"


    resp = req.getResponse()
    return resp;



def HifiveMusicConfigRequestTest(url, port,appkey, secret):
    req = top.api.HifiveMusicConfigRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"


    resp = req.getResponse()
    return resp;


def HifiveBaseWeatherRequestTest(url, port,appkey, secret):
    req = top.api.HifiveBaseWeatherRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.location= "30.779164,103.94547"

    resp = req.getResponse()
    return resp;


def HifiveBaseVisualRequestTest(url, port,appkey, secret):
    req = top.api.HifiveBaseVisualRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.location= "30.779164,103.94547"

    resp = req.getResponse()
    return resp;

def HifiveHotRequestTest(url, port,appkey, secret):
    req = top.api.HifiveHotRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.Duration= "183"
    req.StartTime= "1594639058"
    req.Page= "1"
    req.PageSize= "20"
    resp = req.getResponse()
    return resp;

def HifiveBaseFavoriteRequestTest(url, port,appkey, secret,token):
    req = top.api.HifiveBaseFavoriteRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret,token))
    req.clientId= "1223234343"
    req.page="1"
    req.pageSize="20"

    resp = req.getResponse()
    return resp;


def HifiveBehaviorRequestTest(url, port,appkey, secret,token):
    req = top.api.HifiveBehaviorRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret,token))
    req.clientId= "1223234343"
    req.Action="1009"
    req.TargetId="B75C80A41E3A"

    resp = req.getResponse()
    return resp;


def HifiveUserGetRequestTest(url, port,appkey, secret):
    req = top.api.HifiveUserGetRequest(url, port)
    req.set_app_info(top.appinfo(appkey, secret))
    req.clientId= "1223234343"
    req.nickname = "黄达"
    req.gender = "1"
    req.birthday = "202012121"
    req.location = "30.779164,103.94547"
    req.education = "2"
    req.profession = "8"
    req.isOrganization = "true"
    req.favoriteSinger = "周杰伦"
    req.favoriteGenre = "1"

    resp = req.getResponse()
    return resp;


try:
    resp = HifiveTrafficGroupSheetRequestTest(url,port,appkey,secret)
    print(resp)

except Exception as e:
    print(e)


