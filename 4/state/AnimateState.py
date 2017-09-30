import pygame
from pygame.locals import *
from .GameState import GameState
from .SelectState import SelectState

class AnimateState(GameState):
    def __init__(self, stateSwitcher): super().__init__(stateSwitcher)
    def Event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_RETURN or event.key == K_SPACE or event.key == K_z: self.Switcher.Next()
            elif event.key == K_s: self.Switcher.Select(SelectState)
    def Draw(self, screen): screen.fill((0,255,0))
