'''
base game object
'''

class Game(object):


    def __init__(self, screen_width = 0, screen_height = 0):

        #the game's background image
        self.backgroundimage = None


    def __str__(self):
        return 'Game'


if __name__ == "__main__":
    myObj = Game()
    print (myObj)


        
