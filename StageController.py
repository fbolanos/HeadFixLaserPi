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
        self.motor_x = BipolarStepperMotor(20, 21, 19, 26, 0.075)

        # Y direction motor resolution in mm
        self.motor_y = BipolarStepperMotor(12, 16, 6, 13, 0.075)

        # Laser Pin
        self.laser_pin = 18
        GPIO.setup(self.laser_pin, GPIO.OUT)
        GPIO.output(self.laser_pin, False)

        # Frequency of laser pulses
        self.frequency = 100

        # On time of the pulse
        self.duty_cycle = 0.95

        # Time to leave the laser pulsing for
        self.length = 0.5

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
            return 0

    def pulse_laser(self):
        t_start = time()
        while (time()-t_start < self.length):
            GPIO.output(self.laser_pin, True)
            sleep(self.on_time)
            GPIO.output(self.laser_pin, False)
            sleep(self.off_time)


if __name__ == "__main__":
    sc = StageController()

    #coords = [Coordinate(2, 2), Coordinate(8, 2), Coordinate(3, 5),
    #          Coordinate(5.5, 5.5), Coordinate(5, 5),
    #          Coordinate(7, 5), Coordinate(2, 8), Coordinate(8, 8)]

    #coords = [Coordinate(5, 0.0), Coordinate(5, 0.5), Coordinate(5, 1.0),
    #          Coordinate(5, 1.5), Coordinate(5, 2.0), Coordinate(5, 2.5),
    #          Coordinate(5, 3.0), Coordinate(5, 3.5), Coordinate(5, 4.0),
    #          Coordinate(5, 4.5), Coordinate(5, 5.0), Coordinate(5, 5.5),
    #          Coordinate(5, 6.0), Coordinate(5, 6.5), Coordinate(5, 7.0),
    #          Coordinate(5, 7.5), Coordinate(5, 8.0), Coordinate(5, 8.5),
    #          Coordinate(5, 9.0), Coordinate(5, 9.5), Coordinate(5, 10)]
              

    # Draw a 10x10mmm square
    #GPIO.output(sc.laser_pin, True)
    #sc.move_to(10, 10, 1)
    #sc.move_to(0, 0, 1)
    #GPIO.output(sc.laser_pin, False)

    coords = []
    for i in range(5):
        for j in range(5):
            coords.append(Coordinate(float(i), float(j)))
            
    #for i in range(10):
    #    coords.append(Coordinate(5, float(i)))
        #coords.append(Coordinate(5, float(i)+0.5))
        
        #coords.append(Coordinate(float(i), 5))
        #coords.append(Coordinate(float(i)+0.5, 5))              
    #for i in range(10):
    #    coords.append(Coordinate(float(i), 5))

    #for i in range(10):
    #    coords.append(Coordinate(i, i))

    #for i in range(10):
    #    coords.append(Coordinate(i, 10-i))
    #coords = []
    #for i in range(4):
    #    coords.append(Coordinate(i+1, i+1))
    #    coords.append(Coordinate(0, 0))

    for i in range(1):
        #shuffle(coords)
        for coord in coords:
            print "Moving to (", coord.x, ", ", coord.y, ")."
            sc.move_to(coord.x, coord.y, 1)
            print "Pulsing Laser"
            sc.pulse_laser()

        sc.move_to(0, 0, 10)
