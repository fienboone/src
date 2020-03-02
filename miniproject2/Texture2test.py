# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:48:18 2020

@author: sjanssen
"""

import miniproject2


class a:

    def __init__(self):
        self.dev = miniproject2.miniproject2()

    def pwm(self, angle):
        pwm = (100/16000)*angle #yeet
        return pwm
    '''
    def angleToCrazyNumber(x):#fill in angle x [in degrees], eg x=20, than per 20 degrees the torque will be different
        angle = (x/360)*16000
        return angle
'''
    def b(self,x): #x=how many alternating regions of torque do you want?

        self.dev.set_duty(0)                        #makes sure that the motor doesn't spin without
        self.dev.toggle_d7_en()                     #giving the mechanism a ceertain deviation

        y = 16000/x #aantal graden per gekozen regio
        z = round(y)

        initialAngle = self.dev.get_angle()


        while True:
            newAngle = self.dev.get_angle()
            diff = newAngle - initialAngle
            x = abs(diff)
            regioLijst=[]
            hoekLijst=[]
            
            for i in range(x):
                regioLijst.append(i+1)
                hoekLijst.append(z*i)


            for i in range(x-1):

                if diff > hoekLijst[i-1] and diff <= hoekLijst[i]:

                    if (i%2) != 0: #oneven dus torque geven
                        q = 0
                        self.dev.set_duty(q)

                    elif (i%2) == 0: #even dus geen torque geven
                        q = 60
                        self.dev.set_duty(q)
