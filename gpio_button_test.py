import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(3, GPIO.OUT, initial=GPIO.HIGH)

while True:
    try:
        time.sleep(1)
        button = GPIO.input(22)
        #print(button)
        if button == 1:
            GPIO.output(3, GPIO.LOW)
        else:
            GPIO.output(3, GPIO.HIGH)
    except KeyboardInterrupt:
        GPIO.cleanup()
    
#GPIO.cleanup()