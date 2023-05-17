from Constants.GpioAddress import LEFT_LANE_SENSOR, MIDDLE_LANE_SENSOR, RIGHT_LANE_SENSOR
import RPi.GPIO as GPIO


def init_lane_sensors():
    GPIO.setmode(GPIO.BCM) # use BCM numbers

    GPIO.setup(RIGHT_LANE_SENSOR,GPIO.IN)  # set trackingPin INPUT mode
    GPIO.setup(MIDDLE_LANE_SENSOR,GPIO.IN)
    GPIO.setup(LEFT_LANE_SENSOR,GPIO.IN)

def is_car_in_road():
    # if the read value is 1 , the sensor found black surface
    right_val = GPIO.input(RIGHT_LANE_SENSOR) # read the value 
    middle_val = GPIO.input(MIDDLE_LANE_SENSOR)
    left_val = GPIO.input(LEFT_LANE_SENSOR)
    return ((right_val + middle_val + left_val) > 0)        