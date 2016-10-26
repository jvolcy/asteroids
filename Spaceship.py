'''
Spaceship class
'''

from Actor import Actor
#import math
from CONST import CONST
#import pygame
from Vect2 import Vect2

class Spaceship(Actor):
    def __init__(self):
        #since we've overridden the base class's __init__ function, we must call it explicitly
        super(Spaceship, self).__init__()


    def __str__(self):
        return 'Spaceship: ' + super(Spaceship, self).__str__()

if __name__ == "__main__":
    mySpaceShip = Spaceship()
    mySpaceShip.heading = Vect2(334, 343.2)
    print (mySpaceShip)


        
