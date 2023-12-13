import RPi.GPIO as GPIO
import time

def Setup(GPIOnum, OUT_IN):
    GPIO.setmode(GPIO.BCM) #BOARD or BCM #GPIO -> BCM
    
    if OUT_IN == "OUT":
        GPIO.setup(GPIOnum, GPIO.OUT)
    else:
        GPIO.setup(GPIOnum, GPIO.IN)

def TurnOnLED(GPIOnum):
    GPIO.output(GPIOnum, True) #GPIOnum position power supply

def TurnOffLED(GPIOnum):
    GPIO.output(GPIOnum, False)

def GetGPIOStatus(GPIOnum):
    GPIO_State = GPIO.input(GPIOnum)
    return GPIO_State

def Flashing(GPIOnum, times):
    Setup(GPIOnum, "OUT")
    for i in range(0, times):
        TurnOnLED(GPIOnum)
        time.sleep(0.5)
        TurnOffLED(GPIOnum)
        time.sleep(0.5)


if __name__ == "__main__":
    try:
        #Setup(2, "IN")
        #print("The status of the GPIO10{0} is {1}".format(2,GetGPIOStatus(2)))
        Setup(2, "OUT")
        Setup(3, "OUT")
        Setup(4, "OUT")
        while True:
            TurnOnLED(2)
            time.sleep(1)
            TurnOffLED(2)
            time.sleep(1)
            for i in range(0, 5):
                TurnOnLED(3)
                time.sleep(0.2)
                TurnOffLED(3)
                time.sleep(0.5)
            TurnOnLED(4)
            time.sleep(2)
            TurnOffLED(4)
            time.sleep(1)            
    except KeyboardInterrupt:
            GPIO.cleanup()
            