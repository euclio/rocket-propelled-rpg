import pygame, sys
from pygame.locals import *
from rprpg.window import Window

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("RPRPG")

    currentSelection = 0
    mainMenuOptions=["Attack","Defend","Items","Run"]
    mainMenu = Window(mainMenuOptions, 768, (572+20), 0, 572,DISPLAYSURF)
    currentMenu = mainMenu
    currentMenu.highlight(currentSelection,DISPLAYSURF)

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            
            if (event.type==KEYDOWN) or (event.type == KEYUP):
                print("IN KEYDOWN")
                if event.key == pygame.K_UP and currentSelection > 0:
                    print("IN KEYUP")
                    pastSelection = currentSelection
                    currentSelection = currentSelection-1
                    currentMenu.highlight(currentSelection,DISPLAYSURF)
                    currentMenu.unhighlight(pastSelection,DISPLAYSURF)
                if event.key == pygame.K_DOWN and currentSelection < currentMenu.getSize():
                    pastSelection = currentSelection
                    currentSelection = currentSelection+1
                    currentMenu.highlight(currentSelection,DISPLAYSURF)
                    currentMenu.unhighlight(pastSelection,DISPLAYSURF)
                if event.key == pygame.K_RETURN:
                    currentMenu.select(currentSelection)

            pygame.display.update()

if __name__ == '__main__':
    main()
