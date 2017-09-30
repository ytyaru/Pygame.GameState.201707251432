import pygame
from pygame.locals import *
from abc import ABCMeta, abstractmethod

class Main:
    def __init__(self, title=None):
        self.__title = title
        self.__screen = Screen()
        self.__states = [SelectState(), AnimateState(), ResultState()]
        self.__now_state_index = 0
    def __next_state(self):
        self.__now_state_index += 1
        if len(self.__states) <= self.__now_state_index: self.__now_state_index = 0
    def Run(self):
        pygame.init()
        if self.__title: pygame.display.set_caption(self.__title)
        clock = pygame.time.Clock()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); sys.exit();
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE: pygame.quit(); sys.exit();
                self.__states[self.__now_state_index].Event(event, self.__next_state)
            self.__states[self.__now_state_index].Draw(self.__screen.Screen)
            pygame.display.flip()
            clock.tick(60) # 60 FPS
class Screen:
    def __init__(self, width=320, height=240, color=[0,0,0]):
        self.__color = color
        self.__size = (width, height)
        self.__screen = pygame.display.set_mode(self.__size)
    @property
    def Screen(self): return self.__screen
    @property
    def Size(self): return self.__size
    @property
    def Color(self): return self.__color
    def Fill(self): self.__screen.fill(self.__color)
class GameState(metaclass=ABCMeta):
    @abstractmethod
    def Event(self, event, nextState): raise NotImplementedError()
    @abstractmethod
    def Draw(self, screen): raise NotImplementedError()
class SelectState(GameState):
    def Event(self, event, nextState):
        if event.type == KEYDOWN:
            if event.key == K_KP_ENTER or event.key == K_SPACE or event.key == K_z: nextState()
    def Draw(self, screen): screen.fill((255,0,0))
class AnimateState(GameState):
    def Event(self, event, nextState):
        if event.type == KEYDOWN:
            if event.key == K_KP_ENTER or event.key == K_SPACE or event.key == K_z: nextState()
    def Draw(self, screen): screen.fill((0,255,0))
class ResultState(GameState):
    def Event(self, event, nextState):
        if event.type == KEYDOWN:
            if event.key == K_KP_ENTER or event.key == K_SPACE or event.key == K_z: nextState()
    def Draw(self, screen): screen.fill((0,0,255))

main = Main(title="ゲーム状態")
main.Run()
