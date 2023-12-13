import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import hw2_LED

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 7
GPIO_ECHO = 12
GPIO_TEMP = 14

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
sensor = Adafruit_DHT.DHT11
hw2_LED.Setup(2,"OUT")	#set lights
hw2_LED.Setup(3,"OUT")
hw2_LED.Setup(4,"OUT")

def send_trigger_pulse():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

def get_speed():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, GPIO_TEMP)
    speed = 33100 + 25 * 60
    return speed

def distance(speed):
    send_trigger_pulse()
    
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * speed) / 2
    return distance

if __name__ == '__main__':
    try:
        while True:
            speed = get_speed()
            dist = distance(speed)
            if(dist < 10):
                print("Measured Distance = %.1f cm -> red" %dist)
                hw2_LED.TurnOnLED(4)
                time.sleep(3)
                hw2_LED.TurnOffLED(4)
            elif(dist >= 10 and dist <20):
                print("Measured Distance = %.1f cm -> yellow" %dist)
                hw2_LED.TurnOnLED(3)
                time.sleep(3)
                hw2_LED.TurnOffLED(3)
            elif(dist <= 30):
                print("Measured Distance = %.1f cm -> green" %dist)
                hw2_LED.TurnOnLED(2)
                time.sleep(3)
                hw2_LED.TurnOffLED(2)
            else:
                print("Measured Distance = %.1f cm -> No light!" %dist)
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()