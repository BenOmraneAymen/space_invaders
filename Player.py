import pygame

from Bullet import Bullet


class Player:
    def __init__(self, screen):
        self.playerImg = pygame.image.load("assets/img/space-invaders.png")
        self.x = 370
        self.y = 500
        self.height = 70
        self.width = 90
        self.val = 30
        self.score = 0
        self.screen = screen

    def show(self):
        self.screen.blit(self.playerImg, (self.x, self.y))

    def move(self, key):
        if key == pygame.K_RIGHT and self.x < 736:
            self.x += self.val
        elif key == pygame.K_LEFT and self.x > 0:
            self.x -= self.val
        elif key == pygame.K_UP and self.y > 0:
            self.y -= self.val
        elif key == pygame.K_DOWN and self.y < 536:
            self.y += self.val

    def fire(self):
        bullet = Bullet(self.x + 35, self.y, screen=self.screen)
        bullet.set_fire(True)
        Bullet.bullets.append(bullet)
        for bullet in Bullet.bullets:
            bullet.show()
