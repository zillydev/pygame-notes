import pygame, sys
from pygame.locals import *


pygame.init()
'''
initialises pygame
'''

screen_width = 400
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height), SCALED, vsync=True)
'''
This function creates a window surface of a specified size.
It takes a tuple as a paramater with two values - width and height.
The additional parameters sync the game with the monitor's refresh rate, getting rid of jitter.
We store this surface in the `screen` variable for future use.
The window screen is a basically a grid of pixels, onto which we can draw objects using the standard coordinate system of x-axis and y-axis and xy-coordinates.
The center of the coordinate system is at the top-left corner of the window screen.
The coordinate values are like this:
    x-axis: center-0, rightwards-positive, leftwards-negative
    y-axis: center-0, upwards-negative, downwards-positive
'''


pygame.display.set_caption('Hello World!')
'''
Sets the title of the window.
'''


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
'''
For colors, pygame uses a tuple with three values - Red, Green, and Blue - ranging from 0 to 255.
'''


while True:
    '''
    This loop will run infinitely for every frame, because the game needs to constantly fetch inputs, process game logic, and display graphics on the screen.
    '''


    for event in pygame.event.get():
        '''
        This for loop obtains every event that is occurring at the current frame, and loops through them.
        '''


        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            '''
            If there is a QUIT event detected (triggered when the 'Close (X)' button of the window is pressed), quit pygame and exit the program.
            '''


    screen.fill(white)
    '''
    Fills the screen with the specified color. Does this every frame, and necessary to clear previous frame's graphics to render new ones.
    '''


    pygame.display.update()
    '''
    Lets pygame know that the screen's data has changed, and needs to update. Also needs to happen every frame, for changes to be visible.
    '''


    pygame.time.Clock().tick(60)
    '''
    Locks the frame rate of the game to the specified value.
    '''
