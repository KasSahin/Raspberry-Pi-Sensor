import RPi.GPIO as gpio
from time import sleep

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

gpio.setup(27,gpio.OUT)
pwm_led=gpio.PWM(27,100)
pwm_led.start(0)

for i in range (0,101,10):
    pwm_led.ChangeDutyCycle(i)
    sleep(0.5)
gpio.cleanup()



 
