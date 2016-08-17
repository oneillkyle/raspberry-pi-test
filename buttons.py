import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.IN)
GPIO.setup(21,GPIO.IN)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

try:
    while True:
        GPIO.output(12, not GPIO.input(18))
        GPIO.output(16, not GPIO.input(21))
except KeyboardInterrupt:
    GPIO.cleanup()
