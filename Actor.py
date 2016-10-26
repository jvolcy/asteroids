'''
base actor object
'''
from Vect2 import Vect2
import math
from CONST import CONST
import pygame

class Actor(object):


    def __init__(self, screen_width = 0, screen_height = 0):
        #maximum velocity (magnitude)
        self.max_velocity = 0       #no max

        self.location = Vect2(0, 0)     #units of pixels
        self.velocity = Vect2(0, 0)     #units of pixels/ms
        self.acceleration = Vect2(0, 0)     #units of pixels/ms/ms
        #when we accelerate, the heading tells us in which direction
        self.heading = Vect2(0, 0)

        #where we want to end up
        self.destination = Vect2(0, 0)  #units of pixels

        #the object's screen image
        self.image = None

        #border behaviors (choices are 'None', 'Clip' and 'Wrap'
        self.border_behavior = {}
        self.border_behavior["TOP_BORDER"] = "None"
        self.border_behavior["BOTTOM_BORDER"] = "None"
        self.border_behavior["LEFT_BORDER"] = "None"
        self.border_behavior["RIGHT_BORDER"] = "None"

        # self.border = {}
        # self.border["TOP_BORDER"] = self.image.height/2
        # self.border["BOTTOM_BORDER"] = screen_height-1 - self.image.height/2
        # self.border["LEFT_BORDER"] = self.image.width/2
        # self.border["RIGHT_BORDER"] = screen_width-1 - self.image.width/2

    def __str__(self):
        return 'loc=' + str(self.location)  \
        + '; vel=' + str(self.velocity) \
        + '; accel=' + str(self.acceleration) \
        + '; heading=' + str(self.heading) \


    #image property
    @property
    def oriented_image(self):
        imageAngleDeg = 180.0 * self.heading.angle() / math.pi
        return pygame.transform.rotate(self.image, imageAngleDeg)

    #heading property
    @property
    def heading(self):
        return self.__heading

    @heading.setter
    def heading(self, heading):
        '''ensure that the heading vector is always a unit vector'''
        self.__heading = heading.unit_vector()


   #velocity property
    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity):
        '''ensure that the velocity does not exceed the max'''
        if self.max_velocity > 0 and velocity.magnitude() > self.max_velocity:
            #keep the direction, change the magnitude
            self.__velocity = velocity.unit_vector() * self.max_velocity
        else:
            self.__velocity = velocity

    #location property
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        '''ensure that the location vector adheres to the selected border location behavior'''
        self.__location = location


    def update_position(self, elapsed_ms):
        '''function to update position of Actor; call once every game loop; pass elapsed time since last call in ms'''
        #update the position of the object based on the time that has elapsed since the last call
        self.velocity += self.acceleration * elapsed_ms
        self.location += self.velocity * elapsed_ms



if __name__ == "__main__":
    myObj = Actor()
    myObj.heading = Vect2(334, 343.2)
    print (myObj)


        
