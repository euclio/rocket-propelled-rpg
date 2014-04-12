from . import entity

def default_ordering(entity):
    return entity.speed


class Scene(object):
    def __init__(self, displaysurf, entities, order_key=default_ordering):
        if not order_key:
            self.order_key = default_ordering

        self.entities = entities
        self.order_key = order_key


    def start(self):
        for entity in sorted(self.entities, key=self.order_key):
            action = entity.next_action(self.entities)
            if action.num_targets > 0:
                allowed_types = action.allowed_types
                targets = entity.select_target(self.entities, allowed_types)
                action.execute(entity, targets)
            else:
                action.execute(entity)
