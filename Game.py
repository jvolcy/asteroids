'''
base game object
'''
import pygame
import math
from CONST import CONST #game constants
from Spaceship import Spaceship
from Vect2 import Vect2
from Phaser import Phaser
from Boulder import Boulder
import os
import random

class Game(object):


    def __init__(self, screen):
        super().__init__()

        self.screen = screen

        #the game's background image
        self.backgroundimage = None


    def __str__(self):
        return 'Game'




    def findFilesInDir(self, directory, extension):
        '''function that searches the specified 'directory' for files
        with the supplied extention.  The function returns a list of these files.'''
        foundFiles = []
        filenames = os.listdir(directory)
        for filename in filenames:
            if filename[-len(extension):] == extension:
                foundFiles.append(directory + '/' + filename)
                #print ('===>' + filename)
        return foundFiles


    def init(self):
        #get joystick controller
        self.num_joysticks = pygame.joystick.get_count()
        if self.num_joysticks == 0:
            print ("No joysticks found!")
            #done = True
        else:
            #use joystick 0
            print (self.num_joysticks,"joystick(s) found!")
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()

        #pygame.key.set_repeat(CONST.SCREEN_UPDATE_RATE, CONST.SCREEN_UPDATE_RATE)

        #load and setup background image
        self.background_image = pygame.image.load("pix/background.bmp").convert()


        #setup sprite lists

        #list of all actors
        self.actors = pygame.sprite.Group()

        #list of phasers
        self.phasers = pygame.sprite.Group()

        #list of boulders
        self.boulders = pygame.sprite.Group()



        #create a spaceship object
        self.spaceship = Spaceship()
        #add to the actors sprite list
        self.actors.add(self.spaceship)
        self.spaceship.set_image("pix/spaceship_idle.bmp", CONST.BLACK)

        self.spaceship.border_policy[Spaceship.TOP_BORDER] = 'Wrap'
        self.spaceship.border_policy[Spaceship.RIGHT_BORDER] = 'Wrap'
        self.spaceship.border_policy[Spaceship.LEFT_BORDER] = 'Wrap'
        self.spaceship.border_policy[Spaceship.BOTTOM_BORDER] = 'Wrap'


        #setup sound files
        self.spaceship_sound = pygame.mixer.Sound('sound/ship_idle.ogg')
        self.spaceship_sound_channel = self.spaceship_sound.play(loops=-1, maxtime=0, fade_ms=0)
        self.spaceship_sound_channel.set_volume(CONST.SOUND_SHIP_IDLE_VOLUME)

        self.phaser_sound = pygame.mixer.Sound('sound/laser.ogg')


        self.spaceship.location = Vect2(CONST.SCREEN_X_SIZE/2.0, CONST.SCREEN_Y_SIZE/2.0)
        self.spaceship.max_velocity = 0.3    #pixels/ms

        self.spaceship_angle = 0

        self.keyboard_dx = 0.0
        self.keyboard_dy = 0.0
        self.old_dy = 0      #used to check when dy changes
        #free_running_counter = 0

        #find every image file in the boulders folder
        self.boulder_files = self.findFilesInDir('pix/asteroids', '.bmp')
        #for f in boulder_files:
        #    print(f)


    def run(self, elapsed_time):
        done = False
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                #print(event.key)
                if event.key == pygame.K_LEFT:
                    self.keyboard_dx = -CONST.JOYSTICK_X_SCALE / 2
                elif event.key == pygame.K_RIGHT:
                    self.keyboard_dx = CONST.JOYSTICK_X_SCALE / 2
                elif event.key == pygame.K_UP:
                    self.keyboard_dy = -CONST.JOYSTICK_Y_SCALE / 2
                    #print(dy)
                elif event.key == pygame.K_DOWN:
                    self.keyboard_dy = CONST.JOYSTICK_Y_SCALE / 2
                    #print(dy)
                elif event.key == pygame.K_q:
                    done = True
                elif event.key == pygame.K_d:
                    print(self.spaceship, elapsed_time, len(self.phasers))
                elif event.key == pygame.K_SPACE:
                    self.phaser_sound.play()
                    new_phaser = Phaser(self.spaceship.location, self.spaceship.heading * CONST.PHASER_SPEED, CONST.PHASER_DISTANCE)
                    self.phasers.add(new_phaser)
                    self.actors.add(new_phaser)
                elif event.key == pygame.K_b:
                    #location, velocity, angular_velocity_dps, image
                    boulder_filename = self.boulder_files[random.randint(0, len(self.boulder_files)-1)]
                    new_boulder = Boulder( Vect2(320, 240), Vect2(0.2*random.random() - 0.1, 0.2*random.random() - 0.1), 60.0 * random.random() - 30, boulder_filename)
                    #new_boulder = Boulder( Vect2(320, 240), Vect2(0.2, 0.1), 20.0, "pix/asteroids/boulder1_120.bmp" )
                    new_boulder.border_policy[Spaceship.TOP_BORDER] = 'Wrap'
                    new_boulder.border_policy[Spaceship.RIGHT_BORDER] = 'Wrap'
                    new_boulder.border_policy[Spaceship.LEFT_BORDER] = 'Wrap'
                    new_boulder.border_policy[Spaceship.BOTTOM_BORDER] = 'Wrap'

                    self.boulders.add(new_boulder)
                    self.actors.add(new_boulder)
                    print("#boulders = ", len(self.boulders))

            if event.type == pygame.KEYUP:
                #print(event.key)
                if event.key == pygame.K_LEFT:
                    self.keyboard_dx = 0.0
                elif event.key == pygame.K_RIGHT:
                    self.keyboard_dx = 0.0
                elif event.key == pygame.K_UP:
                    self.keyboard_dy = 0.0
                    #print(dy)
                elif event.key == pygame.K_DOWN:
                    self.keyboard_dy = 0.0
                    #print(dy)

        dx = self.keyboard_dx
        dy = self.keyboard_dy

        # --- Game logic goes here


        if self.num_joysticks != 0:
            dx += CONST.JOYSTICK_X_SCALE * self.joystick.get_axis(CONST.JOYSTICK_X_AXIS)
            dy += CONST.JOYSTICK_Y_SCALE * self.joystick.get_axis(CONST.JOYSTICK_Y_AXIS)
            if self.joystick.get_button(5):
                self.phaser_sound.play()
                self.phasers.add(Phaser(self.spaceship.location, self.spaceship.heading * CONST.PHASER_SPEED, CONST.PHASER_DISTANCE))

        #only respond when the joystick is more than 10% of full scale
        if abs(dx) >= 0.1 * CONST.JOYSTICK_X_SCALE:
            self.spaceship_angle += dx
            self.spaceship.heading = Vect2(math.cos(-self.spaceship_angle), math.sin(self.spaceship_angle))

        if abs(dy) >= 0.1 * (-CONST.JOYSTICK_Y_SCALE):
            self.spaceship.acceleration = self.spaceship.heading * dy
        else:
            dy = 0
            self.spaceship.acceleration = Vect2(0, 0)
            self.spaceship.velocity *= 0.99

        #if the value of dy has changed, (i.e., the ship has accelerated) then change the spaceship image
        if dy != self.old_dy:
            if dy == 0:
                #when idling, the ship has no fire behind it
                self.spaceship.set_image("pix/spaceship_idle.bmp", CONST.BLACK)
                self.spaceship_sound_channel.set_volume(CONST.SOUND_SHIP_IDLE_VOLUME)
            else:
                #when the ship is accelerating, there is fire behind it
                self.spaceship.set_image("pix/spaceship.bmp", CONST.BLACK)
                self.spaceship_sound_channel.set_volume(CONST.SOUND_SHIP_VOLUME)

        self.old_dy = dy

        self.spaceship.update_position(elapsed_time)

        # --- Drawing code goes here

        #First, draw the background.  Place all other drawing code AFTER this command.
        self.screen.blit(self.background_image, [0, 0])


        for phaser in self.phasers:
            phaser.update_position(elapsed_time)
            #draw the phaser
            #phaser.blit_to_screen(self.screen)

            if phaser.end_of_life == True:
                self.phasers.remove(phaser)


        for boulder in self.boulders:
            boulder.update_position(elapsed_time)
            #boulder.blit_to_screen(self.screen)

        #draw the spaceship
        #spaceship.blit_to_screen(self.screen)

        #draw all sprites
        self.actors.draw(self.screen)
        return done


    def quit(self):
        self.spaceship_sound.fadeout(2000)

        if self.num_joysticks != 0:
            self.joystick.quit()






if __name__ == "__main__":
    myObj = Game()
    print (myObj)
