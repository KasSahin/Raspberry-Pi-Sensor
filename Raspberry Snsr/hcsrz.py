from gpiozero import DistanceSensor
from time import sleep

sensor=DistanceSensor(echo=23,trigger=24)

try:
    while True:
        distance=sensor.distance*200
        print("mesafe: ",round(distance,2),"cm")
        sleep(1)


except KeyboardInterrupt:
    pass