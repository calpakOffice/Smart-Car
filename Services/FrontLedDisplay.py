import time
import RPi.GPIO as GPIO

# from Constants.GpioAddress import LED_FRONT_DISPLAY_DIO, LED_FRONT_DISPLAY_SCLK
LED_FRONT_DISPLAY_SCLK = 8
LED_FRONT_DISPLAY_DIO  = 9 

# Display pattern data


matrix_forward = (0x00, 0x00, 0x00, 0x00, 0x12, 0x24, 0x48, 0x90, 0x90, 0x48, 0x24, 0x12, 0x00, 0x00, 0x00, 0x00)
matrix_back = (0x00, 0x00, 0x00, 0x00, 0x48, 0x24, 0x12, 0x09, 0x09, 0x12, 0x24, 0x48, 0x00, 0x00, 0x00, 0x00)
matrix_left = (0x00, 0x00, 0x00, 0x00, 0x18, 0x24, 0x42, 0x99, 0x24, 0x42, 0x81, 0x00, 0x00, 0x00, 0x00, 0x00)
matrix_right = (0x00, 0x00, 0x00, 0x00, 0x00, 0x81, 0x42, 0x24, 0x99, 0x42, 0x24, 0x18, 0x00, 0x00, 0x00, 0x00)

matrix_names = {
    0x46 : matrix_forward,
    0x44 : matrix_left,
    0x43 : matrix_right,
    0x15 : matrix_back
}
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_FRONT_DISPLAY_SCLK,GPIO.OUT)
GPIO.setup(LED_FRONT_DISPLAY_DIO,GPIO.OUT)


def nop():
    time.sleep(0.00003)
    
def start():
    GPIO.output(LED_FRONT_DISPLAY_SCLK,0)
    nop()
    GPIO.output(LED_FRONT_DISPLAY_SCLK,1)
    nop()
    GPIO.output(LED_FRONT_DISPLAY_DIO,1)
    nop()
    GPIO.output(LED_FRONT_DISPLAY_DIO,0)
    nop()
    
def matrix_clear():
    GPIO.output(LED_FRONT_DISPLAY_SCLK,0)
    nop()
    GPIO.output(LED_FRONT_DISPLAY_DIO,0)
    nop()
    GPIO.output(LED_FRONT_DISPLAY_DIO,0)
    nop()
def send_date(date):
    for i in range(0,8):
        GPIO.output(LED_FRONT_DISPLAY_SCLK,0)
        nop()
        if date & 0x01:
            GPIO.output(LED_FRONT_DISPLAY_DIO,1)
        else:
            GPIO.output(LED_FRONT_DISPLAY_DIO,0)
        nop()
        GPIO.output(LED_FRONT_DISPLAY_SCLK,1)
        nop()
        date >>= 1
        GPIO.output(LED_FRONT_DISPLAY_SCLK,0)
    
def end():
    GPIO.output(LED_FRONT_DISPLAY_SCLK,0)
    nop()
    GPIO.output(LED_FRONT_DISPLAY_DIO,0)
    nop()
    GPIO.output(LED_FRONT_DISPLAY_SCLK,1)
    nop()
    GPIO.output(LED_FRONT_DISPLAY_DIO,1)
    nop()
   
def matrix_display(matrix_value):
    if (matrix_value in matrix_names):
        matrix = matrix_names[matrix_value]
    else:
        return 

    
    start()
    send_date(0xc0)
    
    for i in range(0,16):
        send_date(matrix[i])
        
    end()
    start()
    send_date(0x8A)
    end()
