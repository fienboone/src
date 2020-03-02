# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:46:24 2020

@author: sjanssen
"""
import miniproject2
import time
import matplotlib.pyplot as plt

class a:

    def __init__(self):
        self.dev = miniproject2.miniproject2()

    def pwm(self,speed,maxSpeed):
        pwm =(60/maxSpeed)*abs(speed)
        return pwm

    def b(self):

        self.dev.set_duty(0)
        self.dev.toggle_d7_en()

        counter = 0 #counter is only important here for knowing the direction of the disk movement
        maxSpeed = 6000/0.2 #choose

        r = 0
        angularVelocitylist = []
        pwmlist = []

        while True:

            while r < 200:
                r += 1
                angle = self.dev.get_angle()
                a = time.time()
                time.sleep(0.01)
                newerAngle = self.dev.get_angle()
                b = time.time()
                diff = newerAngle-angle
                tijdDiff = (b-a)

                if counter == 0:

                    if diff > 50 and diff < 16300:
                        self.dev.set_dir0()
                        angularVelocity = (diff*3.1415)/(tijdDiff*180)
                        z = round(angularVelocity,2)
                        d = self.pwm(z,maxSpeed)
                        self.dev.set_duty(d)

                    elif diff < -50 and diff > -16300:
                        self.dev.set_dir1()
                        angularVelocity = (diff*3.1415)/(tijdDiff*180)
                        z = round(angularVelocity,2)
                        d = self.pwm(z,maxSpeed)
                        self.dev.set_duty(d)

                    elif diff > 16300:
                        counter = 1

                    elif diff >= -50 and diff <= 50:
                        z = 0
                        d = self.pwm(0,1)
                        self.dev.set_duty(d)

                elif counter == 1:

                    if diff < -50 and diff > -16300:
                        self.dev.set_dir1()
                        angularVelocity = (16383 - abs(diff)*180)/(tijdDiff*180)
                        z = round(angularVelocity,2)
                        d = self.pwm(z,maxSpeed)
                        self.dev.set_duty(d)

                    elif diff > 50 and diff < 16300:
                        self.dev.set_dir0()
                        angularVelocity = (16383 - abs(diff)*180)/(tijdDiff*180)
                        z = round(angularVelocity,2)
                        d = self.pwm(z,maxSpeed)
                        self.dev.set_duty(d)

                    elif diff > -16300:
                        counter = 0


                    elif diff >= -50 and diff <= 50:
                        z = 0
                        d = self.pwm(0,1)
                        self.dev.set_duty(d)

                angularVelocitylist.append(z)
                pwmlist.append(d)

            plt.plot(angularVelocitylist, pwmlist);
            plt.title('Angular Velocity vs Duty')
            plt.xlabel('Anglur Velocity(rad/s)')
            plt.ylabel('Duty(%)')
            plt.show();
            break
