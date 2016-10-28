'''
game constants
'''

class CONST:
    #define some colors constants
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0 , 0)
    BLUE = (0, 0, 255)

    #set the width and height of the screen
    SCREEN_X_SIZE = 700
    SCREEN_Y_SIZE = 500

    #set the screen update rate (frames per second)
    SCREEN_UPDATE_RATE = 15

    #joystick controls
    LEFT_JOYSTICK_X_AXIS = 0
    LEFT_JOYSTICK_Y_AXIS = 1
    RIGHT_JOYSTICK_X_AXIS = 2
    RIGHT_JOYSTICK_Y_AXIS = 3

    JOYSTICK_X_AXIS = LEFT_JOYSTICK_X_AXIS
    JOYSTICK_Y_AXIS = LEFT_JOYSTICK_Y_AXIS

    JOYSTICK_X_SCALE = 0.1     #controls spaceship angle in radians
    JOYSTICK_Y_SCALE = -0.0001     #controls spaceship Y acceleration

    PHASER_SPEED = .3
    PHASER_DISTANCE = 200
