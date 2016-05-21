import RPi.GPIO as GPIO
from time import sleep


phase_seq = [[1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0],
             [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [1, 0, 0, 1]]
num_phase = len(phase_seq)


class BipolarStepperMotor:

    def __init__(self, a1, a2, b1, b2):
        GPIO.setmode(GPIO.BCM)
        self.pin_a1 = a1
        self.pin_a2 = a2
        self.pin_b1 = b1
        self.pin_b2 = b2

        GPIO.setup(self.pin_a1, GPIO.OUT)
        GPIO.setup(self.pin_a2, GPIO.OUT)
        GPIO.setup(self.pin_b1, GPIO.OUT)
        GPIO.setup(self.pin_b2, GPIO.OUT)

        self.phase = 0
        self.dir = 0
        self.pos = 0

    def __del__(self):
        GPIO.cleanup()

    def move(self, dir, steps, delay=0.0005):
        for i in range(steps):
            next_phase = (self.phase + dir) % num_phase

            GPIO.output(self.pin_a1, phase_seq[next_phase][0])
            GPIO.output(self.pin_b2, phase_seq[next_phase][1])
            GPIO.output(self.pin_a2, phase_seq[next_phase][2])
            GPIO.output(self.pin_b1, phase_seq[next_phase][3])

            self.phase = next_phase
            self.dir = dir
            self.pos += dir

            sleep(delay)

    def unhold(self):
        GPIO.output(self.pin_a1, 0)
        GPIO.output(self.pin_a2, 0)
        GPIO.output(self.pin_b1, 0)
        GPIO.output(self.pin_b2, 0)

if __name__ == "__main__":
    m1 = BipolarStepperMotor(19, 26, 20, 21)
    for i in range(10):
        m1.move(1, 50, 0.001)
        m1.move(-1, 50, 0.001)
