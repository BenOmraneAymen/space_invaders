import pygame


def getImg(url):
    img = pygame.image.load(f'assets/img/{url}.png')
    return img


def getSound(url):
    sound = pygame.mixer.Sound(f"assets/audio/{url}.wav")

    return sound
