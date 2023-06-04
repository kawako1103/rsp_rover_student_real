#include "LoRaControl.h"

#define GPS_DEVICE "/dev/serial0"
#define LORA_DEVICE "/dev/serial1"
#define BAUD_RATE 9600

// LoRaモジュールのピン番号
#define LoRa_Rst 14
#define LoRa_RX 13
#define LoRa_TX 12

void LoRa_reset()
{
    digitalWrite(LoRa_Rst, LOW);
    delay(100);
    digitalWrite(LoRa_Rst, HIGH);
    delay(1500);
}

void LoRa_send(int serialPort, const char msg)
{
    serialPrintf(serialPort, "%s", msg);
}

void LoRa_recv(int serialPort, char* buf, int bufSize)
{
    int index = 0;
    while (index < bufSize - 1)
    {
        if (serialDataAvail(serialPort))
        {
            char c = serialGetchar(serialPort);
            buf[index++] = c;
            if (c == '\n')
                break;
        }
        else
        {
            delay(10);
        }
    }
    buf[index] = '\0';
}

void setLoRaMode(int serialPort, int bw, int sf)
{
    char buf[64];
    LoRa_send(serialPort, "config\r\n");
    delay(200);
    LoRa_reset();
    delay(1500);

    while (true)
    {
        LoRa_recv(serialPort, buf, sizeof(buf));
        if (strstr(buf, "Mode"))
        {
            std::cout << buf << std::endl;
            break;
        }
    }

    sprintf(buf, "bw %d\r\n", bw);
    LoRa_send(serialPort, buf);
    sprintf(buf, "sf %d\r\n", sf);
    LoRa_send(serialPort, buf);
    LoRa_send(serialPort, "q 2\r\n");
    LoRa_send(serialPort, "w\r\n");

    LoRa_reset();
    std::cout << "LoRa module set to new mode" << std::endl;
    delay(1000);
}

int main()
{
    wiringPiSetup();
    pinMode(LoRa_Rst, OUTPUT);

    int gpsSerial = serialOpen(GPS_DEVICE, BAUD_RATE);
    int loraSerial = serialOpen(LORA_DEVICE, BAUD_RATE);

    if (gpsSerial < 0 || loraSerial < 0)
    {
        std::cerr << "Failed to open serial ports" << std::endl;
        return 1;
    }
setLoRaMode(loraSerial, 3, 12); // LoRaモジュールのモードを設定（例: バンド幅3, スプレッドファクタ12）

    while (true)
    {
        char gpsData[128];
        char loraRecv[64];

        // GPSデータの受信
        if (serialDataAvail(gpsSerial))
        {
            char c = serialGetchar(gpsSerial);
            if (c == '\n')
            {
                gpsData[strlen(gpsData) - 1] = '\0'; // 改行文字を除去
                std::cout << "Received GPS data: " << gpsData << std::endl;

                // LoRaで送信
                LoRa_send(loraSerial, gpsData);

                // LoRaの受信待ち
                while (true)
                {
                    LoRa_recv(loraSerial, loraRecv, sizeof(loraRecv));
                    if (strstr(loraRecv, "OK"))
                    {
                        std::cout << "LoRa response: " << loraRecv << std::endl;
                        break;
                    }
                    else if (strstr(loraRecv, "NG"))
                    {
                        std::cout << "LoRa response: " << loraRecv << std::endl;
                        break;
                    }
                }

                memset(gpsData, 0, sizeof(gpsData));
            }
            else
            {
                strncat(gpsData, &c, 1);
            }
        }

        // 1秒待機
        usleep(1000000);
    }

    return 0;
}
