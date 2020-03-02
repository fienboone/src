import time
angle = 0

def getAngle():
    angle =5000
    print(angle)
    return angle

def setDutyCycle(x): #percentage
    print("duty cycle = ",x)

def pwm(angle):
    pwm =(1/819)*angle
    return pwm
#T=k*angulardisplacement so getAngle, higher angle--> higher counter torque
#generate this by adjusting the pwm signal (effective voltage on Mpins), higher pwm, higher w so LOWER torque.
#So to get a big torque, lower the pwm signal!

def virtualSpringWhile():
    initialAngle = getAngle() #getAngle from 0-16383
    a = 1
    counter = 0
    while a<2:

         angle = getAngle()
         time.sleep(0.01)
         newerAngle= getAngle()
         diff = newerAngle-angle
         diff2 = newerAngle-initialAngle #<16383

         if counter > =0:
             if diff > 0 and diff < 15000:
                 #stijging
                 q=(16383*counter)+diff2
                 r = pwm(q)
                 setDutyCycle(r)

             elif diff<0 and diff>-15000:
                 #daling
                 q=(16383*counter)+diff2
                 r = pwm(q)
                 setDutyCycle(r)

             elif diff == 0:
                 #stilstand
                 q=(16383*counter)+diff2
                 r = pwm(q)
                 setDutyCycle(r)

             elif diff < -15000:
                 counter += 1
                 q=(16383*counter)+diff2
                 r = pwm(q)
                 setDutyCycle(r)

             elif diff >15000:
                 counter -= 1
                 q=(16383*counter)+diff2
                 r = pwm(q)
                 setDutyCycle(r)

         elif counter <0:
             #changeDirection pin
             if diff > 0 and diff < 15000:
                 #stijging
                 q=(16383*counter)+diff2
                 r = pwm(q)
                 setDutyCycle(r)

             elif diff<0 and diff>-15000:
                 #daling
                 q=(16383*counter)+diff2
                 r = pwm(q)
                 setDutyCycle(r)

             elif diff == 0:
                 #stilstand
                 q=(16383*counter)+diff2
                 r = pwm(q)
                 setDutyCycle(r)

             elif diff < -15000:
                 counter += 1
                 q=(16383*counter)+diff2
                 r = pwm(q)
                 setDutyCycle(r)

             elif diff >15000:
                 counter -= 1
                 q=(16383*counter)+diff2
                 r = pwm(q)
                 setDutyCycle(r)

virtualSpring()
