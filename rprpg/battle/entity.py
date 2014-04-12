class EntityType(object):
    NUM_DEFAULT_TYPES = 3
    All, Player, Enemy = range(NUM_DEFAULT_TYPES)

class Entity(object):
    pass

class Player(Entity):
    pass

class NPC(Entity):
    pass
