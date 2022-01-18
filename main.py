import pygame
from Enemy import Ennemy
import button
from Bullet import Bullet
from Player import Player

pygame.init()
# create the screen
screen = pygame.display.set_mode((800, 600))
# Design
pygame.display.set_caption('project:space  ')
background = pygame.image.load('assets/img/background.png')
music = pygame.mixer.Sound("assets/audio/background_music.mp3")
music.play(-1)


def main_menu(screen):
    running = True
    title = pygame.image.load('assets/img/space-invaders-logo.png')
    tune1 = pygame.image.load('assets/img/tune1.png')
    tune2 = pygame.image.load('assets/img/tune2.png')
    start_img = pygame.image.load('assets/img/start_btn.png').convert_alpha()
    exit_img = pygame.image.load('assets/img/exit_btn.png').convert_alpha()
    start_button = button.Button(300, 350, start_img, 0.7, screen=screen)
    exit_button = button.Button(300, 450, exit_img, 0.7, screen=screen)
    tune1_btn = button.Button(700, 500, tune1, 0.3, screen=screen)
    tune2_btn = button.Button(50, 500, tune2, 0.3, screen=screen)
    while running:
        screen.fill((200, 200, 200))
        screen.blit(background, (0, 0))
        screen.blit(title, (100, 50))
        if start_button.draw():
            print('START')
            running = False
            level()
        if exit_button.draw():
            print('EXIT')
            running = False
        tune1_btn.draw()
        tune2_btn.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


def finish(wl):
    start_img = pygame.image.load('assets/img/start_btn.png').convert_alpha()
    exit_img = pygame.image.load('assets/img/exit_btn.png').convert_alpha()
    youWin = pygame.image.load('assets/img/youWin.png')
    youLoss = pygame.image.load('assets/img/youLoss.png')
    start_button = button.Button(300, 350, start_img, 0.7, screen=screen)
    exit_button = button.Button(300, 450, exit_img, 0.7, screen=screen)
    running = True
    while running:
        screen.fill((200, 200, 200))
        screen.blit(background, (0, 0))
        if(wl == "win"):
            screen.blit(youWin, (125, 50))
        else:
            screen.blit(youLoss, (200, 100))
        if start_button.draw():
            print('START')
            running = False
            level()
        if exit_button.draw():
            print('EXIT')
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


def level():
    pick = pygame.image.load('assets/img/pick.png')
    lvl1 = pygame.image.load('assets/img/num1.png').convert_alpha()
    lvl2 = pygame.image.load('assets/img/num2.png').convert_alpha()
    lvl3 = pygame.image.load('assets/img/num3.png').convert_alpha()
    lvl4 = pygame.image.load('assets/img/num4.png').convert_alpha()
    lvl5 = pygame.image.load('assets/img/num5.png').convert_alpha()
    btn_lvl1 = button.Button(100, 250, lvl1, 0.2, screen=screen)
    btn_lvl2 = button.Button(225, 250, lvl2, 0.2, screen=screen)
    btn_lvl3 = button.Button(350, 250, lvl3, 0.2, screen=screen)
    btn_lvl4 = button.Button(475, 250, lvl4, 0.2, screen=screen)
    btn_lvl5 = button.Button(600, 250, lvl5, 0.2, screen=screen)
    running = True
    while running:
        screen.fill((200, 200, 200))
        screen.blit(background, (0, 0))
        screen.blit(pick, (50, 50))
        if btn_lvl1.draw():
            game(background, 0.1)
            running = False
        if btn_lvl2.draw():
            game(background, 0.2)
            running = False
        if btn_lvl3.draw():
            game(background, 0.3)
            running = False
        if btn_lvl4.draw():
            game(background, 0.4)
            running = False
        if btn_lvl5.draw():
            game(background, 1)
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


def game(bg, speed):
    player = Player(screen=screen)
    score = 0
    enemy = Ennemy(20, 20, 2, screen=screen)
    enemy2 = Ennemy(20, 120, 3, screen=screen)
    enemy3 = Ennemy(20, 220, 4, screen=screen)
    enemy4 = Ennemy(20, 320, 2, screen=screen)
    enemy5 = Ennemy(120, 220, 3, screen=screen)
    enemy6 = Ennemy(120, 320, 1, screen=screen)
    enemies = [enemy6, enemy5, enemy4, enemy3, enemy2, enemy]
    shoot_sound = pygame.mixer.Sound("assets/audio/laserShoot.wav")
    explosion_sound = pygame.mixer.Sound("assets/audio/explosion.wav")
    damage_sound = pygame.mixer.Sound("assets/audio/explosion1.wav")

    # looping the function
    running = True
    while running:
        screen.fill((200, 200, 200))
        screen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.QUIT()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.key.set_repeat(100)
                    player.fire()
                    shoot_sound.play()
                pygame.key.set_repeat(500)
                player.move(event.key)
        # show the player
        player.show()
        for enemy in enemies:
            enemy.show()
            enemy.y += speed
            if(enemy.y > player.y-player.height and enemy.destroyed == False):
                running = False
                finish("lost")

        # show the bullets if exist

        for bullet in Bullet.bullets:
            if(bullet.destroy):
                continue
            bullet.show()

            for enemy in enemies:
                if((enemy.x < bullet.x < (enemy.x+enemy.width)) and (enemy.y < bullet.y < (enemy.y + enemy.height)) and (not enemy.destroyed) and (not bullet.destroy)):
                    enemy.strength -= 1
                    bullet.destroy = True
                    if(enemy.strength == 0):
                        score += 1
                        explosion_sound.play()
                        enemy.destroyed = True
                    else:
                        damage_sound.play()
                if(score == len(enemies)):
                    for bullet in Bullet.bullets:
                        bullet.destroy = True
                    running = False
                    finish("win")

        pygame.display.update()


main_menu(screen)
