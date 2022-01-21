from threading import Timer
import pygame

from Helpers import Helpers


class Enemy:
    def __init__(self, x, y, strength, screen):
        self.x = x
        self.y = y
        self.strength = strength
        self.width = 100
        self.height = 78
        self.image = Helpers.getImg(f"enemy{self.strength}")
        self.destroyed = False
        self.screen = screen

    def show(self):
        if(self.destroyed == False):
            self.screen.blit(self.image, (self.x, self.y))

    def destroy(self):
        self.destroyed = True
        # display explosion picture
