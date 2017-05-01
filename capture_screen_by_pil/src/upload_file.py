# -*- coding: utf-8 -*- 
# 仅支持Windows系统(x86,x64)
import urllib
import urllib2

__author__ = 'Administrator'
from poster.encode import multipart_encode
from poster.streaminghttp import  register_openers

register_openers()

def upload(fileName):
    # 通过百度开发者 API 上传文件到百度云

    baseurl = "https://pcs.baidu.com/rest/2.0/pcs/file?"
    args = {
        "method": "upload",
        "access_token": "0.a2834e35964a7b0704242wef160507c1.2592000.1386326697.1060338330-1668780",
        "path": "/apps/ResourceSharing/%s"%fileName
    }

    try:
        datagen, headers = multipart_encode({"file": open("c:\\temp\\%s"%fileName, "rb")})

        encodeargs = urllib.urlencode(args)
        url = baseurl + encodeargs
        print(url)

        request = urllib2.Request(url, datagen, headers)
        result = urllib2.urlopen(request).read()
        print(result)
    except:
        print(u"获得数据结果时发生异常!")

upload("1.txt")