from BipolarStepperMotor import BipolarStepperMotor
#from math import sqrt
from time import sleep, time
from random import shuffle
import RPi.GPIO as GPIO

class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class StageController:

    def __init__(self):
        # X direction motor resolution in mm
        self.motor_x = BipolarStepperMotor(19, 26, 20, 21, 0.075)

        # Y direction motor resolution in mm
        self.motor_y = BipolarStepperMotor(12, 16, 6, 13, 0.075)

        # Laser Pin
        self.laser_pin = 18
        GPIO.setup(self.laser_pin, GPIO.OUT)
        GPIO.output(self.laser_pin, False)

        # Frequency of laser pulses
        self.frequency = 100

        # On time of the pulse
        self.duty_cycle = 0.9

        # Time to leave the laser pulsing for
        self.length = 2

        # On time and off time
        self.on_time = 1.0/self.frequency * self.duty_cycle
        self.off_time = 1.0/self.frequency - self.on_time


    def move_to(self, new_x, new_y, speed):
        steps_x = int(round(new_x / self.motor_x.resolution)) - self.motor_x.pos
        steps_y = int(round(new_y / self.motor_y.resolution)) - self.motor_y.pos

        dir_x = self.get_dir(steps_x)
        dir_y = self.get_dir(steps_y)

        steps_x = abs(steps_x)
        steps_y = abs(steps_y)

        self.motor_x.move(dir_x, steps_x, self.motor_x.resolution / speed)
        self.motor_y.move(dir_y, steps_y, self.motor_y.resolution / speed)

    def get_dir(self, steps):
        if steps > 0:
            return 1
        elif steps < 0:
            return -1
        else:
            raise ValueError

    def pulse_laser(self):
        t_start = time()
        while (time()-t_start < self.length):
            GPIO.output(self.laser_pin, True)
            sleep(self.on_time)
            GPIO.output(self.laser_pin, False)
            sleep(self.off_time)


if __name__ == "__main__":
    sc = StageController()

    coords = [Coordinate(1, 1), Coordinate(9, 1), Coordinate(3, 5),
              Coordinate(7, 5), Coordinate(1, 9), Coordinate(9, 9)]

    # Draw a 10x10mmm square
    sc.move_to(10, 10, 1)



    #coords = []
    #for i in range(4):
    #    coords.append(Coordinate(i+1, i+1))
    #    coords.append(Coordinate(0, 0))

    #for i in range(1):
    #    for coord in coords:
    #        shuffle(coords)
    #        print "Moving to (", coord.x, ", ", coord.y, ")."
    #        sc.move_to(coord.x, coord.y, 5)
    #        print "Pulsing Laser"
    #        sc.pulse_laser()
