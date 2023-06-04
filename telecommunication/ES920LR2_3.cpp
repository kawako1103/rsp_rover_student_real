//#include <iostream>
#include <pigpio.h>
#include <cstring>
#include <ctime>
#include <unistd.h>
#include "LoraCommunication.h"

#define GPS_DEVICE "/dev/serial0"
#define LORA_DEVICE "/dev/serial1"
#define BAUD_RATE 9600

// LoRaモジュールのピン番号
#define LoRa_Rst 14
#define LoRa_RX 13
#define LoRa_TX 12

/*
void LoRa_reset()
{
    gpioWrite(LoRa_Rst, 0);
    gpioDelay(100000);
    gpioWrite(LoRa_Rst, 1);
    gpioDelay(1500000);
}

void LoRa_send(int serialPort, const char msg)
{
    serialPrintf(serialPort, "%s", msg);
}

void LoRa_recv(int serialPort, charbuf, int bufSize)
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
            gpioDelay(10000);
        }
    }
    buf[index] = '\0';
}

void setLoRaMode(int serialPort, int bw, int sf)
{
    char buf[64];
    LoRa_send(serialPort, "config\r\n");
    gpioDelay(200000);
    LoRa_reset();
    gpioDelay(1500000);

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
    gpioDelay(1000000);
}
int main()
{
    if (gpioInitialise() < 0)
    {
        std::cerr << "Failed to initialize pigpio" << std::endl;
        return 1;
    }

    gpioSetMode(LoRa_Rst, PI_OUTPUT);

    int loraSerial = serialOpen(LORA_DEVICE, BAUD_RATE);

    if (loraSerial < 0)
    {
        std::cerr << "Failed to open serial port" << std::endl;
        gpioTerminate();
        return 1;
    }

    setLoRaMode(loraSerial, 3, 12); // LoRaモジュールのモードを設定（例: バンド幅3, スプレッドファクタ12）

    // Pythonから受け取ったGPSの値を代入
    const char *gpsData = "GPS_VALUE_HERE";

    // LoRaで送信
    LoRa_send(loraSerial, gpsData);

    while (true)
    {
        char loraRecv[64];

        // LoRaの受信待ち
        while (true)
        {
            LoRa_recv(loraSerial, loraRecv, sizeof(loraRecv));
            if (strstr(loraRecv
*/

void LoRa_send(int serialPort, const char* msg)
{
    //gpioSerialWrite(serialPort, msg, strlen(msg));
    gpioWrite(serilaPort, msg, strlen(msg));
}

int LoRa_recv(int serialPort, char* buf, int bufSize)
{
   

    if (bytesRead >= 0)
    {
        buf[bytesRead] = '\0';
    }
    return bytesRead;
}

void setLoRaMode(int serialPort, int bw, int sf)
{
    char buf[64];
    LoRa_send(serialPort, "config\r\n");
    time_sleep(0.2);
    LoRa_reset();
    time_sleep(1.5);

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
    time_sleep(1.0);
}

int main()
{
    if (gpioInitialise() < 0)
    {
        std::cerr << "Failed to initialize pigpio" << std::endl;
        return 1;
    }

    int loraSerial = gpioSerialReadOpen(14, 9600, 0); // GPIO 14 を使用してシリアルポートを開きます

    if (loraSerial < 0)
    {
        std::cerr << "Failed to open serial port" << std::endl;
        gpioTerminate();
        return 1;
    }

    setLoRaMode(loraSerial, 3, 12); // LoRaモジュールのモードを設定（例: バンド幅3, スプレッドファクタ12）

    const char* gpsData = "GPS_VALUE_HERE";

    LoRa_send(loraSerial, gpsData);

    while (true)
    {
        char loraRecv[64];

        while (true)
        {
            int bytesRead = LoRa_recv(loraSerial, loraRecv, sizeof(loraRecv));
            if (strstr(loraRecv, "OK"))
            {
                std::cout << "LoRa response: " << loraRecv << std::endl;
                break;
            }
            else if (bytesRead > 0)
            {
                std::cout << "Received data: " << loraRecv << std::endl;
            }
        }

        time_sleep(1.0);
    }

    gpioSerialReadClose(loraSerial);
    gpioTerminate();

    return 0;
}
