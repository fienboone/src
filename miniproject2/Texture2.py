# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:48:18 2020

@author: sjanssen
"""

import miniproject2
import matplotlib.pyplot as plt

class a:

    def __init__(self):
        self.dev = miniproject2.miniproject2()

    def pwm(self, angle):
        pwm = (100/16000)*angle #yeet
        return pwm

    def b(self,x): #x=how many alternating regions of torque do you want?

        self.dev.set_duty(0)                        #makes sure that the motor doesn't spin without
        self.dev.toggle_d7_en()                     #giving the mechanism a ceertain deviation

        y = 16000/x #aantal graden per gekozen regio
        z = round(y)

        initialAngle = self.dev.get_angle()

        r = 0
        anglelist = []
        pwmlist = []

        while True:

            while r < 5000:
                r += 1
                newAngle = self.dev.get_angle()
                diff = newAngle - initialAngle
                x = abs(diff)
                angle_degrees = (newAngle/43.9);
                anglelist.append(angle_degrees);

                regioLijst=[]
                hoekLijst=[]

                for i in range(x):
                    regioLijst.append(i+1)
                    hoekLijst.append(z*i)


                for i in range(x-1):

                    if diff > hoekLijst[i-1] and diff <= hoekLijst[i]:

                        if (i%2) != 0:
                            q = 0
                            self.dev.set_duty(q)


                        elif (i%2) == 0:
                            q = 10*i
                            self.dev.set_duty(q)

                pwmlist.append(q)

            plt.plot(anglelist, pwmlist);
            plt.title('Angle vs PWM')
            plt.xlabel('Angle(degrees)')
            plt.ylabel('Duty(%)')
            plt.show();
            break
