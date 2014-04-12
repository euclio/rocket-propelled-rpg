import abc
import pygame
from . import action
from ..window import Window

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

    def __init__(self, displaysurf, spritesheet, position=None):
        self.spritesheet = spritesheet
        self.animations = {}
        self.position = position

        # Default stats
        self.attack = 10
        self.defense = 5
        self.speed = 5
        self.hp = 20


    def set_location(self, x, y):
        self.position = x, y


    def register_animation(self, animation_type, sprite_tiles):
        self.animations[animation_type] = sprite_tiles


    def animate(self, animation_type):
        frames = self.spritesheet.get_frames(self.animations[animation_type])
        for frame in frame:
            print('hi')

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


class Player(Entity):
    def __init__(self, displaysurf, spritesheet, position=None):
        super(Player, self).__init__(displaysurf, spritesheet, position)

    @property
    def type(self):
        return EntityType.Player


    def next_action(self, entities):
        enemies = EntityType.get_type(EntityType.Enemy, entities)
        return action.Attack(self, EntityType.Enemy)


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
