'''
base pygame script
'''
import pygame
from CONST import CONST #game constants
import os
import Game


def findFilesInDir(directory, extension):
    '''function that searches the specified 'directory' for files
    with the supplied extention.  The function returns a list of these files.'''
    foundFiles = []
    filenames = os.listdir(directory)
    for filename in filenames:
        if filename[-len(extension):] == extension:
            foundFiles.append(directory + '/' + filename)
            #print ('===>' + filename)
    return foundFiles


def main():
    #initialize the pygame library
    pygame.init()

    #initialize sound mixer
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

    screen = pygame.display.set_mode((CONST.SCREEN_X_SIZE, CONST.SCREEN_Y_SIZE))

    pygame.display.set_caption("Asteroids")

    #creae a clock to control screen update rate
    clock = pygame.time.Clock()

    elapsed_time = 0

    done = False

    #instantian the game object
    game = Game.Game(screen)
    game.init()

    #Main program loop
    while not done:

        # --- run game loop
        done = game.run(elapsed_time)

        # --- flip (update) the display
        pygame.display.flip()

        # --- limit the refresh rate
        elapsed_time = clock.tick(CONST.SCREEN_UPDATE_RATE)


    game.quit()

    pygame.mixer.quit()

    #close the window and quit
    pygame.quit()



main()