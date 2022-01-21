import pygame


class Helpers:
    @staticmethod
    def getImg(url):
        img = pygame.image.load(f'assets/img/{url}.png')
        return img

    @staticmethod
    def getSound(url):
        sound = pygame.mixer.Sound(f"assets/audio/{url}.wav")
        return sound
