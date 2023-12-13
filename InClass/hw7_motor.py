import motor
import hw2_LED as LED
import time



if __name__ == '__main__':
    LED.Setup(2, "OUT")
    LED.TurnOnLED(2)
    
    while True:
        motor.SetAngle(0)
        time.sleep(2)        
        speed = motor.get_speed()
        dist = motor.distance(speed)
        angle = 0
        if dist < 100:
            break
        
        motor.SetAngle(180)
        time.sleep(2)
        speed = motor.get_speed()
        dist = motor.distance(speed)
        angle = 180
        if dist < 100:
            break
        
        
    LED.TurnOffLED(2)
    print("Measured Distance = %.1fcm" % dist)
    print("DateTime = ", time.ctime())
    print("Angle = ", angle)
    LED.Flashing(4, 5)
    
        
        
