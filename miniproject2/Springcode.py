import miniproject2
import time

class a:

    def __init__(self):
        self.dev = miniproject2.miniproject2()

    def pwm(self, angle):
        pwm = (20/16383)*angle
        return pwm

    def b(self):

        self.dev.set_duty(0)                        #makes sure that the motor doesn't spin without
        self.dev.toggle_d7_en()                     #giving the mechanism a ceertain deviation

        counter = 0                                 #counter counts amount of full rotations
        initialAngle = self.dev.get_angle()

        while True:
            time.sleep(0.3)
            currentAngle = self.dev.get_angle()
            time.sleep(0.00001)
            newAngle = self.dev.get_angle()

            diff = newAngle - currentAngle
            diff2 = newAngle - initialAngle
            print("diff is", diff, "newAngle is", newAngle, "diff2 is", diff2, "counter is", counter)

            if counter >= 0:
                if diff >= -16000 and diff <= -10:
                    q = diff2
                    r = self.pwm(q)
                    self.dev.set_duty(r)

                elif diff <= 16000 and diff >= 10:
                    q = diff2
                    r = self.pwm(q)
                    self.dev.set_duty(r)
                    '''
                elif diff > 16000:
                    self.dev.toggle_d6_dir()
                    counter -= 1
                    q = diff2
                    r = self.pwm(q)
                    self.dev.set_duty(r)
                '''
                elif diff < -100:
                    self.dev.toggle_d6_dir()
                    counter -= 1;
                    q = diff2
                    r = self.pwm(q)
                    self.dev.set_duty(r)


            elif counter < 0:
                if diff >= -16000 and diff <= -10:
                    q = 16383 - diff2
                    r = self.pwm(q)
                    self.dev.set_duty(r)

                elif diff <= 16000 and diff >= 10:
                    q = 16383 - diff2
                    r = self.pwm(q)
                    self.dev.set_duty(r)

                elif diff < -16000:
                    counter += 1;
                    q = 16383 - diff2
                    r = self.pwm(q)
                    self.dev.set_duty(r)

                elif diff > -100:
                    self.dev.toggle_d6_dir()
                    counter -= 1
                    q = 16383 - diff2
                    r = self.pwm(q)
                    self.dev.set_duty(r)
