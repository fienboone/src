# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:46:24 2020

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
    pwm =(100/maxSpeed)*abs(speed)
    return pwm

def VirtualDamper():
    
    counter = 0 #counter is only important here for knowing the direction of the disk movement
    maxSpeed = 6000/0.2 #choose
    
    while 1:
        
        angle = getAngle()
        a = time.time()
        time.sleep(0.01)
        newerAngle= getAngle()
        b=time.time()
        diff = newerAngle-angle
        tijdDiff=(b-a)
        
        if counter >= 0:
            
            if diff >= -15000 and diff <=15000:
                 #stijging
                 
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
            if diff >= -15000 and diff <=15000:
                 #stijging
                 
                 angularVelocity = (16383 - abs(diff))/tijdDiff
                 z=round(angularVelocity,2)
                 d = pwm(z,maxSpeed)
                 setDutyCycle(d)

            elif diff < -15000:
                 counter += 1
                 
                 angularVelocity = (16383 - abs(diff))/tijdDiff
                 z=round(angularVelocity,2)
                 d = pwm(z,maxSpeed)
                 setDutyCycle(d)
                 
            elif diff >15000:
                 counter -= 1
                 
                 angularVelocity = (16383 - abs(diff))/tijdDiff
                 z=round(angularVelocity,2)
                 d = pwm(z,maxSpeed)
                 setDutyCycle(d)
VirtualDamper()
