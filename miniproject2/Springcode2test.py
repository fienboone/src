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
        a = time.time()

        while True:
            newAngle = self.dev.get_angle()
            diff = newAngle - initialAngle
            x = abs(diff)

            '''
            b = time.time();
            y = b-a;
            list.append(y);

            angle_degrees = (newAngle/43.9);
            anglelist.append(angle_degrees);
            '''

            if counter == 0:
                if diff > 50 and diff < 15000:
                    self.dev.set_dir0()
                    q = self.pwm(x)
                    self.dev.set_duty(q)

                elif diff > 15000:
                    counter = 1
                    self.dev.set_duty(0)

                elif diff >= -15 and diff <= 50:
                    q = self.pwm(0)
                    self.dev.set_duty(q)

            elif counter == 1:
                self.dev.set_dir1()

                if diff > 100 and diff < 15000:
                    q = self.pwm(16383-x)
                    self.dev.set_duty(q)

                elif diff > 50 and diff < 100:
                    counter = 0

                elif diff >= 15000 or diff <= 50:
                    q = self.pwm(0)
                    self.dev.set_duty(q)

        '''
        plt.plot(list, anglelist);
        plt.title('Angle vs Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Angle(degrees)')
        plt.show();
        '''
