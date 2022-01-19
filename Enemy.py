from threading import Timer
import pygame

from Helpers import getImg


class Ennemy:
    def __init__(self, x, y, strength, screen):
        self.x = x
        self.y = y
        self.strength = strength
        self.width = 100
        self.height = 78
        self.image = pygame.image.load(f'assets/img/enemy{self.strength}.png')
        self.destroyed = False
        self.screen = screen

    def show(self):
        if(self.destroyed == False):
            self.screen.blit(self.image, (self.x, self.y))

    def destroy(self):
        self.destroyed = True
        # display explosion picture
