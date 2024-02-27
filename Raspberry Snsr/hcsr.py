import RPi.GPIO as gpio
from time import sleep
import time

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

trig=23
echo=24

gpio.setup(trig,gpio.OUT)
gpio.setup(echo,gpio.IN)


while True:
    gpio.output(trig,gpio.LOW)
    sleep(0.5)

    gpio.output(trig,gpio.HIGH)
    sleep(0.0001)
    gpio.output(trig,gpio.LOW)

    while gpio.input(echo)==0:
        start=time.time()

    while gpio.input(echo)==1:
        end=time.time()

    float ,sure=end-start

    uzaklık=sure/0.000058

    print("uzaklık:",uzaklık,"cm")
    