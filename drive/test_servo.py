import pigpio
import time

SERVO_PIN = 19

pi = pigpio.pi()

while True:

    pi.set_servo_pulsewidth( SERVO_PIN, 1000 )
    time.sleep(0.2)

    #pi.set_servo_pulsewidth( SERVO_PIN, 500  )
    #time.sleep( 1 )

    pi.set_servo_pulsewidth( SERVO_PIN, 1500 )
    time.sleep(1)

    pi.set_servo_pulsewidth( SERVO_PIN, 2000 )
    time.sleep(0.2)

    pi.set_servo_pulsewidth( SERVO_PIN, 1500 )
    time.sleep(1)
    #pi.set_servo_pulsewidth( SERVO_PIN, 1000 )
    #time.sleep( 1 )

    #pi.set_servo_pulsewidth( SERVO_PIN, 1500 )
    #time.sleep( 1 )

    #pi.set_servo_pulsewidth( SERVO_PIN, 2000 )
    #time.sleep( 1 )

    #pi.set_servo_pulsewidth( SERVO_PIN, 2500 )
    #time.sleep(1)
