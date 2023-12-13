import Adafruit_DHT
import time
import hw2_LED

sensor = Adafruit_DHT.DHT11
GPIO = 14
hw2_LED.Setup(3,"OUT")
hw2_LED.Setup(4,"OUT")
hw2_LED.TurnOnLED(3)
hw2_LED.TurnOnLED(4)
time.sleep(1.5)
hw2_LED.TurnOffLED(3)
hw2_LED.TurnOffLED(4)
while True:
    hw2_LED.Setup(2,"OUT")
    currentTime = time.strftime("%H:%M:%S")
    
    humidity, temperature = Adafruit_DHT.read_retry(sensor, GPIO)
    
    if humidity is not None and temperature is not None:
        print(currentTime, '->Temp={0}*C Humidity={1}%'.format(temperature, humidity))
        
        if(temperature > 25 and humidity > 60):
            hw2_LED.TurnOnLED(2)
            time.sleep(1)
            hw2_LED.TurnOffLED(2)
            time.sleep(1)
    else:
        print('Failed to get reading. Try again!')
    time.sleep(5)