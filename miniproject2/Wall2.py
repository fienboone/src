import miniproject2
import time
import matplotlib.pyplot as plt
import numpy as np
import math

class a:

    def __init__(self):
        self.dev = miniproject2.miniproject2()

    def pwm(self, angle):
        pwm = (50/16383)*angle #yeet
        return pwm

    def b(self):

        self.dev.set_duty(0)                        #makes sure that the motor doesn't spin without
        self.dev.toggle_d7_en()                     #giving the mechanism a ceertain deviation

        counter = 0                                 #counter counts amount of full rotations
        initialAngle = self.dev.get_angle()

        r = 0
        anglelist = []
        pwmlist = []

        while True:

            while r < 7000:
                r += 1
                newAngle = self.dev.get_angle()
                diff = newAngle - initialAngle
                x = abs(diff)
                angle_degrees = (newAngle/43.9);
                anglelist.append(angle_degrees);


                if counter == 0:
                    if diff > -5 and diff < 7800:
                        self.dev.set_dir0()
                        q = 0
                        self.dev.set_duty(q)


                    elif diff >= 7800 and diff <= 16000:
                        q = 100
                        self.dev.set_duty(q)


                    elif diff < 16383 and diff > 16000:
                        counter = 1
                        q = 0
                        self.dev.set_duty(q)


                elif counter == 1:
                    if diff < 16838 and diff > 8200:
                        self.dev.set_dir1()
                        q = 0
                        self.dev.set_duty(q)


                    elif diff <= 8200 and diff >= 100:
                        q = 100
                        self.dev.set_duty(q)


                    elif diff > 0 and diff < 100:
                        counter = 0
                        q = 0
                        self.dev.set_duty(q)

                pwmlist.append(q)

            plt.plot(anglelist, pwmlist);
            plt.title('Angle vs Duty')
            plt.xlabel('Angle(degrees)')
            plt.ylabel('Duty(%)')
            plt.show();
            break
