'''
Boulder class
'''

from Actor import Actor
import math
#from CONST import CONST
#import pygame
from Vect2 import Vect2

class Boulder(Actor):
    def __init__(self, location, velocity, angular_velocity_dps, image):
        #since we've overridden the base class's __init__ function, we must call it explicitly
        super().__init__()
        self.location = location
        self.velocity = velocity    #in pixels/ms
        #angular velocity provided in degrees/sec (dps)
        #but stored in rads/msec (rpms)
        self.__angular_velocity_rpms = angular_velocity_dps*math.pi/180.0/1000.0
        self.__angle = 0    #default heading in rads

        self.end_of_life = False

        #self.set_image("pix/actor_default.bmp", (0,0,0))
        self.set_image(image, (255,255,255))

    def __str__(self):
        return 'Boulder: '  + super(Boulder, self).__str__()

    def update_position(self, elapsed_ms):
        '''function to update position of Phaser; call once every game loop; pass elapsed time since last call in ms'''

        self.__angle += elapsed_ms * self.__angular_velocity_rpms

        #keep __angle in the -pi to +pi range:
        if self.__angle > math.pi:
            self.__angle -= 2 * math.pi

        if self.__angle < -math.pi:
            self.__angle += 2 * math.pi

        #update the position of the object based on the time that has elapsed since the last call
        self.heading = Vect2.from_rads(self.__angle)

        super(Boulder, self).update_position(elapsed_ms)


if __name__ == "__main__":
    myBoulder = Boulder()
    myBoulder.heading = Vect2(334, 343.2)
    print (myBoulder)



