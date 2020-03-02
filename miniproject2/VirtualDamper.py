# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:51:28 2020

@author: sjanssen
"""

import time

def getAngle():
    angle =5000
    print(angle)
    return angle
def setDutyCycle(x): #percentage
    print("duty cycle = ",x)

def pwm(speed,maxSpeed):
    pwm =(20/maxSpeed)*speed
    return pwm

def VirtualDamper():

    x=1
    counter = 0 #counter is only important here for knowing the direction of the disk movement
    maxSpeed = 16383/0.2 #choose

    while x<2:

        angle = getAngle()
        a = time.time()
        time.sleep(0.01)
        newerAngle= getAngle()
        b=time.time()
        diff = newerAngle-angle
        tijdDiff=(b-a)

        if counter >= 0:

            if diff >= 0 and diff < 15000:
                 #stijging

                 angularVelocity = diff/tijdDiff
                 z=round(angularVelocity,2)
                 d = pwm(z,maxSpeed)
                 setDutyCycle(d)

            elif diff<0 and diff>-15000:
                 #daling

                 angularVelocity = diff/tijdDiff
                 z=round(angularVelocity,2)
                 d = pwm(z,maxSpeed)
                 setDutyCycle(d)

            elif diff < -15000:
                 counter += 1

                 angularVelocity = diff/tijdDiff
                 z=round(angularVelocity,2)
                 d = pwm(z,maxSpeed)
                 setDutyCycle(d)

            elif diff >15000:
                 counter -= 1

                 angularVelocity = diff/tijdDiff
                 z=round(angularVelocity,2)
                 d = pwm(z,maxSpeed)
                 setDutyCycle(d)



        elif counter <0 :
            #change direction pin
            if diff >= 0 and diff < 15000:
                 #stijging

                 angularVelocity = diff/tijdDiff
                 z=round(angularVelocity,2)
                 d = pwm(z,maxSpeed)
                 setDutyCycle(d)

            elif diff<0 and diff>-15000:
                 #daling

                 angularVelocity = diff/tijdDiff
                 z=round(angularVelocity,2)
                 d = pwm(z,maxSpeed)
                 setDutyCycle(d)

            elif diff < -15000:
                 counter += 1

                 angularVelocity = diff/tijdDiff
                 z=round(angularVelocity,2)
                 d = pwm(z,maxSpeed)
                 setDutyCycle(d)

            elif diff >15000:
                 counter -= 1

                 angularVelocity = diff/tijdDiff
                 z=round(angularVelocity,2)
                 d = pwm(z,maxSpeed)
                 setDutyCycle(d)
