# -*- coding: utf-8 -*-
'''
Created on 2012-7-3

@author: lihao
'''
import hifive.api
from hifive.api import HFBitRateEnum, GenderEnum, EducationEnum
from hifive.api.rest import AreaEnum, PeriodEnum

appkey = 'ee45ca73bf1746428b2a942e017056df'
secret = 'cd231e0c8d314074b2'
token = '5a9a8a7b7a6c34b6cabbbace77808b67'
url = "https://hifive-gateway-test.hifiveai.com"
port = 80


def hifiveHQListenRequestTest(url, appkey, secret):
    req = hifive.api.HFHQListenRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.musicId = "B7B810AABADF"
    req.audioFormat = HFBitRateEnum.MP3_128.value[0]
    req.audioRate = HFBitRateEnum.MP3_128.value[1]
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveTrafficDownloadRequestTest(url, appkey, secret):
    req = hifive.api.HFTrafficDownloadRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.musicId = "B7B810AABADF"
    req.audioFormat = HFBitRateEnum.MP3_128.value[0]
    req.audioRate = HFBitRateEnum.MP3_128.value[1]
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveTrafficTagMusicRequestTest(url, appkey, secret):
    req = hifive.api.HFTrafficTagMusicRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.tagId = "5440"
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveOrderTagMusicRequestTest(url, appkey, secret):
    req = hifive.api.HFOrderTagMusicRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.tagId = "5440"
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveTrafficSearchMusicRequestTest(url, appkey, secret):
    req = hifive.api.HFTrafficSearchMusicRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.keyword = "a"
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveOrderSearchMusicRequestTest(url, appkey, secret):
    req = hifive.api.HFOrderSearchMusicRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.keyword = "a"
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveTrafficListenMixedRequestTest(url, appkey, secret):
    req = hifive.api.HFTrafficListenMixedRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.musicId = "B7B810AABADF"
    req.audioFormat = HFBitRateEnum.MP3_128.value[0]
    req.audioRate = HFBitRateEnum.MP3_128.value[1]
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveOrderListenMixedRequestTest(url, appkey, secret):
    req = hifive.api.HFOrderListenMixedRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.musicId = "B7B810AABADF"
    req.audioFormat = HFBitRateEnum.MP3_128.value[0]
    req.audioRate = HFBitRateEnum.MP3_128.value[1]
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveTrafficListenSliceRequestTest(url, appkey, secret):
    req = hifive.api.HFTrafficListenSliceRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.musicId = "B7B810AABADF"
    req.audioFormat = HFBitRateEnum.MP3_128.value[0]
    req.audioRate = HFBitRateEnum.MP3_128.value[1]

    req.isMixed = "TRUE"
    req.auditionBegin = "2"
    req.auditionEnd = "100"
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveOrderListenSliceRequestTest(url, appkey, secret):
    req = hifive.api.HFOrderListenSliceRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.musicId = "B7B810AABADF"
    req.audioFormat = HFBitRateEnum.MP3_128.value[0]
    req.audioRate = HFBitRateEnum.MP3_128.value[1]

    req.isMixed = "TRUE"
    req.auditionBegin = "2"
    req.auditionEnd = "100"
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveTrafficListenRequestTest(url, appkey, secret):
    req = hifive.api.HFTrafficListenRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.musicId = "B7B810AABADF"
    req.audioFormat = HFBitRateEnum.MP3_128.value[0]
    req.audioRate = HFBitRateEnum.MP3_128.value[1]
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveOrderListenRequestTest(url, appkey, secret):
    req = hifive.api.HFOrderListenRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.musicId = "B7B810AABADF"
    req.audioFormat = HFBitRateEnum.MP3_128.value[0]
    req.audioRate = HFBitRateEnum.MP3_128.value[1]
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveOrderSheetMusicRequestTest(url, appkey, secret):
    req = hifive.api.HFOrderSheetMusicRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.sheetId = "1203"
    req.language = "1"
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveTrafficSheetMusicRequestTest(url, appkey, secret):
    req = hifive.api.HFTrafficSheetMusicRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.sheetId = "1203"
    req.language = "1"
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveOrderGroupSheetRequestTest(url, appkey, secret):
    req = hifive.api.HFOrderGroupSheetRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.groupId = "csa0t86qv24"
    req.language = "1"
    req.recoNum = "10"
    req.page = "1"
    req.pageSize = "10"
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveTrafficGroupSheetRequestTest(url, appkey, secret):
    req = hifive.api.HFTrafficGroupSheetRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.groupId = "csa0t86qv24"
    req.language = "1"
    req.recoNum = "10"
    req.page = "1"
    req.pageSize = "10"
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveOrderTagSheetRequestTest(url, appkey, secret):
    req = hifive.api.HFOrderTagSheetRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.recoNum = "2"
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveTrafficTagSheetRequestTest(url, appkey, secret):
    req = hifive.api.HFTrafficTagSheetRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.recoNum = "2"
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveOrderGroupRequestTest(url, appkey, secret):
    req = hifive.api.HFOrderGroupRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveTrafficGroupRequestTest(url, appkey, secret):
    req = hifive.api.HFTrafficGroupRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveTrafficTagRequestTest(url, appkey, secret):
    req = hifive.api.HFTrafficTagRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveOrderTagRequestTest(url, appkey, secret):
    req = hifive.api.HFOrderTagRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveOrderRefundRequestTest(url, appkey, secret):
    req = hifive.api.HFOrderRefundRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.orderId = "1434556569145"
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveOrderDetailRequestTest(url, appkey, secret):
    req = hifive.api.HFOrderDetailRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.orderId = "1434556569145"
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveOrderPublishRequestTest(url, appkey, secret):
    req = hifive.api.HFOrderPublishRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.orderId = "1434556569145"
    req.workId = "uEC00xeWbExGNilHpSN7MoM3AalWqwUp1"
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveOrderMusicRequestTest(url, appkey, secret):
    req = hifive.api.HFOrderMusicRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.orderId = "143455656914512"
    req.workId = "uEC00xeWbExGNilHpSN7MoM3AalWqwUp1"
    req.subject = "nYyple"
    req.music = "[{\"versionId\":\"B7B810AABADF\",\"price\":20,\"num\":1}]"
    req.totalFee = "1556"
    req.deadline = "50"
    req.language = "1"
    req.audioFormat = HFBitRateEnum.AAC_320.value[0]
    req.audioRate = HFBitRateEnum.AAC_320.value[1]

    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveHQListenSliceRequestTest(url, appkey, secret):
    req = hifive.api.HFHQListenSliceRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.musicId = "B7B810AABADF"
    req.audioFormat = HFBitRateEnum.MP3_128.value[0]
    req.audioRate = HFBitRateEnum.MP3_128.value[1]

    req.isMixed = "TRUE"
    req.auditionBegin = "2"
    req.auditionEnd = "100"
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveChannelSheetRequestTest(url, appkey, secret):
    req = hifive.api.HFChannelSheetRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.groupId = "csa0t86qv24"
    req.recoNum = "10"
    req.language = "1"

    req.Page = "1"
    req.PageSize = "10"

    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveChannelRequestTest(url, appkey, secret):
    req = hifive.api.HFChannelRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"

    resp = req.getResponse()
    print(resp)
    return resp;


