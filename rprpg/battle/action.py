import abc

class Action(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, actor, acts_on):
        self.actor = actor
        self.acts_on = acts_on


    def execute(self, actor, targets=None):
        if not targets and self.num_targets > 0:
            raise ValueError('Attempted to execute an action that requires a '
                             'target without specifying a target')

        if len(targets) > self.num_targets:
            raise ValueError('More targets specified than allowed')

        self._apply(actor, targets)


    @property
    @abc.abstractmethod
    def num_targets(self):
        pass


    @abc.abstractmethod
    def _apply(self, actor, targets):
        pass

    @property
    @abc.abstractmethod
    def allowed_types(self):
        pass


def default_damage_function(attacker, defender):
    return attacker.attack - defender.defense


class Attack(Action):
    def __init__(self, actor, acts_on, damage_function=default_damage_function):
        super(Attack, self).__init__(actor, acts_on)
        self.damage_function = damage_function

    @property
    def num_targets(self):
        return 1

    def _apply(self, actor, targets):
        for target in targets:
            damage = self.damage_function(actor, target)
            target.hp -= damage

    @property
    def allowed_types(self):
        from .entity import EntityType
        if self.actor.type == EntityType.Player:
            return EntityType.Enemy,
        else:
            return EntityType.Player,
