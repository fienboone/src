
import Spindown
import time
import matplotlib.pyplot as plt
import numpy as np
import math

class Motor:


    def __init__(self):
        self.dev = Spindown.Spindown();

    def spinmotor(self):
        self.dev.toggle_d5_pwm();
        self.dev.toggle_d6_dir();
        time.sleep(5);
        self.dev.toggle_d7_en();

        x = 0;
        list = [];
        anglelist = [];
        a = time.time();

        while x < 5000:
            x += 1;
            b = time.time();
            y = b-a;
            list.append(y);

            angle = self.dev.get_angle();
            angle_degrees = (angle/43.9);
            anglelist.append(angle_degrees);
            anglelist2 = np.unwrap(anglelist, 360);

        #print(list);
        #print(anglelist);
        plt.plot(list, anglelist);
        plt.title('Angle vs Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Angle(degrees)')
        plt.show();
        plt.plot(list, anglelist2);
        plt.title('Absolute angle vs Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Absolute angle (degrees)')
        plt.show();
