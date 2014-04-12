import abc

class Action(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, acts_on, targets):
        self.acts_on = acts_on
        self.targets = targets


    def execute(self, targets=None):
        if not targets and self.requires_target:
            raise ValueError('Attempted to execute an action that requires a '
                             'target without specifying a target')

        if len(targets) > len(self.targets):
            raise ValueError('More targets specified than allowed')

        self._apply(targets)


    def requires_target(self):
        return self.targets > 0


    @abc.abstractmethod
    def _apply(self, targets):
        pass
