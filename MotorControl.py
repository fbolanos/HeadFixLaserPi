import pygame
from BipolarStepperMotor import BipolarStepperMotor



# motor object to be controlled
motor = BipolarStepperMotor(19,26,20,21)

# initialize game engine
pygame.init()
# set screen width/height and caption
size = [640, 480]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My Game')
# initialize clock. used later in the loop.
clock = pygame.time.Clock()

# Loop until the user clicks close button
done = False
step_mode = False
delay = 0.1
while done == False:
    # write event handlers here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if step_mode:
                    motor.move(1, 1, 0)
                else:
                    move_left = True
            elif event.key == pygame.K_RIGHT:
                if step_mode:
                    motor.move(-1, 1, 0)
                else:
                    move_right = True
            elif event.key == pygame.K_s:
                if step_mode:
                    step_mode = False
                else:
                    step_mode = True

            elif event.key == pygame.K_UP:
                delay /= 2
                print delay
            elif event.key == pygame.K_DOWN:
                delay *= 2
                print delay
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            elif event.key == pygame.K_RIGHT:
                move_right = False




    # write game logic here
    if move_left:
        motor.move(1,1,delay)
    elif move_right:
        motor.move(-1,1,delay)


    # clear the screen before drawing
    screen.fill((255, 255, 255))
    # write draw code here

    # display what’s drawn. this might change.
    pygame.display.update()
    # run at 60 fps
    clock.tick(60)

# close the window and quit
pygame.quit()