#Python 3D Positioning Test System
#uses a 3D matrix to create a three-axis coordinate system, which can be moved around using keyboard input

#pygame and all methods used are just for quick user input purposes, can and will be changed in the future
import pygame
#random is just used for testing 3D matrix coordinates and position movement, can be replaced with any display output
import random
#sys is just used to make the printNoLn method print to console, this parameter probably isn't even necessary but whatever 
import sys

#some pygame initialization stuff, pretty useless for anything besides user input
pygame.init()
clock = pygame.time.Clock()
displayWidth = 160
displayHeight = 90
window = pygame.display.set_mode((displayWidth, displayHeight))
window.fill((255,255,255))

#define printNoLn method, very handy method that prints to console without adding '\n' to the end of each line
def printNoLn(string):
    return print('%s'%string, sep = '', end = ',', file = sys.stdout)

#define printMstrix method, used to iterate through entire 3D matrix and print all values to console
def printMatrix(matrix):
    for dep in range(len(matrix)):
        for row in range(len(matrix[0])):
            for col in range(len(matrix[0][0])):
                printNoLn(matrix[dep][row][col])
            print('')
        print('')

#define main method
def main():
    l = int(input("Enter a length: "))
    w = int(input("Enter a width: "))
    h = int(input("Enter a height: "))
    dispX, dispY, dispZ = 0, 0, 0
    displayMatrix = [[[random.randint(0, 9) for x in range(w)] for y in range(h)] for z in range(l)]
    printMatrix(displayMatrix)
    printNoLn(displayMatrix[dispZ][dispY][dispX])
    repeat = True
    while repeat:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    repeat = False
                if event.key == pygame.K_LEFT:
                    if dispX > 0:
                        dispX -= 1
                    printNoLn(displayMatrix[dispZ][dispY][dispX])
                if event.key == pygame.K_RIGHT:
                    if dispX < (w-1):
                        dispX += 1
                    printNoLn(displayMatrix[dispZ][dispY][dispX])
                if event.key == pygame.K_DOWN:
                    if dispY < (h-1):
                        dispY += 1
                    printNoLn(displayMatrix[dispZ][dispY][dispX])
                if event.key == pygame.K_UP:
                    if dispY > 0:
                        dispY -= 1
                    printNoLn(displayMatrix[dispZ][dispY][dispX])
        
        clock.tick(60)
        pygame.display.flip()
    pygame.quit()

#execute main method
main()
