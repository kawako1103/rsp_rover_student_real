import time
import serial
from micropyGPS import MicropyGPS

def get_gps():#呼び出したら緯度(latitude)、経度(longitude)を得る
    # シリアル通信設定
    uart = serial.Serial('/dev/ttyUSB0', 9600, timeout = 10)
    # gps設定
    my_gps = MicropyGPS(9, 'dd')

    # 5秒ごとに表示
    tm_last = 0
    sentence = uart.readline()
    if len(sentence) > 0:
        for x in sentence:
            if 10 <= x <= 126:
                stat = my_gps.update(chr(x))
                if stat:
                    tm = my_gps.timestamp
                    tm_now = (tm[0] * 3600) + (tm[1] * 60) + int(tm[2])
                    if (tm_now - tm_last) >= 5:
                        return my_gps.latitude[0], my_gps.longitude[0]
