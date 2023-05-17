import RPi.GPIO as GPIO
import time

# Control M2 motor
L_IN1 = 20
L_IN2 = 21
L_PWM1 = 0
# Control M1 motor
L_IN3 = 22
L_IN4 = 23
L_PWM2 = 1
# Control M3 motor
R_IN1 = 24
R_IN2 = 25
R_PWM1 = 12
# Control M4 motor
R_IN3 = 26
R_IN4 = 27
R_PWM2 = 13

class MotorDrive:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)  # use BCM numbers
        #set the MOTOR Driver Pin OUTPUT mode
        GPIO.setup(L_IN1,GPIO.OUT)
        GPIO.setup(L_IN2,GPIO.OUT)
        GPIO.setup(L_PWM1,GPIO.OUT)
        GPIO.setup(L_IN3,GPIO.OUT)
        GPIO.setup(L_IN4,GPIO.OUT)
        GPIO.setup(L_PWM2,GPIO.OUT)
        GPIO.setup(R_IN1,GPIO.OUT)
        GPIO.setup(R_IN2,GPIO.OUT)
        GPIO.setup(R_PWM1,GPIO.OUT)
        GPIO.setup(R_IN3,GPIO.OUT)
        GPIO.setup(R_IN4,GPIO.OUT)
        GPIO.setup(R_PWM2,GPIO.OUT)

        GPIO.output(L_IN1,GPIO.LOW)
        GPIO.output(L_IN2,GPIO.LOW)
        GPIO.output(L_IN3,GPIO.LOW)
        GPIO.output(L_IN4,GPIO.LOW)
        GPIO.output(R_IN1,GPIO.LOW)
        GPIO.output(R_IN2,GPIO.LOW)
        GPIO.output(R_IN3,GPIO.LOW)
        GPIO.output(R_IN4,GPIO.LOW)

        #set pwm frequence to 1000hz
        self.pwm_R1 = GPIO.PWM(R_PWM1,100)
        self.pwm_R2 = GPIO.PWM(R_PWM2,100)
        self.pwm_L1 = GPIO.PWM(L_PWM1,100)
        self.pwm_L2 = GPIO.PWM(L_PWM2,100)
        self.pwm_R1.start(0)
        self.pwm_L1.start(0)
        self.pwm_R2.start(0)
        self.pwm_L2.start(0)

    def stop(self):
        self.pwm_L1.ChangeDutyCycle(0)
        self.pwm_L2.ChangeDutyCycle(0)
        self.pwm_R1.ChangeDutyCycle(0)
        self.pwm_R2.ChangeDutyCycle(0)

    def drive_cmd(self,key_val,distance):
        if((key_val==0x46) and (distance>10)):
            GPIO.output(L_IN1,GPIO.LOW)  #Upper Left forward
            GPIO.output(L_IN2,GPIO.HIGH)
            self.pwm_L1.ChangeDutyCycle(50)
            GPIO.output(L_IN3,GPIO.HIGH)  #Lower left forward
            GPIO.output(L_IN4,GPIO.LOW)
            self.pwm_L2.ChangeDutyCycle(50)
            GPIO.output(R_IN1,GPIO.HIGH)  #Upper Right forward
            GPIO.output(R_IN2,GPIO.LOW)
            self.pwm_R1.ChangeDutyCycle(50)
            GPIO.output(R_IN3,GPIO.LOW)  #Lower Right forward
            GPIO.output(R_IN4,GPIO.HIGH)
            self.pwm_R2.ChangeDutyCycle(50)
            time.sleep(0.25)
            self.stop()
        elif(key_val==0x44):
            GPIO.output(L_IN1,GPIO.HIGH)
            GPIO.output(L_IN2,GPIO.LOW)
            self.pwm_L1.ChangeDutyCycle(70)
            GPIO.output(L_IN3,GPIO.LOW)  
            GPIO.output(L_IN4,GPIO.HIGH)
            self.pwm_L2.ChangeDutyCycle(70)
            GPIO.output(R_IN1,GPIO.HIGH)  #Upper Right forward
            GPIO.output(R_IN2,GPIO.LOW)
            self.pwm_R1.ChangeDutyCycle(70)
            GPIO.output(R_IN3,GPIO.LOW)  #Lower Right forward
            GPIO.output(R_IN4,GPIO.HIGH)
            self.pwm_R2.ChangeDutyCycle(70)
            time.sleep(0.15)
            self.stop()
        elif(key_val==0x40):
            print("Button ok")
            # self.stop()
        elif(key_val==0x43):
            GPIO.output(L_IN1,GPIO.LOW)  #Upper Left forward
            GPIO.output(L_IN2,GPIO.HIGH)
            self.pwm_L1.ChangeDutyCycle(70)
            GPIO.output(L_IN3,GPIO.HIGH)  #Lower left forward
            GPIO.output(L_IN4,GPIO.LOW)
            self.pwm_L2.ChangeDutyCycle(70)
            GPIO.output(R_IN1,GPIO.LOW)  #Upper Right forward
            GPIO.output(R_IN2,GPIO.HIGH)
            self.pwm_R1.ChangeDutyCycle(70)
            GPIO.output(R_IN3,GPIO.HIGH)  #Lower Right forward
            GPIO.output(R_IN4,GPIO.LOW)
            self.pwm_R2.ChangeDutyCycle(70)
            time.sleep(0.15)
            self.stop()
        elif(key_val==0x15):
            print("Button down")
            GPIO.output(L_IN1,GPIO.HIGH)
            GPIO.output(L_IN2,GPIO.LOW)
            self.pwm_L1.ChangeDutyCycle(50)
            GPIO.output(L_IN3,GPIO.LOW)
            GPIO.output(L_IN4,GPIO.HIGH)
            self.pwm_L2.ChangeDutyCycle(50)
            GPIO.output(R_IN1,GPIO.LOW)
            GPIO.output(R_IN2,GPIO.HIGH)
            self.pwm_R1.ChangeDutyCycle(50)
            GPIO.output(R_IN3,GPIO.HIGH)
            GPIO.output(R_IN4,GPIO.LOW)
            self.pwm_R2.ChangeDutyCycle(50)
            time.sleep(0.35)
            self.stop()
        elif(key_val==0x16):
            print("Button 1")
        elif(key_val==0x19):
            print("Button 2")
        elif(key_val==0x0d):
            print("Button 3")
        elif(key_val==0x0c):
            print("Button 4")
        elif(key_val==0x18):
            print("Button 5")
        elif(key_val==0x5e):
            print("Button 6")
        elif(key_val==0x08):
            print("Button 7")
        elif(key_val==0x1c):
            print("Button 8")
        elif(key_val==0x5a):
            print("Button 9")
        elif(key_val==0x42):
            print("Button *")
        elif(key_val==0x52):
            print("Button 0")
        elif(key_val==0x4a):
            print("Button #")