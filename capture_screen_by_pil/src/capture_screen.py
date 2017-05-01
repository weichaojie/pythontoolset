# -*- coding: utf-8 -*- 
# 仅支持Windows系统(x86,x64)
from PIL import ImageGrab  # 用于截图并生成文件
import time  # 以时间字符串作为文件名称
import os,os.path,datetime
from itertools import izip
import Image
import urllib
import urllib2

__author__ = 'Administrator'
from poster.encode import multipart_encode
from poster.streaminghttp import  register_openers

register_openers()

def upload(fileName):
    # 通过百度开发者 API 上传文件到百度云
    datagen, headers = multipart_encode({"file": open("E:\\PHPTest\\Test1\\%s"%fileName, "rb")})
    baseurl = "https://pcs.baidu.com/rest/2.0/pcs/file?"
    args = {
        "method": "upload",
        "access_token": "0.a2834e35964a7b0704242wef160507c1.2592000.1386326697.1060338330-1668780",
        "path": "/apps/ResourceSharing/%s"%fileName
    }
    encodeargs = urllib.urlencode(args)
    url = baseurl + encodeargs
    print(url)
    request = urllib2.Request(url, datagen, headers)
    result = urllib2.urlopen(request).read()
    print(result)

# 计算两个文件的差异率，差异率越高表明图片内容的差异越大
def calc_difference_rate(left_image, right_image):
    try:
        i1 = Image.open(left_image)
        i2 = Image.open(right_image)
        assert i1.mode == i2.mode, "Different kind of images."
        assert i1.size == i2.size, "Different size."
    except:
        print(u"calc_difference_rate 打开文件发生异常！")
        
    pairs = izip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
        dif = sum(abs(p1-p2) for p1, p2 in pairs)
    else:
        dif = sum(abs(c1-c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))
        ncomponetns = i1.size[0] * i1.size[1]*3
    Difference = (dif / 255.0 *100)/ncomponetns
    print u"差异率为: ", Difference
    return Difference

# 按文件的创建时间为关键字,查找一个当前最新的文件,若没有文件则返回空的路径
def get_prvious_file_path(base_dir):
    l = os.listdir(base_dir)

    if len(l) == 0:
        return "";
    try:
        l.sort(key = lambda fn: os.path.getmtime(base_dir + fn) if not os.path.isdir(base_dir + fn) else 0)
    except:
        print(u"get_prvious_file_path 对文件目录以时间排序发生异常")

    if len(l) > 0:
        return l[-1]

if  __name__  == "__main__":
    temp_path = "c:\\temp\\"
    try:
        os.mkdir(temp_path)
    except:
        print(temp_path)

    while 1: # 循环执行截图
        try:
            pre_file_path = get_prvious_file_path(temp_path)
            print (u"前一个文件的全路径为:")
            print(pre_file_path)
            timeTemp = time.time()  # 1970年之后经过的浮点描述，得到时间戳
            timeTempNext = time.localtime(timeTemp) # 将一个时间戳转换成一个当前时区的struct_time
            timeNow = time.strftime("%Y-%m-%d %H-%M-%S", timeTempNext) # 根据指定的格式化字符串输出
            
            savePath = temp_path + timeNow + ".jpg" # 拼成图片的文件路径
            print(savePath)
            pic = ImageGrab.grab() # 全屏截图
            pic.save(savePath) # 保存图片
            print timeNow
            difference = 0.0
            
            if pre_file_path == "":
                print(u"没有文件可以比较")
            else:
                difference = calc_difference_rate(temp_path + "\\" + pre_file_path, savePath)
                
            if difference < 0.002 and pre_file_path <> "":
                os.remove(savePath)
                print(u"文件基本无变化，删除最近保存的一个文件")
            else:
                print(u"差异率较大，保存新的文件")
                
            time.sleep(30) # sleep函数的参数是秒
        except:
            time.sleep(60)