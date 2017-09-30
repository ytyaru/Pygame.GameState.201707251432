from abc import ABCMeta, abstractmethod
class GameState(metaclass=ABCMeta):
    def __init__(self, stateSwitcher): self.__stateSwitcher = stateSwitcher
    @abstractmethod
    def Event(self, event): raise NotImplementedError()
    @abstractmethod
    def Draw(self, screen): raise NotImplementedError()
    @property
    def Switcher(self): return self.__stateSwitcher
