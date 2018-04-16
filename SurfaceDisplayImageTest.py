"""
A test module for experimenting with display, Surface, image, and PixelArray
"""

import random
import pygame

pygame.init()

#define printNoLn method, very handy method that prints to console without adding '\n' to the end of each line
def printNoLn(string):
    return print('%s'%string, sep = '', end = ',')

#define randomColor method, returns a random RGB triple
def randomColor():
    return (random.randint(0, 255), random.randint(0,255), random.randint(0, 255))

#define screenDisplay method
def screenDisplay(height, width, screen, inputArray):
    for i in range(0, height):
        for j in range(0, width):
            screen.set_at((j, i), inputArray[i][j])

def main():
    clock = pygame.time.Clock()
    displayWidth = 160
    displayHeight = 90
    length = 5
    layer = 0
    
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
    
    #attempt to use numpy and pygame.surfarray to create and blit an array of random pixels to a Surface
    x = 1
    y = 1
    z = 1
    array3D = [[[]]]
    for i in range(0, length):
        for j in range(0, displayHeight):
            for k in range(0, displayWidth):
                print ("Added pixel ||| layer: " + str(z) + " ||| height: " + str(y) + " ||| width: " + str(x))
                x += 1
                array3D[i][j].append(randomColor())
            y += 1
            x = 1
            array3D[i].append([])
        z += 1
        y = 1
        x = 1
        array3D.append([[]])

    screenDisplay(displayHeight, displayWidth, screen, array3D[layer])
    repeat = True
    while repeat:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                repeat = False
        string = input("Enter a direction: ")
        if string == "up" and layer < (length - 1):
            layer += 1
            print("Moving up one layer")
            #iterate through list of pixel arrays, set screen to each pixel array
            screenDisplay(displayHeight, displayWidth, screen, array3D[layer])
        elif string == "down" and layer > 0:
            layer -= 1
            print("Moving down one layer")
            #iterate through list of pixel arrays, set screen to each pixel array
            screenDisplay(displayHeight, displayWidth, screen, array3D[layer])
        elif string == "quit":
            repeat = False

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

main()
