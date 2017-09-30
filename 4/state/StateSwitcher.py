import pygame
from pygame.locals import *
from abc import ABCMeta, abstractmethod
from .GameState import GameState
from .SelectState import SelectState
from .AnimateState import AnimateState
from .ResultState import ResultState

class StateSwitcher:
    def __init__(self):
        self.__states = [c(self) for c in [SelectState, AnimateState, ResultState]]
        self.__now_state_index = 0
    def Next(self):
        self.__now_state_index += 1
        if len(self.__states)-1 < self.__now_state_index: self.__now_state_index = 0
    def Prev(self):
        self.__now_state_index -= 1
        if self.__now_state_index < 0: self.__now_state_index = len(self.__states)-1
    def First(self): self.__now_state_index = 0
    def Last(self): self.__now_state_index = len(self.__states)-1
    def Select(self, cls):
        if not issubclass(cls, GameState): return
        for i, ins in enumerate(self.__states):
            if cls == type(ins): self.__now_state_index = i
    @property
    def State(self): return self.__states[self.__now_state_index]

