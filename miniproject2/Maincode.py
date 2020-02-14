import miniproject2
import time

class Maincode:

    def __init__(self):
        self.dev = miniproject2.miniproject2();

    def testVoltage(self):
        self.dev.set_duty(10);
        time.sleep(2);
        self.dev.set_duty(30);
        time.sleep(2);
        self.dev.set_duty(50);
        time.sleep(2);
        self.dev.set_duty(70);
        time.sleep(2);
        self.dev.set_duty(90);
