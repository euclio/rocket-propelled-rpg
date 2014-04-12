import pygame, sys
from pygame.locals import *
from rprpg.window import Window

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("RPRPG")

    currentSelection = 0
    mainMenuOptions=["Attack","Defend","Items","Run"]
    mainMenu = Window(mainMenuOptions, 1024, (572+20), 0, 572,DISPLAYSURF)
    currentMenu = mainMenu
    currentMenu.highlight(currentSelection,DISPLAYSURF)

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if (event.type==KEYDOWN):
                if event.key == pygame.K_UP and currentSelection > 0:
                    pastSelection = currentSelection
                    currentSelection = currentSelection-1
                    currentMenu.highlight(currentSelection,DISPLAYSURF)
                    currentMenu.unhighlight(pastSelection,DISPLAYSURF)
                if event.key == pygame.K_DOWN and currentSelection < currentMenu.getSize()-1:
                    print(currentSelection)
                    pastSelection = currentSelection
                    currentSelection = currentSelection+1
                    currentMenu.highlight(currentSelection,DISPLAYSURF)
                    currentMenu.unhighlight(pastSelection,DISPLAYSURF)
                if event.key == pygame.K_RETURN:
                    currentMenu.select(currentSelection)

            pygame.display.update()

if __name__ == '__main__':
    main()
