import pygame
from pygame.locals import *
from abc import ABCMeta, abstractmethod

class Main:
    def __init__(self, title=None):
        self.__title = title
        self.__screen = Screen()
        self.__stateSwitcher = StateSwitcher()
    def Run(self):
        pygame.init()
        if self.__title: pygame.display.set_caption(self.__title)
        clock = pygame.time.Clock()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); sys.exit();
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE: pygame.quit(); sys.exit();
                self.__stateSwitcher.State.Event(event)
            self.__stateSwitcher.State.Draw(self.__screen.Screen)
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
        for i, ins in enumerate(self.__states):
            if cls == type(ins): self.__now_state_index = i
    @property
    def State(self): return self.__states[self.__now_state_index]

class GameState(metaclass=ABCMeta):
    def __init__(self, stateSwitcher): self.__stateSwitcher = stateSwitcher
    @abstractmethod
    def Event(self, event): raise NotImplementedError()
    @abstractmethod
    def Draw(self, screen): raise NotImplementedError()
    @property
    def Switcher(self): return self.__stateSwitcher
class SelectState(GameState):
    def __init__(self, stateSwitcher): super().__init__(stateSwitcher)
    def Event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_RETURN or event.key == K_SPACE or event.key == K_z: self.Switcher.Next()
    def Draw(self, screen): screen.fill((255,0,0))
class AnimateState(GameState):
    def __init__(self, stateSwitcher): super().__init__(stateSwitcher)
    def Event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_RETURN or event.key == K_SPACE or event.key == K_z: self.Switcher.Next()
            elif event.key == K_s: self.Switcher.Select(SelectState)
    def Draw(self, screen): screen.fill((0,255,0))
class ResultState(GameState):
    def __init__(self, stateSwitcher): super().__init__(stateSwitcher)
    def Event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_RETURN or event.key == K_SPACE or event.key == K_z: self.Switcher.Next()
    def Draw(self, screen): screen.fill((0,0,255))

main = Main(title="ゲーム状態")
main.Run()
