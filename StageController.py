from BipolarStepperMotor import BipolarStepperMotor
#from math import sqrt
from time import sleep

class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class StageController:

    def __init__(self):
        # X direction motor resolution in mm
        self.motor_x = BipolarStepperMotor(20, 21, 19, 26, 0.075)

        # Y direction motor resolution in mm
        self.motor_y = BipolarStepperMotor(6, 13, 12, 16, 0.075)

    def move_to(self, new_x, new_y, speed):
        steps_x = int(round(new_x / self.motor_x.resolution)) - self.motor_x.pos
        steps_y = int(round(new_y / self.motor_y.resolution)) - self.motor_y.pos

        dir_x = self.get_dir(steps_x)
        dir_y = self.get_dir(steps_y)

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

    coords = [Coordinate(5,5), Coordinate(0, 0)]


    for coord in coords:
        sc.move_to(coord.x, coord.y)
        sleep(2)
