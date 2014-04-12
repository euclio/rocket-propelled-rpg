from .entity import Entity, Player, NPC

def default_ordering(entity):
    return entity.speed


class Scene(object):
    def __init__(self, canvas, entities, order_key=default_ordering):
        if not order_key:
            self.order_key = default_ordering

        self.entities = entities
        self.order_key = order_key
        self.canvas = canvas


    def start(self):
        for entity in sorted(self.entities, key=self.order_key):
            action = entity.next_action()
            if action.requires_target():
                targets = entity.select_target(self.entities)
                action.execute(targets)
            else:
                action.execute()
