import pygame, sys
from pygame.locals import *

WHITE = (255,255,255,0)
YELLOW = (255,253,99,0)

class Window(object):


    def __init__(self, strings, sizeX, sizeY, posX, posY, DISPLAYSURF, action=None):

       
        self.action = action
        self.posX = posX
        self.posY = posY
        self.strings = strings
    
        textOffsetY = 30
        textOffsetX = (sizeX/2)

        menuSurf = pygame.Surface((sizeX, sizeY))
        menuSurf.fill((0,0,0,0))

        textBox = pygame.image.load('rprpg/assets/textbox.bmp')
        pygame.transform.scale(textBox, (sizeX, sizeY))
        menuSurf.blit(textBox, (0,0))
        self.menuSurf = menuSurf
        
        fontObj = pygame.font.Font('freesansbold.ttf',32)
        self.fontObj = fontObj
        menuOptions=[]
        self.menuOptions = menuOptions
        for string in strings:
            text = fontObj.render(string, True, WHITE)
            textRect=text.get_rect()
            textRect.center = (textOffsetX, textOffsetY)
            self.menuSurf.blit(text, textRect)
            textOffsetY += 40
            self.menuOptions.append([string, text, textRect, self.action])

        DISPLAYSURF.blit(menuSurf, (posX, posY))

    def highlight(self, selection,DISPLAYSURF):
        currentOption = self.menuOptions[selection]
        string = currentOption[0]
        currentOption[1] = self.fontObj.render(string, True, YELLOW)
        self.menuSurf.blit(currentOption[1],currentOption[2])
        DISPLAYSURF.blit(self.menuSurf, (self.posX, self.posY))


    def unhighlight(self, selection, DISPLAYSURF):
        currentOption = self.menuOptions[selection]
        string = currentOption[0]
        currentOption[1] = self.fontObj.render(string, True, WHITE)
        self.menuSurf.blit(currentOption[1],currentOption[2])
        DISPLAYSURF.blit(self.menuSurf, (self.posX, self.posY))

    def select(self, selection):
        currentOption = self.menuOptions[selection]
        currentAction = currentOption[3]
        currentAction.execute()

    def getSize(self):
        return len(self.menuOptions)