def HifiveOrderAuthorizationRequestTest(url, appkey, secret):
    req = hifive.api.HFOrderAuthorizationRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.companyName = "嗨翻屋d1g"
    req.projectName = "小嗨nbdb"
    req.brand = "HIFIVE音乐开放平台"
    req.period = PeriodEnum.TOW_YEAR.value
    req.area = AreaEnum.ZH.value
    req.orderIds = "14345565691451"

    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveSheetMusicRequestTest(url, appkey, secret):
    req = hifive.api.HFSheetMusicRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.sheetId = "1203"

    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveTagSheetRequestTest(url, appkey, secret):
    req = hifive.api.HFTagSheetRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.recoNum = "10"

    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveSheetTagRequestTest(url, appkey, secret):
    req = hifive.api.HFSheetTagRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"

    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveSearchMusicRequestTest(url, appkey, secret):
    req = hifive.api.HFSearchMusicRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.priceFromCent = "1"
    req.priceToCent = "100000"
    req.page = "1"
    req.pageSize = "20"

    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveMusicConfigRequestTest(url, appkey, secret):
    req = hifive.api.HFMusicConfigRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"

    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveBaseWeatherRequestTest(url, appkey, secret):
    req = hifive.api.HFBaseWeatherRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.location = "30.779164,103.94547"

    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveBaseVisualRequestTest(url, appkey, secret):
    req = hifive.api.HFBaseVisualRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.location = "30.779164,103.94547"

    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveHotRequestTest(url, appkey, secret):
    req = hifive.api.HFBaseHotRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.duration = "183"
    req.startTime = "1594639058"
    req.page = "1"
    req.pageSize = "20"
    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveBaseFavoriteRequestTest(url, appkey, secret, token):
    req = hifive.api.HFBaseFavoriteRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret, token))
    req.clientId = "1223234343"
    req.page = "1"
    req.pageSize = "20"

    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveBaseReportRequestTest(url, appkey, secret, token):
    req = hifive.api.HFBaseReportRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret, token))
    req.clientId = "1223234343"
    req.action = "1009"
    req.targetId = "B75C80A41E3A"

    resp = req.getResponse()
    print(resp)
    return resp;


