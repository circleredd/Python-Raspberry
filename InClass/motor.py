import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
pwm = GPIO.PWM(21, 50)
pwm.start(0)
GPIO.output(21,True)

GPIO_TRIGGER = 7
GPIO_ECHO = 12
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def send_trigger_pulse():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    
def get_speed():
    speed = 33100+26*60
    return speed

def distance(speed):
    send_trigger_pulse()
    
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * speed)
    
    return distance

def SetAngle(angle):
    dutyCycle = 1/20 * angle + 3
    pwm.ChangeDutyCycle(dutyCycle)
    
if __name__ == '__main__':
    try:
        while True:
            speed = get_speed()
            dist = distance(speed)
            print("Measured Distance = %.1fcm" % dist)
            
            if dist < 15:
                SetAngle(0)
            else:
                SetAngle(180)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
