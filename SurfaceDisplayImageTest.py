"""
A test module for experimenting with display, Surface, image, and PixelArray
"""

import random
import pygame

pygame.init()

#define printNoLn method, very handy method that prints to console without adding '\n' to the end of each line
def printNoLn(string):
    return print('%s'%string, sep = '', end = ',')

#define randomColor method, returns (you guessed it!) a random RGB triple
def randomColor():
    return (random.randint(0, 255), random.randint(0,255), random.randint(0, 255))

def main():
    clock = pygame.time.Clock()
    displayWidth = 160
    displayHeight = 90
    
    #creates a Surface object named screen with width and height parameters
    screen = pygame.display.set_mode((displayWidth, displayHeight))

    #creates an array that represents the PixelArray wrapping the screen Surface, 
    #prints the Surface that PixelArray is wrapping (which is screen)
    #not a lot of progress towards displaying an image, but I'm beginning to understand how everything fits together with these objects and classes 
    screenArray = pygame.PixelArray(screen)
    print(screenArray.surface)


    repeat = True
    while repeat:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                repeat = False



    clock.tick(60)
    pygame.quit()

main()
