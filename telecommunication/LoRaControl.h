#ifndef LORA_CONTROL_H
#define LORA_CONTROL_H

#include <wiringPi.h>
#include <wiringSerial.h>
#include <cstring>
#include <iostream>
#include <unistd.h>

#define GPS_DEVICE "/dev/serial0"
#define LORA_DEVICE "/dev/serial1"
#define BAUD_RATE 9600

#define LoRa_Rst 14
#define LoRa_RX 13
#define LoRa_TX 12

void LoRa_reset();
void LoRa_send(int serialPort, const char* msg);
void LoRa_recv(int serialPort, char* buf, int bufSize);
void setLoRaMode(int serialPort, int bw, int sf);

#endif
