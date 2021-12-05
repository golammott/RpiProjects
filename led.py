import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(38, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)

def cycle(cycle_time=1):
    GPIO.output(36, GPIO.HIGH)
    time.sleep(cycle_time)
    GPIO.output(36, GPIO.LOW)
    GPIO.output(38, GPIO.HIGH)
    time.sleep(cycle_time)
    GPIO.output(38, GPIO.LOW)
    GPIO.output(40, GPIO.HIGH)
    time.sleep(cycle_time)
    GPIO.output(40, GPIO.LOW)
    GPIO.output(37, GPIO.HIGH)
    time.sleep(cycle_time)
    GPIO.output(37, GPIO.LOW)

def close():
    GPIO.cleanup([36,38,40,37])

if __name__=="__main__":
    cycle()
    cycle(cycle_time=0.5)
    cycle(cycle_time=0.25)
    cycle(cycle_time=0.1)
    cycle(cycle_time=0.1)
    cycle(cycle_time=0.1)
    cycle(cycle_time=0.1)
    close()
