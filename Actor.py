'''
base actor object
'''
from Vect2 import Vect2
import math
#from CONST import CONST
import pygame

class Actor(pygame.sprite.Sprite):

    BORDER_POLICY_NONE = 'None'
    BORDER_POLICY_WRAP = 'Wrap'
    BORDER_POLICY_CLIP = 'Clip'

    TOP_BORDER = 0
    RIGHT_BORDER = 1
    LEFT_BORDER = 2
    BOTTOM_BORDER = 3


    def __init__(self):

        super().__init__()  #call base class (Sprite)  __init__()


        #define the borders for the actor;  by default, this is the screen size
        infoObject = pygame.display.Info()  #use display.Info to retrieve the size of the screen
        pygame.display.set_mode((infoObject.current_w, infoObject.current_h))

        self.set_borders(0, infoObject.current_w-1, 0, infoObject.current_h-1)
        #border policy (choices are 'None', 'Clip' and 'Wrap'
        self.border_policy = {}
        self.border_policy[Actor.TOP_BORDER] = 'None'
        self.border_policy[Actor.BOTTOM_BORDER] = 'None'
        self.border_policy[Actor.LEFT_BORDER] = 'None'
        self.border_policy[Actor.RIGHT_BORDER] = 'None'

        #when we accelerate, the heading tells us in which direction
        self.__heading = Vect2(1, 0)

        #the default image will be a black 10x10 surface with a black colorkey
        self.__base_image = pygame.Surface((10, 10))
        self.__update_image()

        #maximum velocity (magnitude)
        self.max_velocity = 0       #no max

        self.location = Vect2(0, 0)     #units of pixels
        self.velocity = Vect2(0, 0)     #units of pixels/ms
        self.acceleration = Vect2(0, 0)     #units of pixels/ms/ms


    def __str__(self):
        return 'loc=' + str(self.location)  \
        + '; vel=' + str(self.velocity) \
        + '; accel=' + str(self.acceleration) \
        + '; heading=' + str(self.heading) \


    #heading property
    @property
    def heading(self):
        return self.__heading

    @heading.setter
    def heading(self, heading):
        '''ensure that the heading vector is always a unit vector'''
        self.__heading = heading.unit_vector()

        #generate the rotated image.  Update the image whenever its heading changes
        self.__update_image()


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
        '''location property used to enforce adherance to the selected border policy.'''
        self.__location = location

        if self.__location.x > self.borders[Actor.RIGHT_BORDER]:
            '''gone too far right'''
            if self.border_policy[Actor.RIGHT_BORDER] == 'Wrap':
                self.__location.x -= self.borders[Actor.RIGHT_BORDER] - self.borders[Actor.LEFT_BORDER]
            elif self.border_policy[Actor.RIGHT_BORDER] == 'Clip':
                self.__location.x = self.borders[Actor.RIGHT_BORDER]
            else:   #assume policy is 'None'
                pass

        if self.__location.x < self.borders[Actor.LEFT_BORDER]:
            '''gone too far left'''
            if self.border_policy[Actor.RIGHT_BORDER] == 'Wrap':
                self.__location.x += self.borders[Actor.RIGHT_BORDER] - self.borders[Actor.LEFT_BORDER]
            elif self.border_policy[Actor.RIGHT_BORDER] == 'Clip':
                self.__location.x = self.borders[Actor.LEFT_BORDER]
            else:   #assume policy is 'None'
                pass

        if self.__location.y > self.borders[Actor.BOTTOM_BORDER]:
            '''gone too far down'''
            if self.border_policy[Actor.BOTTOM_BORDER] == 'Wrap':
                self.__location.y -= self.borders[Actor.BOTTOM_BORDER] - self.borders[Actor.TOP_BORDER]
            elif self.border_policy[Actor.BOTTOM_BORDER] == 'Clip':
                self.__location.y = self.borders[Actor.BOTTOM_BORDER] - self.borders[Actor.TOP_BORDER]
            else:   #assume policy is 'None'
                pass

        if self.__location.y < self.borders[Actor.TOP_BORDER]:
            '''gone too far up'''
            if self.border_policy[Actor.TOP_BORDER] == 'Wrap':
                self.__location.y += self.borders[Actor.BOTTOM_BORDER] - self.borders[Actor.TOP_BORDER]
            elif self.border_policy[Actor.TOP_BORDER] == 'Clip':
                self.__location.y = self.borders[Actor.TOP_BORDER]
            else:   #assume policy is 'None'
                pass

        #calcuate the location of the image and store it in the inherited Sprite.rect Rect member
        self.rect.x = self.__location.x - self.__image_xcenter_offset
        self.rect.y = self.__location.y - self.__image_ycenter_offset


    def update_position(self, elapsed_ms):
        '''function to update position of Actor; call once every game loop; pass elapsed time since last call in ms'''
        #update the position of the object based on the time that has elapsed since the last call
        self.velocity += self.acceleration * elapsed_ms
        self.location += self.velocity * elapsed_ms


    def __update_image(self):
        '''function that generates __image, the base_image's rotated version'''
        imageAngleDeg = 180.0 * self.__heading.angle() / math.pi

        self.image = pygame.transform.rotate(self.__base_image, imageAngleDeg)

        #put the image's height and width in the inherited Sprite.rect Rect member
        #self.rect.width = self.__image.get_rect().width
        #self.rect.height = self.__image.get_rect().height
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)    #create a bit mask for use in collision detection

        #calculate the object's center offset
        self.__image_xcenter_offset = self.rect.width/2
        self.__image_ycenter_offset = self.rect.height/2


    def set_image(self, image, colorkey):
        '''sets the object's base image given the image filename and colorkey'''
        #the object's base screen image
        self.__base_image = pygame.image.load(image).convert()
        self.__base_image.set_colorkey(colorkey)

        #update the object's rotated screen image
        self.__update_image()


    def get_image(self):
        '''function that provides direct access to the actor's internal base image'''
        return self.__base_image


    def set_borders(self, left, right, top, bottom):
        '''function to limit the position of the actor on the screen'''
        self.borders = {}
        self.borders[Actor.LEFT_BORDER] = left
        self.borders[Actor.RIGHT_BORDER] = right
        self.borders[Actor.TOP_BORDER] = top
        self.borders[Actor.BOTTOM_BORDER] = bottom


if __name__ == "__main__":
    myObj = Actor()
    myObj.heading = Vect2(334, 343.2)
    print (myObj)


        
