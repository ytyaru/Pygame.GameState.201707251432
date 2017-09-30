import pygame, sys
from pygame.locals import *
from abc import ABCMeta, abstractmethod
import Screen
import state.StateSwitcher

class Main:
    def __init__(self, title=None):
        self.__title = title
        self.__screen = Screen.Screen()
        self.__stateSwitcher = state.StateSwitcher.StateSwitcher()
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


if __name__ == '__main__':
    main = Main(title="ゲーム状態")
    main.Run()
