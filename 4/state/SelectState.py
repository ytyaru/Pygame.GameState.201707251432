import pygame
from pygame.locals import *
from .GameState import GameState

class SelectState(GameState):
    def __init__(self, stateSwitcher): super().__init__(stateSwitcher)
    def Event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_RETURN or event.key == K_SPACE or event.key == K_z: self.Switcher.Next()
    def Draw(self, screen): screen.fill((255,0,0))
