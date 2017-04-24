# -*- coding: utf-8 -*- 

from PIL import ImageGrab
import time
import os

if  __name__  == "__main__":
    path = "c:\\temp\\"
    try:
        os.mkdir(path)
    except:
        print(path)

    while 1:
        try:
            pic = ImageGrab.grab()
            timeTemp = time.time()
            timeTempNext = time.localtime(timeTemp)
            timeNow = time.strftime("%Y-%m-%d-%H-%M-%S", timeTempNext)
            
            savePath = path + timeNow + ".jpg"
            pic.save(savePath)
            time.sleep(60)
            print timeNow
        except:
            time.sleep(120)
