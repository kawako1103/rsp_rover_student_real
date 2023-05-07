import picamera
import time
import datetime
 #wifi接続がない場合は、接続があった時に電源をOFFにした時から時間が再開されるが、大体開始からどのタイミングで得られた写真なのかを比較的容易に判別できるように（枚数かけるインターバル秒でもいいが面倒な気がするので）という意味でimportしてます

dirName  = '/home/rsp/Pictures/'
camera = picamera.PiCamera()

camera.start_preview()
time.sleep(3)


for i in range(5):
    nowTime  = datetime.datetime.now()
    fileName = nowTime.strftime('%Y%m%d-%H%M%S') + '.jpg'
    camera.capture(dirName + fileName)
    time.sleep(10) 

camera.stop_preview() 
