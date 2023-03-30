import RPi.GPIO as GPIO
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp   = 4
troyka = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)


def dac2bin(a):
    return [int(digit) for digit in bin(a)[2:].zfill(8)]

def adc():
    binary_val = 0
    for i in range(7, -1, -1):
        binary_val += 2**(i)
        GPIO.output(dac, dac2bin(binary_val))
        time.sleep(0.005)
        if GPIO.input(comp) == 0:
            binary_val -= 2**(i)
    return binary_val


try:
    while 88005553535:
        get_value = adc()
        if get_value:
            print(get_value, '{:.2f}v'.format(3.3 * get_value / 256))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()