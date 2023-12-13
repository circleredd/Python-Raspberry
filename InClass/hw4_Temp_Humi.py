import Adafruit_DHT
import time
import random
import hw2_LED

sensor = Adafruit_DHT.DHT11
GPIO = 14

while True:
    hw2_LED.Setup(2,"OUT")
    hw2_LED.Setup(3,"OUT")
    hw2_LED.Setup(4,"OUT")
    currentTime = time.strftime("%H:%M:%S")
    
    #humidity, temperature = Adafruit_DHT.read_retry(sensor, GPIO)
    humidity, temperature = random.randint(5,100), random.randint(30,40)
    
    if humidity is not None and temperature is not None:
        print(currentTime, '->Temp={0}*C Humidity={1}%'.format(temperature, humidity))
        
        if((temperature > 38 and humidity > 30) or (temperature > 31 and humidity > 80)):
            hw2_LED.Flashing(4,3)
            print("Be carefull of heatstroke!(Red Light)")
        elif(temperature > 34):
            hw2_LED.Flashing(3,3)
            print("Be carefull of heatstroke!(Yellow Light)")
        else:
            hw2_LED.TurnOnLED(2)
            print("no heatstroke danger")
            time.sleep(5)
            hw2_LED.TurnOffLED(2)
            time.sleep(1)
    else:
        print('Failed to get reading. Try again!')
    time.sleep(5)