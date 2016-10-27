'''
base pygame script
'''
import pygame
import math
from CONST import CONST #game constants
from Spaceship import Spaceship
from Vect2 import Vect2


#initialize the pygame library
pygame.init()
done = False

screen = pygame.display.set_mode((CONST.SCREEN_X_SIZE, CONST.SCREEN_Y_SIZE))

pygame.display.set_caption("My Game")

#creae a clock to control screen update rate
clock = pygame.time.Clock()

#get joystick controller
num_joysticks = pygame.joystick.get_count()
if num_joysticks == 0:
    print ("No joysticks found!")
    #done = True
else:
    #use joystick 0
    print (num_joysticks,"joystick(s) found!")
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

#pygame.key.set_repeat(CONST.SCREEN_UPDATE_RATE, CONST.SCREEN_UPDATE_RATE)

#load and setup background image
background_image = pygame.image.load("pix/background.bmp").convert()

#create a spaceship object
spaceship = Spaceship()
spaceship.set_image("pix/spaceship.bmp", CONST.BLACK)

spaceship.border_policy[Spaceship.TOP_BORDER] = 'Wrap'
spaceship.border_policy[Spaceship.RIGHT_BORDER] = 'Wrap'
spaceship.border_policy[Spaceship.LEFT_BORDER] = 'Wrap'
spaceship.border_policy[Spaceship.BOTTOM_BORDER] = 'Wrap'


#spaceship.base_image = pygame.image.load("pix/actor_default.bmp").convert()

threshold = 0.2

#set a default spaceship image
#spaceship = spaceship_image

#spaceship.base_image.set_colorkey(CONST.BLACK)

#Main program loop
spaceship.location = Vect2(CONST.SCREEN_X_SIZE/2.0, CONST.SCREEN_Y_SIZE/2.0)
spaceship.max_velocity = 0.3    #pixels/ms

elapsed_time = 0
spaceship_angle = 0

keyboard_dx = 0.0
keyboard_dy = 0.0

while not done:

    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            #print(event.key)
            if event.key == pygame.K_LEFT:
                keyboard_dx = -CONST.JOYSTICK_X_SCALE / 2
            elif event.key == pygame.K_RIGHT:
                keyboard_dx = CONST.JOYSTICK_X_SCALE / 2
            elif event.key == pygame.K_UP:
                keyboard_dy = -CONST.JOYSTICK_Y_SCALE / 2
                #print(dy)
            elif event.key == pygame.K_DOWN:
                keyboard_dy = CONST.JOYSTICK_Y_SCALE / 2
                #print(dy)
            elif event.key == pygame.K_q:
                done = True
            elif event.key == pygame.K_d:
                print(spaceship, elapsed_time)

        if event.type == pygame.KEYUP:
            #print(event.key)
            if event.key == pygame.K_LEFT:
                keyboard_dx = 0.0
            elif event.key == pygame.K_RIGHT:
                keyboard_dx = 0.0
            elif event.key == pygame.K_UP:
                keyboard_dy = 0.0
                #print(dy)
            elif event.key == pygame.K_DOWN:
                keyboard_dy = 0.0
                #print(dy)

    dx = keyboard_dx
    dy = keyboard_dy

    # --- Game logic goes here
    if num_joysticks != 0:
        dx += CONST.JOYSTICK_X_SCALE * joystick.get_axis(CONST.JOYSTICK_X_AXIS)
        dy += CONST.JOYSTICK_Y_SCALE * joystick.get_axis(CONST.JOYSTICK_Y_AXIS)

    #only respond when the joystick is more than 10% of full scale
    if abs(dx) >= 0.1 * CONST.JOYSTICK_X_SCALE:
        spaceship_angle += dx
        spaceship.heading = Vect2(math.cos(-spaceship_angle), math.sin(spaceship_angle))
        #print(spaceship_angle*180/math.pi, spaceship.heading.angle()*180/math.pi)
        #print(spaceship)

    if abs(dy) >= 0.1 * (-CONST.JOYSTICK_Y_SCALE):
        spaceship.acceleration = spaceship.heading * dy
#        print(spaceship.heading * 5)
#        print(spaceship.heading * 0.000005)
        #print(dy, -0.1*CONST.JOYSTICK_Y_SCALE, spaceship.heading * 5)
    else:
        spaceship.acceleration = Vect2(0, 0)
    
    spaceship.update_position(elapsed_time)

    # --- Drawing code goes here

    #First, draw the background.  Place all other drawing code AFTER this command.
    screen.blit(background_image, [0, 0])

    #draw the spaceship
    spaceship.blit_to_screen(screen)

    # --- flip (update) the display
    pygame.display.flip()

    # --- limit the refresh rate
    elapsed_time = clock.tick(CONST.SCREEN_UPDATE_RATE)


if num_joysticks != 0:
    joystick.quit()

#close the window and quit
pygame.quit()

