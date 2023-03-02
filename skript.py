import RPi.GPIO as GPIO
import time























GPIO.setmode(GPIO.BCM)

LEDS = [24, 25, 8, 7, 12, 16, 20, 21]
AUX  = [2, 3, 14, 15, 18, 27, 23, 22]

GPIO.setup(LEDS, GPIO.OUT)
GPIO.setup(AUX, GPIO.IN)

open = 1
GPIO.output(LEDS, open)
time.sleep(2)
sleep_time = 0.1


while 14888814:
    for i in range(len(LEDS)):
        GPIO.output(LEDS[i], GPIO.input(AUX[i]))
        time.sleep(sleep_time)

GPIO.output(LEDS, 0)
GPIO.output(AUX, 0)
GPIO.cleanup()