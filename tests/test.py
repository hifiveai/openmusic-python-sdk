# -*- coding: utf-8 -*-
'''
Created on 2012-7-3

@author: lihao
'''
import hifive.api
from hifive.api import HFBitRateEnum, GenderEnum, EducationEnum
from hifive.api.rest import AreaEnum, PeriodEnum

appkey = '5216d02806d5464b943492838b7e4390'
secret = '2d241e8f934d47d5'
token = '5a9a8a7b7a6c34b6cabbbace77808b67'
url = "https://hifive-openapi-qa.hifiveai.com"
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


try:
   # resp = hifiveBaseLoginRequestTest(url, appkey, secret)
    resp = hifiveBaseReportRequestTest(url, appkey, secret,'55c82cd073e8f87e0f298ad5719768d2')
    resp = hifiveBaseFavoriteRequestTest(url, appkey, secret,'55c82cd073e8f87e0f298ad5719768d2')
    resp = hifiveHotRequestTest(url, appkey, secret)
    resp = hifiveBaseVisualRequestTest(url, appkey, secret)

    resp = hifiveBaseWeatherRequestTest(url, appkey, secret)
    resp = hifiveMusicConfigRequestTest(url, appkey, secret)
    resp = hifiveSearchMusicRequestTest(url, appkey, secret)
    resp = hifiveSheetTagRequestTest(url, appkey, secret)

    resp = hifiveTagSheetRequestTest(url, appkey, secret)
    resp = hifiveSheetMusicRequestTest(url, appkey, secret)
    resp = HifiveOrderAuthorizationRequestTest(url, appkey, secret)
    resp = hifiveChannelRequestTest(url, appkey, secret)

    resp = hifiveChannelSheetRequestTest(url, appkey, secret)
    resp = hifiveHQListenSliceRequestTest(url, appkey, secret)
    resp = hifiveOrderMusicRequestTest(url, appkey, secret)
    resp = hifiveOrderPublishRequestTest(url, appkey, secret)


    resp = hifiveOrderDetailRequestTest(url, appkey, secret)
    resp = hifiveOrderRefundRequestTest(url, appkey, secret)
    resp = hifiveOrderTagRequestTest(url, appkey, secret)
    resp = hifiveTrafficTagRequestTest(url, appkey, secret)

    resp = hifiveTrafficGroupRequestTest(url, appkey, secret)
    resp = hifiveOrderGroupRequestTest(url, appkey, secret)
    resp = hifiveTrafficTagSheetRequestTest(url, appkey, secret)
    resp = hifiveOrderTagSheetRequestTest(url, appkey, secret)

    resp = hifiveTrafficGroupSheetRequestTest(url, appkey, secret)
    resp = hifiveOrderGroupSheetRequestTest(url, appkey, secret)
    resp = hifiveTrafficSheetMusicRequestTest(url, appkey, secret)
    resp = hifiveOrderSheetMusicRequestTest(url, appkey, secret)

    resp = hifiveOrderListenRequestTest(url, appkey, secret)
    resp = hifiveTrafficListenRequestTest(url, appkey, secret)
    resp = hifiveOrderListenSliceRequestTest(url, appkey, secret)
    resp = hifiveTrafficListenSliceRequestTest(url, appkey, secret)


    resp = hifiveOrderListenMixedRequestTest(url, appkey, secret)
    resp = hifiveTrafficListenMixedRequestTest(url, appkey, secret)
    resp = hifiveOrderSearchMusicRequestTest(url, appkey, secret)
    resp = hifiveTrafficSearchMusicRequestTest(url, appkey, secret)

    resp = hifiveOrderTagMusicRequestTest(url, appkey, secret)
    resp = hifiveTrafficTagMusicRequestTest(url, appkey, secret)
    resp = hifiveTrafficDownloadRequestTest(url, appkey, secret)
    resp = hifiveHQListenRequestTest(url, appkey, secret)

except Exception as e:
    print(e)
