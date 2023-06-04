from digitalio import DigitalInOut, Direction
import board
import busio
import adafruit_rfm9x

# LoRa送信用のピンとSPIインターフェースを設定
cs = DigitalInOut(board.CE1)
reset = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# LoRaモジュールの設定
rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 433.0)
rfm9x.tx_power = 23

# LoRaデータを送信する関数
def send_lora_data(data):
    rfm9x.send(bytes(data, "utf-8"))

# GPSデータを読み取るシリアルポートを設定
gps_port = "/dev/serial0"  # UART接続の場合は通常 "/dev/serial0" を使用

# シリアルポートを開く
gps_serial = serial.Serial(gps_port, baudrate=9600, timeout=1)

while True:
    # GPSデータを読み取る
    gps_data = gps_serial.readline().decode("utf-8")

    # GPSデータを表示
    print(gps_data)

    # GPSデータをLoRa経由でPCに送信
    send_lora_data(gps_data)

