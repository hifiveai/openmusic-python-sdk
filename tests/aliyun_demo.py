# -*- coding: utf-8 -*-
'''
Created on 2014-6-17

@author: lijie.ma
'''
import aliyun.api


appkey = '23571563'
secret = 'def8bf03f76c2373b17f0698c5e80c9d'
sessionkey = '6100210dd2cab1586a1a2d7c7a35c5b9102fbad0dab255f2270467557'
url = "http://gw.api.taobao.com/router/rest"
port = 80

'''
这边可以设置一个默认的accessKeyId和accessKeySecret，当然也可以不设置
注意：默认的只需要设置一次就可以了

'''
aliyun.setDefaultAppInfo(appkey, secret)

'''
使用自定义的域名和端口（测试沙箱环境使用）
a = aliyun.api.Rds20130528DescribeDBInstancesRequest("rds.aliyuncs.com",80)

使用自定义的域名（测试沙箱环境使用）
a = aliyun.api.Rds20130528DescribeDBInstancesRequest("rds.aliyuncs.com")

使用默认的配置（调用线上环境）
a = aliyun.api.Rds20130528DescribeDBInstancesRequest()

'''

a = aliyun.api.RestApi(url,port)

'''
可以在运行期替换掉默认的appkey和secret的设置
a.set_app_info(aliyun.appinfo("accessKeyId","accessKeySecret"))
'''
a.DBInstanceId = ""

try:
    print("begin");
    f= a.getResponse()
    print(f)
except Exception as e:
    print(e)
    
