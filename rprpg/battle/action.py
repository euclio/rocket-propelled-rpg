import abc

class Action(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, requires_target):
        self.target = None
        self.requires_target = requires_target

    @abc.abstractmethod
    def execute(self):
        pass
