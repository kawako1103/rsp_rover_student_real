from gpiozero import Motor
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

# DCモータのピン設定
PIN_AIN1 = 18
PIN_AIN2 = 23
PIN_BIN1 = 24
PIN_BIN2 = 13

dcm_pins = {
    "left_forward": PIN_AIN2,
    "left_backward": PIN_AIN1,
    "right_forward": PIN_BIN2,
    "right_backward": PIN_BIN1,
}

def reset():
    #初期化"
    # 初期化
     factory = PiGPIOFactory()
     motor_left = Motor( forward=dcm_pins["left_forward"],
                         backward=dcm_pins["left_backward"],
                         pin_factory=factory)
     motor_right = Motor( forward=dcm_pins["right_forward"],
                         backward=dcm_pins["right_backward"],
                         pin_factory=factory)


def main():
    # 初期化
    factory = PiGPIOFactory()
    motor_left = Motor( forward=dcm_pins["left_forward"],
                        backward=dcm_pins["left_backward"],
                        pin_factory=factory)
    motor_right = Motor( forward=dcm_pins["right_forward"],
                        backward=dcm_pins["right_backward"],
                        pin_factory=factory)


    # 正回転 -> 停止 -> 逆回転 -> 停止
    try:
        # 最高速で正回転 - 1秒
        print("最高速で正回転 -  1秒")
        motor_left.value = 1.0
        motor_right.value = 1.0
        sleep(1)
        # 少し遅く正回転 - 1秒
        print("少し遅く正回転 - 2秒")
        motor_left.value = 0.75
        motor_right.value = 0.75
        sleep(2)
        # 遅く正回転 : 1秒
        print("遅く正回転 - 1秒")
        motor_left.value = 0.5
        motor_right.value = 0.5
        sleep(1)
        """" # 停止 - 1秒
        motor_left.value = 0.0
        motor_right.value = 0.0
        sleep(1)
        # 最高速で逆回転 - 1秒
        print("最高速で逆回転 - 1秒")
        motor_left.value = -1.0
        motor_right.value = -1.0
        sleep(1)
        # 少し遅く逆回転 - 1秒
        print("少し遅く逆回転 - 1秒")
        motor_left.value = -0.75
        motor_right.value = -0.75
        sleep(1)
        # 遅く逆回転 - 1秒
        print("遅く逆回転 - 1秒")
        motor_left.value = -0.50
        motor_right.value = -0.50
        sleep(1)
        """
        # 停止 - 1秒
        motor_left.value = 0.0
        motor_right.value = 0.0
        sleep(1)
    except KeyboardInterrupt:
        print("stop")
        # 停止
        motor_left.value = 0.0
        motor_right.value = 0.0

    return

if __name__ == "__main__":
    main()

def rotate():

    # 初期化
    factory = PiGPIOFactory()
    motor_left = Motor( forward=dcm_pins["left_forward"],
                        backward=dcm_pins["left_backward"],
                        pin_factory=factory)
    motor_right = Motor( forward=dcm_pins["right_forward"],
                        backward=dcm_pins["right_backward"],
                        pin_factory=factory)


   # 右5回転くらい  -> 停止
    try:
        # 最高速で正回転 - 1秒
        print("最高速で正回転 : 2秒")
        motor_left.value = 1.0
        motor_right.value = 1.0
        sleep(2)
        # 遅く正回転 - 1秒
        print("遅く正回転 : 2秒")
        motor_left.value = 0.5
        motor_right.value =-0.5
        sleep(2)
        #停止：2秒
        print("停止：2秒") 
        motor_left.value = 0
        motor_right.value=0
        sleep(2)
        """# 遅く逆回転 : 2秒
        print("遅く逆回転 : 2秒")
        motor_left.value = -0.5
        motor_right.value =--0.5
        sleep(2)
        #最高速度で逆回転：2秒
        print("最高速度で逆回転：2秒")
        motor_left.value=-1.0
        motor_right.value=-1.0
        sleep(2)
        # 停止 : 2
        print("停止：2秒")
        motor_left.value = 0.0
        motor_right.value = 0.0
        sleep(2)
        """
    except KeyboardInterrupt:
        print("stop")
        # 停止
        motor_left.value = 0.0
        motor_right.value = 0.0

    return
    
