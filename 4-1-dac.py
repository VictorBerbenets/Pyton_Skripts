import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dac2bin(a):
    return [int(digit) for digit in bin(a)[2:].zfill(8)]

def Enter():
    try:
        value = input()
        arg = int(value)

        if (arg > 255):
            print('Error: number must be <= 255')
            return -1
        elif (arg < 0):
            print('ERror: number should be >= 0')
            return -1
        else:
            return arg
    except:
        if value == "q":
            return -2
        else:
            print("error: invalid input")
            return -1

try:
    while (True):
        value = Enter()
        if value != -1:
            bin_num = dac2bin(value)
            GPIO.output(dac, bin_num)
            print(round(3.3 / 256 * value, 3), " B")
        elif value == -2:
            break

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()