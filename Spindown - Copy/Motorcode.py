
import Spindown
import time
import matplotlib.pyplot as plt

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

        while x < 10000:
            x += 1;
            b = time.time();
            y = b-a;
            y_rounded = round(y,2);
            list.append(y_rounded);

            angle = self.dev.get_angle();
            angle_degrees = (angle/43.9);
            angle_degrees_rounded = round(angle_degrees, 2);
            anglelist.append(angle_degrees_rounded);

        #print(list);
        #print(anglelist);
        plt.plot(list, anglelist);
        plt.title('Angle vs Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Angle(degrees)')
        plt.show();
