import pygame
from BipolarStepperMotor import BipolarStepperMotor

# Motors settings

# motor_lr object to be controlled
motor_lr = BipolarStepperMotor(20, 21, 19, 26)


# motor_ud object to be controlled
motor_ud = BipolarStepperMotor(6, 13, 12, 16)
#motor_ud = BipolarStepperMotor(12, 16, 6, 13)

# initialize game engine
pygame.init()
# set screen width/height and caption
size = [64, 48]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Laser Stage Controller')
# initialize clock. used later in the loop.
clock = pygame.time.Clock()

# Loop until the user clicks close button
done = False
step_mode = False
delay = 0.1
move_left = False
move_right = False
move_up = False
move_down = False
number_steps = 1
while done is False:
    # write event handlers here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            # Left Right motor motion
            if event.key == pygame.K_LEFT:
                if step_mode:
                    motor_lr.move(1, number_steps, delay)
                else:
                    move_left = True
            elif event.key == pygame.K_RIGHT:
                if step_mode:
                    motor_lr.move(-1, number_steps, delay)
                else:
                    move_right = True

            # Up Down motor motion
            elif event.key == pygame.K_UP:
                if step_mode:
                    motor_ud.move(1, number_steps, delay)
                else:
                    move_up = True
            elif event.key == pygame.K_DOWN:
                if step_mode:
                    motor_ud.move(-1, number_steps, delay)
                else:
                    move_down = True

            # Delay, mode and unhold keys
            elif event.key == pygame.K_e:
                if step_mode:
                    print "Fast Mode!!"
                    step_mode = False
                else:
                    print "Step by step mode..."
                    step_mode = True
            elif event.key == pygame.K_w:
                delay /= 2
                print delay
            elif event.key == pygame.K_s:
                delay *= 2
                print delay
            elif event.key == pygame.K_u:
                motor_lr.unhold()
                motor_ud.unhold()

        # Stop the fast mode keys.
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            elif event.key == pygame.K_RIGHT:
                move_right = False
            elif event.key == pygame.K_UP:
                move_up = False
            elif event.key == pygame.K_DOWN:
                move_down = False




    # write game logic here
    if move_left:
        motor_lr.move(1, 1, delay)
    elif move_right:
        motor_lr.move(-1, 1, delay)

    if move_up:
        motor_ud.move(1, 1, delay)
    elif move_down:
        motor_ud.move(-1, 1, delay)


    # clear the screen before drawing
    screen.fill((255, 255, 255))
    # write draw code here

    pygame.display.update()
    # run at 60 fps
    clock.tick(1000)

# close the window and quit
pygame.quit()
