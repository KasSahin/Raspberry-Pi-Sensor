from gpiozero import PWMLED
from time import sleep

pwm_led=PWMLED(27) 

for i in range(0,101,10):
    pwm_led.value=float (f"0.{i}")
    sleep(0.5)