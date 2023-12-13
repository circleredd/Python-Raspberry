import RPi.GPIO as GPIO
import time
import hw2_LED as LED

GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 7
GPIO_ECHO = 12

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

distance0 = 0
StopTime1 = 0

def send_trigger_pulse():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    

def get_speed():
    speed = 33100+26*60
    return speed


def get_velocity():
    global StopTime1, distance0, dist_error
    send_trigger_pulse()
    StopTime0 = StopTime1
    
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime1 = time.time()
    
    TimeElapsed = StopTime1 - StartTime
    speed = get_speed()
    distance1 = (TimeElapsed * speed) *0.5
    
    if distance1 < 2 or distance1 > 400:
        dist_error = True
    else:
        dist_error = False
    velocity = (distance1-distance0)/(StopTime1-StopTime0)
    distance0 = distance1
    
    return abs(velocity)

if __name__ == '__main__':
    try:
        LED.Setup(2, "OUT")
        LED.Setup(3, "OUT")
        LED.Setup(4, "OUT")
        global dist_error
        dist_error = False
        while True:
            velocity = get_velocity()
            if velocity > 30:
                LED.TurnOnLED(4)
                time.sleep(1.5)
                LED.TurnOffLED(4)
            elif velocity > 20 or velocity < 30:
                LED.TurnOnLED(3)
                time.sleep(1.5)
                LED.TurnOffLED(3)
            else:
                LED.TurnOnLED(2)
                time.sleep(1.5)
                LED.TurnOffLED(2)
            time.sleep(1.5)
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
                
                
                
    
    
    