def hifiveBaseLoginRequestTest(url, appkey, secret):
    req = hifive.api.HFBaseLoginRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "1223234343"
    req.nickname = "黄达"
    req.gender = GenderEnum.MAN.value
    req.birthday = "202012121"
    req.location = "30.779164,103.94547"
    req.education = EducationEnum.MASTER.value
    req.profession = "8"
    req.isOrganization = "true"
    req.favoriteSinger = "周杰伦"
    req.favoriteGenre = "1"

    resp = req.getResponse()
    print(resp)
    return resp;


def HFTrialRequest(url, appkey, secret):
    req = hifive.api.HFTrialRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "HOomxI+g0HvxGKofmUVsnw==";
    req.musicId = "1D652150715";

    resp = req.getResponse()
    print(resp)
    return resp;


def HFKHQListenRequest(url, appkey, secret):
    req = hifive.api.HFKHQListenRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "HOomxI+g0HvxGKofmUVsnw==";
    req.musicId = "1D652150715";

    resp = req.getResponse()
    print(resp)
    return resp;


def HFKReportListenRequest(url, appkey, secret):
    req = hifive.api.HFKReportListenRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "HOomxI+g0HvxGKofmUVsnw==";
    req.musicId = "1D652150715";
    req.duration = "2"
    req.timestamp = "1618564947000"

    resp = req.getResponse()
    print(resp)
    return resp;


def HFKTrialRequest(url, appkey, secret):
    req = hifive.api.HFKTrialRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "HOomxI+g0HvxGKofmUVsnw==";
    req.musicId = "1D652150715";
    req.duration = "2"
    req.timestamp = "1618564947000"

    resp = req.getResponse()
    print(resp)
    return resp;


def HFUGCHQListenRequest(url, appkey, secret):
    req = hifive.api.HFUGCHQListenRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "HOomxI+g0HvxGKofmUVsnw=="
    req.musicId = "1D652150715"

    resp = req.getResponse()
    print(resp)
    return resp;


def HFUGCTrialRequest(url, appkey, secret):
    req = hifive.api.HFUGCTrialRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "HOomxI+g0HvxGKofmUVsnw=="
    req.musicId = "1D652150715"

    resp = req.getResponse()
    print(resp)
    return resp;

def HFUGCReportListenRequest(url, appkey, secret):
    req = hifive.api.HFUGCReportListenRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "HOomxI+g0HvxGKofmUVsnw=="
    req.musicId = "1D652150715"

    resp = req.getResponse()
    print(resp)
    return resp;

def HFAuthorizeMusicRequest(url, appkey, secret):
    req = hifive.api.HFAuthorizeMusicRequest(url)
    req.set_app_info(hifive.appinfo(appkey, secret))
    req.clientId = "HOomxI+g0HvxGKofmUVsnw=="
    req.page = "1"
    req.pageSize = "20"

    resp = req.getResponse()
    print(resp)
    return resp;


try:
    resp = HFAuthorizeMusicRequest(url, appkey, secret)

except Exception as e:
    print(e)
