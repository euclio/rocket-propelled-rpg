import pygame, sys
from pygame.locals import *
def main ():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("RPRPG")

    textBoxOffsetX = 768
    textBoxOffsetY = 572+20

    TRANSPARENCY = pygame.Color(0,0,0,0)
    textBox = pygame.image.load('textbox.bmp')

    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    menuTextList = []
    menuTextList.append(menuFontRender("Attack",fontObj))
    menuTextList.append(menuFontRender("Defend",fontObj))
    menuTextList.append(menuFontRender("Items",fontObj))
    menuTextList.append(menuFontRender("Run",fontObj))

    windowSurf = pygame.Surface((1024,768))
    windowSurf.fill(TRANSPARENCY)
    windowSurf.blit(textBox, (0,572))

    for text in menuTextList:
        textRectObj = text.get_rect()
        textRectObj.center = (textBoxOffsetX, textBoxOffsetY)
        windowSurf.blit(text, textRectObj)
        textBoxOffsetY += 50

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            DISPLAYSURF.blit(windowSurf,(0,0))    
            pygame.display.update()

#----
def menuFontRender (string,fontObj):
    textSurf = fontObj.render(string, True, (255,255,255))
    return textSurf

if __name__ == '__main__':
    main()
