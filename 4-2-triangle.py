import RPi.GPIO as GPIO
import time

def dec2bin(a):
    return [int(digit) for digit in bin(a)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    value = int(input())

    while 1:
        for i in range(256):
            bin_val = dec2bin(i)
            GPIO.output(dac, bin_val)
            time.sleep(value / 512)

        for i in range(255, -1, -1):
            bin_val = dec2bin(i)
            GPIO.output(dac, bin_val)
            time.sleep(value / 512)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()