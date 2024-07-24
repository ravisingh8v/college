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

GPIO.setup(3, GPIO.IN) 

EN1 = GPIO.PWM(Motor1['EN'], 100) 
EN2 = GPIO.PWM(Motor2['EN'], 100)
EN1.start(0)
EN2.start(0)

try:
    while True:
        if GPIO.input(3) == True:
            print("No Object Detected")
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

        else:  
            print("Object Detected")
            for duty_cycle in range(40, 45):
                EN1.ChangeDutyCycle(duty_cycle)
                EN2.ChangeDutyCycle(duty_cycle)
                GPIO.output(Motor1['input1'], GPIO.LOW)
                GPIO.output(Motor1['input2'], GPIO.LOW)
                GPIO.output(Motor2['input1'], GPIO.LOW)
                GPIO.output(Motor2['input2'], GPIO.LOW)
                sleep(0.1)

            print("STOP")
            EN1.ChangeDutyCycle(0)
            EN2.ChangeDutyCycle(0)
            sleep(5)
        
except KeyboardInterrupt:
    pass

GPIO.cleanup()
