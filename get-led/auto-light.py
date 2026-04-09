import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)
delitel = 6
GPIO.setup(delitel, GPIO.IN)


while True:
    state = GPIO.input(delitel)
    GPIO.output(led, not state)
    
    