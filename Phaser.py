'''
Phaser class
'''

from Actor import Actor
#import math
#from CONST import CONST
#import pygame
from Vect2 import Vect2

class Phaser(Actor):
    def __init__(self, location, velocity, life_distance):
        #since we've overridden the base class's __init__ function, we must call it explicitly
        super().__init__()
        self.location = location
        self.velocity = velocity    #in pixels/ms
        self.__time_ms = 0      #how long we've been alive
        speed = velocity.magnitude()
        self.__life_time_ms = life_distance / speed     #how long we will be alive
        self.end_of_life = False

        #self.set_image("pix/actor_default.bmp", (0,0,0))
        self.set_image("pix/phaser.bmp", (0,0,0))

    def __str__(self):
        return 'Phaser: time(ms)=' + str(self.__time_ms) + ' life time(ms) =' + str(self.__life_time_ms) + super(Phaser, self).__str__()

    def update_position(self, elapsed_ms):
        '''function to update position of Phaser; call once every game loop; pass elapsed time since last call in ms'''

        if self.__time_ms > self.__life_time_ms:
            self.end_of_life = True
            return

        #update the position of the object based on the time that has elapsed since the last call
        super(Phaser, self).update_position(elapsed_ms)
        self.__time_ms += elapsed_ms



if __name__ == "__main__":
    myPhaser = Phaser()
    myPhaser.heading = Vect2(334, 343.2)
    print (myPhaser)



