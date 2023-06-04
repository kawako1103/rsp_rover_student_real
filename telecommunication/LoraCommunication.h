#ifndef LORA_COMMUNICATION_H
#define LORA_COMMUNICATION_H

#include <iostream>

void LoRa_reset();
void LoRa_send(int, const char);
void LoRa_recv(int, char, int);
void setLoRaMode(int, int , int);

#endif // LORA_COMMUNICATION_H
