from BipolarStepperMotor import BipolarStepperMotor
#from math import sqrt
from time import sleep
from random import randint

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


if __name__ == "__main__":
    sc = StageController()

    coords = [Coordinate(15, 15), Coordinate(0, 0)]

    #coords = []
    #for i in range(4):
    #    coords.append(Coordinate(i+1, i+1))
    #    coords.append(Coordinate(0, 0))

    for i in range(10):
        for coord in coords:
            sc.move_to(coord.x, coord.y, 1)
            sleep(0.01)
