
import time
from Constants.GpioAddress import HORIZENTAL_CAMERA_SERVO, VERTICAL_CAMERA_SERVO
import RPi.GPIO as GPIO
import cv2
class cameraController:
    def __init__(self):
        
        self.verticalAngle = 90
        self.horizentalAngle = 90
        GPIO.setup(VERTICAL_CAMERA_SERVO, GPIO.OUT)
        GPIO.setup(HORIZENTAL_CAMERA_SERVO, GPIO.OUT)

    def getStatus(self):
        capture = cv2.VideoCapture(0)
        capture.set(3,600)  # Gets the video frame width
        capture.set(10, 55)  # Screen brightness
        flag = False
        if (capture.isOpened()):
            # Open the camera and read the image
            flag, image = capture.read()
            if(flag):
                cv2.imwrite("./Services/Camera/status.jpg", image)
        capture.release()
        return flag

    def playVideo(self):
        while self.capture.isOpened():
            flag, image = self.capture.read()
            if(flag):
                cv2.imshow("image", image)
        
        self.capture.release()
        # Close all Windows
        cv2.destroyAllWindows()
    
    def moveVertical(self):
        verticalToMove = ((45 + self.verticalAngle)%180)
        print(verticalToMove)
        pulsewidth = (verticalToMove*11) + 500  # The pulse width
        GPIO.output(VERTICAL_CAMERA_SERVO,GPIO.HIGH)
        time.sleep(pulsewidth/1000000.0)
        GPIO.output(VERTICAL_CAMERA_SERVO,GPIO.LOW)
        self.verticalAngle = verticalToMove
    
    def moveHorizontal(self):
        horizentalToMove = ((45 + self.horizentalAngle)%180)
        print(horizentalToMove)
        pulsewidth = (horizentalToMove*11) + 500  # The pulse width
        GPIO.output(HORIZENTAL_CAMERA_SERVO,GPIO.HIGH)
        time.sleep(pulsewidth/1000000.0)
        GPIO.output(HORIZENTAL_CAMERA_SERVO,GPIO.LOW)  
        self.horizentalAngle = horizentalToMove 



