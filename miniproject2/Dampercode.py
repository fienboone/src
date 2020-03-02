import miniproject2
import time

class VirtualDamper:

    def __init__(self):
        self.dev = miniproject2.miniproject2()

    def pwm(self, speed, maxSpeed):
        pwm = (100/maxSpeed)*abs(speed)
        return pwm

    def virtualDamper(self):

        self.dev.set_duty(0)                        #makes sure that the motor doesn't spin without
        self.dev.toggle_d7_en()                     #giving the mechanism a ceertain deviation

        counter = 0
        maxSpeed = 6000/0.2                              #counter counts amount of full rotations

        while True:
            currentAngle = self.dev.get_angle()
            a = time.time()
            time.sleep(0.01)
            newAngle = self.dev.get_angle()
            b = time.time()
            diff = newAngle - currentAngle
            timediff = (b-a)

            if counter >= 0:

                if  diff >= -15000 and diff <= 15000:
                    angularVelocity = diff/timediff
                    z = round(angularVelocity,2)
                    d = self.pwm(z,maxSpeed)
                    self.dev.set_duty(d)

                elif diff < -15000:
                    counter += 1

                    angularVelocity = diff/timediff
                    z = round(angularVelocity,2)
                    d = self.pwm(z,maxSpeed)
                    self.dev.set_duty(d)


                elif diff > 15000:
                    counter -= 1

                    angularVelocity = diff/timediff
                    z = round(angularVelocity,2)
                    d = self.pwm(z,maxSpeed)
                    self.dev.set_duty(d)


            elif counter < 0:
                self.dev.toggle_d6_dir()

                if  diff >= -15000 and diff <= 15000:
                    angularVelocity = (16383- abs(diff))/timediff
                    z = round(angularVelocity,2)
                    d = self.pwm(z,maxSpeed)
                    self.dev.set_duty(d)

                elif diff < -15000:
                    counter += 1

                    ngularVelocity = (16383- abs(diff))/timediff
                    z = round(angularVelocity,2)
                    d = self.pwm(z,maxSpeed)
                    self.dev.set_duty(d)

                elif diff > 15000:
                    counter -= 1

                    ngularVelocity = (16383- abs(diff))/timediff
                    z=round(angularVelocity,2)
                    d = self.pwm(z,maxSpeed)
                    self.dev.set_duty(d)
