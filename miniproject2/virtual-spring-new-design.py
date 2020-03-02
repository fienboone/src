# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:31:45 2020

@author: sjanssen
"""

import time
angle = 0

def getAngle():
    angle =5000
    print(angle)
    return angle

def setDutyCycle(x): #percentage
    print("duty cycle = ",x)

def pwm(angle):
    pwm =(100/16383)*angle
    return pwm
#T=k*angulardisplacement so getAngle, higher angle--> higher counter torque
#generate this by adjusting the pwm signal (effective voltage on Mpins), higher pwm, higher w so increase torque.
#So to get a big torque, increase the pwm signal!
def virtualSpring():

    initialAngle = getAngle() #getAngle from 0-16383

    counter =0
    while 1:

         angle = getAngle()
         time.sleep(0.01)
         newerAngle= getAngle()
         diff = newerAngle-angle
         diff2 = newerAngle-initialAngle #<16383
         
         if counter >=0:
             
             if diff >= -15000 and diff <=15000:
                 #stijging
                 q=diff2
                 r = pwm(q)
                 setDutyCycle(r)

             elif diff < -15000:
                 counter += 1
                 q=diff2
                 r = pwm(q)
                 setDutyCycle(r)

             elif diff >15000:
                 counter -= 1
                 q=diff2
                 r = pwm(q)
                 setDutyCycle(r)

         elif counter <0:
             #changeDirection pin
             if diff >= -15000 and diff <=15000:
                 #stijging
                 q=16383 - diff2
                 r = pwm(q)
                 setDutyCycle(r)


             elif diff < -15000:
                 counter += 1
                 q=16383 - diff2
                 r = pwm(q)
                 setDutyCycle(r)

             elif diff >15000:
                 counter -= 1
                 q=16383 - diff2
                 r = pwm(q)
                 setDutyCycle(r)

virtualSpring()