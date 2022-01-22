import pygame

from Helpers import Helpers


class Bullet():
    bullets = []

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.bulletImg = Helpers.getImg("laser")
        self.is_fire = False
        self.destroy = False
        self.screen = screen

    def set_fire(self, val):
        self.is_fire = val

    def show(self):
        if(self.is_fire and not self.destroy):
            self.screen.blit(self.bulletImg, (self.x, self.y))
            self.y -= 5
        # delete the object it hits an ennemy
        # delete the object it goes out of screen

    def __del__(self):
        self.x = 0
        self.y = 0
        self.destroy = True
