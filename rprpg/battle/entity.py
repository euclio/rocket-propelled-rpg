import abc
import pygame
from . import action
from ..window import Window

import sys

class EntityType(object):
    NUM_DEFAULT_TYPES = 3
    All, Player, Enemy = range(NUM_DEFAULT_TYPES)

    @staticmethod
    def get_type(entity_type, entities):
        return [entity for entity in entities if entity.type == entity_type]


class AnimationType(object):
    NUM_ANIMATION_TYPES = 3
    Idle, Attack, Hurt = range(NUM_ANIMATION_TYPES)


class Entity(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, displaysurf, spritesheet, position=(0, 0)):
        self.displaysurf = displaysurf
        self.spritesheet = spritesheet
        self.strip = self.spritesheet.load_strip(pygame.Rect(0, 0, 400, 400), 3, colorkey=(255, 255, 255))
        self.animations = {}
        self.position = position

        displaysurf.blit(self.strip[0], position)

        # Default stats
        self.attack = 10
        self.defense = 5
        self.speed = 5
        self.hp = 20

    @property
    def bounding_box(self):
        return self.strip[0].get_rect()


    def set_location(self, x, y):
        self.position = x, y


    def register_animation(self, animation_type, sprite_tiles):
        self.animations[animation_type] = sprite_tiles


    @property
    @abc.abstractmethod
    def type(self):
        pass


    @abc.abstractmethod
    def next_action(self, entities):
        pass


    @abc.abstractmethod
    def select_target(self, entities, allowed_types):
        pass


    def animate(self):
        rect = self.strip[1].get_rect().copy()
        rect.move_ip(self.position)
        self.displaysurf.fill((0, 0, 0), rect=rect)
        self.displaysurf.blit(self.strip[1], self.position)



class Player(Entity):
    def __init__(self, displaysurf, spritesheet, position=None):
        super(Player, self).__init__(displaysurf, spritesheet, position)
        actionList = []
        actionList.append(action.Attack(self, EntityType.Enemy))

        currentSelection = 0
        self.currentSelection = currentSelection
        menuOptions = ["Attack"]
        menu = Window(menuOptions, 1024, (572+20), 0, 572, self.displaysurf, actionList)
        currentMenu = menu
        self.currentMenu = currentMenu
        self.currentMenu.highlight(currentSelection, self.displaysurf)

    @property
    def type(self):
        return EntityType.Player


    def next_action(self, entities):
        enemies = EntityType.get_type(EntityType.Enemy, entities)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    pygame.quit()
                    sys.exit()
                if (event.type == pygame.locals.KEYDOWN):
                    if event.key == pygame.K_UP and self.currentSelection > 0:
                        pastSelection = self.currentSelection
                        self.currentSelection =self.currentSelection-1
                        self.currentMenu.highlight(self.currentSelection,self.displaysurf)
                        self.currentMenu.unhighlight(pastSelection,self.displaysurf)
                    if event.key == pygame.K_DOWN and self.currentSelection < self.currentMenu.getSize()-1:
                        pastSelection = self.currentSelection
                        self.currentSelection = self.currentSelection+1
                        self.currentMenu.highlight(self.currentSelection,self.displaysurf)
                        self.currentMenu.unhighlight(pastSelection,self.displaysurf)
                    if event.key == pygame.K_RETURN:
                        action = self.currentMenu.select(self.currentSelection)
                        return action

                pygame.display.update()


    def select_target(self, entities, allowed_types):
        return [next(entity for entity in entities if entity.type in allowed_types)]


class Enemy(Entity):
    @property
    def type(self):
        return EntityType.Enemy


    def next_action(self, entities):
        enemies = EntityType.get_type(EntityType.Enemy, entities)
        return action.Attack(self, EntityType.Enemy)


    def select_target(self, entities, allowed_types):
        return [next(entity for entity in entities if entity.type in allowed_types)]
