import pygame, sys
from pygame.locals import *
from rprpg.window import Window
from rprpg.battle.scene import Scene
from rprpg.battle.entity import Player, Enemy
from rprpg.render.spritesheet import SpriteSheet

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("RPRPG")

    spritesheet = SpriteSheet('rprpg/assets/biker.png')
    entities = [Player(DISPLAYSURF, spritesheet), Enemy(DISPLAYSURF, spritesheet)]
    battle = Scene(DISPLAYSURF, entities)
    battle.start()

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
          #  if (event.type==KEYDOWN):
           #     if event.key == pygame.K_UP and currentSelection > 0:
            #        pastSelection = currentSelection
             #       currentSelection = currentSelection-1
              #      currentMenu.highlight(currentSelection,DISPLAYSURF)
               #     currentMenu.unhighlight(pastSelection,DISPLAYSURF)
                #if event.key == pygame.K_DOWN and currentSelection < currentMenu.getSize()-1:
                 #   print(currentSelection)
                  #  pastSelection = currentSelection
                   # currentSelection = currentSelection+1
                    #currentMenu.highlight(currentSelection,DISPLAYSURF)
                    #currentMenu.unhighlight(pastSelection,DISPLAYSURF)
                #if event.key == pygame.K_RETURN:
                 #   currentMenu.select(currentSelection)

            pygame.display.update()

if __name__ == '__main__':
    main()
