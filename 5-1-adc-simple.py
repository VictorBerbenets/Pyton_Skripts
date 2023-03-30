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
diapazon = 256
def adc():
    for i in range(diapazon):
        value = dac2bin(i)
        GPIO.output(dac, value)

        time.sleep(0.001)
        if GPIO.input(comp) == 0:
            return i


try:
    while True:

            print('Digit value:',adc(), '  Napriagenie: {:.2f}v'.format(3.3 * adc() / 256))



finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()