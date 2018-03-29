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
    displayWidth = 800
    displayHeight = 450
    
    #creates a display Surface object named screen with width and height parameters, defaults to black
    screen = pygame.display.set_mode((displayWidth, displayHeight))
    
    print(screen.get_at((80,45)))
    #set a single pixel at (80, 45) to color (255, 255, 255) a.k.a. white
    screen.set_at((80, 45), (255, 255, 255))
    print(screen.get_at((80, 45)))
    
    #creates an array that represents the PixelArray wrapping the screen Surface, 
    #prints the Surface that PixelArray is wrapping (which is screen) 
    screenArray = pygame.PixelArray(screen)
    print(screenArray.surface)
    #prints the dimensions of the screenArray
    print(screenArray.shape)
    
    
    #create a Surface object directly using pygame.Surface()
    screenTest = pygame.Surface((displayWidth / 2, displayHeight / 2))
    screenTest.fill((0, 255, 100))
    
    array3D = []
    for i in range(5):
    #fills screen with randomly colored pixels, VERY SLOWLY (approx. 0.001 fps)
        for j in range(0, displayHeight):
            for k in range(0, displayWidth):
                array3D[i][j].append(randomColor())
            array3D[i].append([])
        array3D.append([])
    array3D.remove([])
    
    repeat = True
    while repeat:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                repeat = False
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed(K_SPACE):
                    #iterate through list of pixel arrays, set screen to each pixel array
                    pygame.surfarray.blit_array(screen, array)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

main()
