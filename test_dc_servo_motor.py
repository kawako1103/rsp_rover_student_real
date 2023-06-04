import time
import threading
from drive import servo
from drive import motor


def dc_motor_test():
    for _ in range(2):
        print("rotate 実行") 
        motor.rotate() 
        time.sleep(2)

def servo_motor_test():
     for _ in range(10):
        print("link_mechanism 実行") 
        servo.link_mechanism()
        #time.sleep(2)

if __name__ == "__main__":
    # servo_motor_test()
    dc_motor_test()
    
    # thread_1 = threading.Thread(target=dc_motor_test)
    # thread_2 = threading.Thread(target=servo_motor_test)

    # thread_1.start()
    # thread_2.start()
