from gpiozero import LED,Button
led=LED(27)
button= Button(17)

button.when_activated=led.on
button.when_deactivated=led.off
while True:
    pass
        
        

    