# Left Right Resulting Movement
# Forward Backward Turn Right
# Backward Forward Turn Left
# Forward Forward Go Straight
# Backward Backward Reverse

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Motor1 = {'EN': 25, 'input1': 24, 'input2': 23}
Motor2 = {'EN': 17, 'input1': 27, 'input2': 22}

for pin in Motor1.values():
    GPIO.setup(pin, GPIO.OUT)
for pin in Motor2.values():
    GPIO.setup(pin, GPIO.OUT)

EN1 = GPIO.PWM(Motor1['EN'], 100)  # channel=xx frequency=100Hz
EN2 = GPIO.PWM(Motor2['EN'], 100)
EN1.start(0)
EN2.start(0)

try:
    while True:
        # Forward Motion
        for duty_cycle in range(40, 45):
            print("FORWARD MOTION")
            EN1.ChangeDutyCycle(duty_cycle)
            EN2.ChangeDutyCycle(duty_cycle)
            GPIO.output(Motor1['input1'], GPIO.HIGH)
            GPIO.output(Motor1['input2'], GPIO.LOW)
            GPIO.output(Motor2['input1'], GPIO.HIGH)
            GPIO.output(Motor2['input2'], GPIO.LOW)
            sleep(0.1)

        print("STOP")
        EN1.ChangeDutyCycle(0)
        EN2.ChangeDutyCycle(0)
        sleep(5)

        # Left Turn
        print("LEFT TURN")
        left_speed = 10
        right_speed = 80
        EN1.ChangeDutyCycle(left_speed)
        EN2.ChangeDutyCycle(right_speed)
        GPIO.output(Motor1['input1'], GPIO.LOW)
        GPIO.output(Motor1['input2'], GPIO.HIGH)
        GPIO.output(Motor2['input1'], GPIO.HIGH)
        GPIO.output(Motor2['input2'], GPIO.LOW)
        sleep(1)

        # Right Turn
        print("RIGHT TURN")
        left_speed = 80
        right_speed = 10
        EN1.ChangeDutyCycle(left_speed)
        EN2.ChangeDutyCycle(right_speed)
        GPIO.output(Motor1['input1'], GPIO.HIGH)
        GPIO.output(Motor1['input2'], GPIO.LOW)
        GPIO.output(Motor2['input1'], GPIO.LOW)
        GPIO.output(Motor2['input2'], GPIO.HIGH)
        sleep(1)

        # Backward Motion
        for duty_cycle in range(40, 45):
            print("BACKWARD MOTION")
            EN1.ChangeDutyCycle(duty_cycle)
            EN2.ChangeDutyCycle(duty_cycle)
            GPIO.output(Motor1['input1'], GPIO.LOW)
            GPIO.output(Motor1['input2'], GPIO.HIGH)
            GPIO.output(Motor2['input1'], GPIO.LOW)
            GPIO.output(Motor2['input2'], GPIO.HIGH)
            sleep(0.1)

        print("STOP")
        EN1.ChangeDutyCycle(0)
        EN2.ChangeDutyCycle(0)
        sleep(5)
        
except KeyboardInterrupt:
    pass

GPIO.cleanup()
