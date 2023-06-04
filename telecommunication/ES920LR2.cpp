#include "ES920LR2.h"
#include <iostream>
#include <wiringPi.h>
#include <wiringSerial.h>
#include <cstring>

ES920LR2::ES920LR2()
{

}

void ES920LR2::begin()
{
  std::cout << "LoRa.begin()" << std::endl;
  for(int i=0;i<5;i++){
    delay(1000);
    std::cout << ".";
  }
  std::cout << std::endl;

  serialPort = serialOpen("/dev/serial0", 115200);
  if (serialPort < 0) {
    std::cerr << "Serial port initialization failed." << std::endl;
    return;
  }

  pinMode(LoRa_Rst, OUTPUT); // リセット用PINをOUTPUTに設定。
  digitalWrite(LoRa_Rst, HIGH);

  // Power ON
  pinMode(LoRa_power, OUTPUT); // スリープ割り込み用PINをOUTPUTに設定。
  digitalWrite(LoRa_power, HIGH); // スリープ割り込みピンをHIGHに設定
  delay(1000);

  // 無線からの情報を読み込み
  LoRa_reset();
  delay(1500);
  LoRa_recv(buf);
  std::cout << buf;
  std::cout << "LoRa start" << std::endl;
}

int ES920LR2::LoRa_recv(char *buf){
  /*
   * LoRaから受信。戻り値は受信文字数。
   */
  char *start = buf;
  int icount = 0;
  int itimeout = 0;

  while(true){
    delay(1);
    while(serialDataAvail(serialPort) > 0){
      *buf++ = serialGetchar(serialPort);
      if(icount>=2){
        if(*(buf-2) == '\r' && *(buf-1) == '\n'){
          *buf = '\0';
          return (buf-start);
        }
      }
      icount++;
      if(icount>=BUFF_SIZE-1){
        //std::cout << "受信文字数上限超過エラー LoRa_recv()" << std::endl;// 受信文字数上限超過エラー
        return -1;
      }
    }
    // timeout処理
    itimeout++;
    if(itimeout >10000){
      //std::cout << "LoRa_recve() timeout" << std::endl;
      return -2;
    }
  }
}

void ES920LR2::set_config(int in_bw, int in_sf){
  /*
   * LoRaの設定。帯域幅、拡散率、スリープモードを設定する
   */
  
  ///
  const char* configStr = "config\r\n";  // 文字列定数をconst char*に変更
  LoRa_send(const_cast<char*>(configStr));

  ///
  char buf[BUFF_SIZE];
  LoRa_send(const_cast<char*>("config\r\n"));
  delay(200);
  LoRa_reset();
  delay(1500);

  // LoRaから"Select Mode"を受信するまで待機
  while(true){
    LoRa_recv(buf);
    if(strstr(buf, "Mode")){
      std::cout << buf;
      break;
    }
  }

  // Modeはプロセッサモード:2を選択
  sendcmd(const_cast<char*>("2\r\n"));

  // 帯域幅設定
  sprintf(buf, "bw %d\r\n", in_bw);
  sendcmd(buf);
  // 拡散率設定
  sprintf(buf, "sf %d\r\n", in_sf);
  sendcmd(buf);
  // 動作モードをオペレーションモードに設定
  sendcmd(const_cast<char*>("q 2\r\n"));
  // EEPROMに設定をセーブ
  sendcmd(const_cast<char*>("w\r\n"));

  LoRa_reset();
  std::cout << "LoRa module setting finished" << std::endl;
  delay(1000);
}

int ES920LR2::LoRa_send(char *msg){
  /*
   * LoRaにコマンドを送信
   */
  char *start = msg;

  while(*msg != '\0'){
    serialPutchar(serialPort, *msg++);
  }
  return (msg - start);
}

bool ES920LR2::sendcmd(char *cmd){
  /*
   * LoRaにコマンドを送る
   */
  unsigned long t;
  char buf[BUFF_SIZE]; // コマンド送付後のデータ受信バッファ

  std::cout << cmd; // デバッグプリント
  LoRa_send(cmd); // データ送信

  //受信チェック
  while(true){
    LoRa_recv(buf);
    if(strstr(buf, "OK")){
      std::cout << buf; // デバッグプリント
      return true;
    }else if(strstr(buf, "NG")){
      std::cout << buf; // デバッグプリント
      return false;
    }
  }
}


void ES920LR2::LoRa_reset(){
  /*
   * LoRaをリセットする
   */
   std::cout << "LoRa_reset()" << std::endl; // デバッグプリント
   digitalWrite(LoRa_Rst, LOW);
   delay(100);
   digitalWrite(LoRa_Rst, HIGH);
}

void ES920LR2::debug(){
  // 通信のテスト
  std::cout << "send test" << std::endl;
  char ibuf[BUFF_SIZE];
  int res=0;

  LoRa_send(const_cast<char*>("send test\r\n"));

  while(true){
    LoRa_recv(ibuf);
    if(strstr(ibuf, "OK")){
      std::cout << ibuf;
      break;
    } else if(strstr(ibuf, "NG")){
      std::cout << ibuf;
      break;
    }
  }

  std::cout << "END";
}

