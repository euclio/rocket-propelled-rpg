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
        for the_entity in sorted(self.entities, key=self.order_key):
            action = the_entity.next_action(self.entities)
            if action.num_targets > 0:
                allowed_types = action.allowed_types
                targets = the_entity.select_target(self.entities, allowed_types)
                action.execute(the_entity, targets)
                the_entity.animate()
            else:
                action.execute(the_entity)
