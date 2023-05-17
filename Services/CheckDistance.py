from Constants.GpioAddress import ULTRASONIC_GPIO_ECHO, ULTRASONIC_GPIO_TRIGGER
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)


def check_distance():
    GPIO.setup(ULTRASONIC_GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(ULTRASONIC_GPIO_ECHO, GPIO.IN )

    GPIO.output(ULTRASONIC_GPIO_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)  #10us
    GPIO.output(ULTRASONIC_GPIO_TRIGGER, GPIO.LOW)
    while not GPIO.input(ULTRASONIC_GPIO_ECHO):
        pass
    t1 = time.time()
    while GPIO.input(ULTRASONIC_GPIO_ECHO):
        pass
    t2 = time.time()
    time.sleep(0.01)
    return ((t2 - t1)* 340 / 2) * 100