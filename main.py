import pygame
import Button
from Bullet import Bullet
from Helpers import Helpers
from Player import Player
from threading import Timer

from StartUp import Startup


pygame.init()
# create the screen
screen = pygame.display.set_mode((800, 600))
# Design
pygame.display.set_caption('project:space invaders ')
background = Helpers.getImg('background')
music = Helpers.getSound("background_music")
music.play(-1)


def main_menu(screen):
    running = True
    sound = True
    title = Helpers.getImg("space-invaders-logo")
    tune1 = Helpers.getImg('tune1')
    start_img = Helpers.getImg('start_btn').convert_alpha()
    exit_img = Helpers.getImg('exit_btn').convert_alpha()
    start_button = Button.Button(300, 350, start_img, 0.7, screen=screen)
    exit_button = Button.Button(300, 450, exit_img, 0.7, screen=screen)
    tune1_btn = Button.Button(700, 500, tune1, 0.3, screen=screen)
    while running:
        screen.fill((200, 200, 200))
        screen.blit(background, (0, 0))
        screen.blit(title, (100, 50))
        if start_button.draw():
            running = False
            level(sound)
        if exit_button.draw():
            # print('EXIT')
            running = False
        if tune1_btn.draw():
            if sound == True:
                music.stop()
                sound = False
            else:
                music.play()
                sound = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


def finish(wl, sound):
    start_img = Helpers.getImg("start_btn") .convert_alpha()
    exit_img = Helpers.getImg("exit_btn").convert_alpha()
    youWin = Helpers.getImg("youWin")
    youLoss = Helpers.getImg("youLoss")
    tune1 = Helpers.getImg('tune1')

    start_button = Button.Button(300, 350, start_img, 0.7, screen=screen)
    exit_button = Button.Button(300, 450, exit_img, 0.7, screen=screen)
    tune1_btn = Button.Button(700, 500, tune1, 0.3, screen=screen)
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
            level(sound)
        if exit_button.draw():
            # print('EXIT')
            running = False
        if tune1_btn.draw():
            if sound == True:
                music.stop()
                sound = False
            else:
                music.play()
                sound = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


def level(sound):
    pick = Helpers.getImg('pick')
    tune1 = Helpers.getImg('tune1')
    lvl1 = Helpers.getImg('num1').convert_alpha()
    lvl2 = Helpers.getImg('num2').convert_alpha()
    lvl3 = Helpers.getImg('num3').convert_alpha()
    lvl4 = Helpers.getImg('num4').convert_alpha()
    lvl5 = Helpers.getImg('num5').convert_alpha()
    tune1_btn = Button.Button(700, 500, tune1, 0.3, screen=screen)

    btn_lvl1 = Button.Button(100, 250, lvl1, 0.2, screen=screen)
    btn_lvl2 = Button.Button(225, 250, lvl2, 0.2, screen=screen)
    btn_lvl3 = Button.Button(350, 250, lvl3, 0.2, screen=screen)
    btn_lvl4 = Button.Button(475, 250, lvl4, 0.2, screen=screen)
    btn_lvl5 = Button.Button(600, 250, lvl5, 0.2, screen=screen)
    running = True
    while running:
        screen.fill((200, 200, 200))
        screen.blit(background, (0, 0))
        screen.blit(pick, (50, 50))
        if btn_lvl1.draw():
            game(background, 0.1, sound)
            running = False
        if btn_lvl2.draw():
            game(background, 0.2, level=2, sound=sound)
            running = False
        if btn_lvl3.draw():
            game(background, 0.3, level=3, sound=sound)
            running = False
        if btn_lvl4.draw():
            game(background, 0.4, level=4, sound=sound)
            running = False
        if btn_lvl5.draw():
            game(background, 1, level=5, sound=sound)
            running = False
        if tune1_btn.draw():
            if sound == True:
                music.stop()
                sound = False
            else:
                music.play()
                sound = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


def display_score(x, y, score):
    font = pygame.font.SysFont('comicsansms', 30)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (x, y))


def game(bg, speed, sound, level=1):
    player = Player(screen=screen)
    # read level and enemy from file
    startup = Startup(screen, level)
    ennemies = startup.init_ennemies()
    shoot_sound = Helpers.getSound("laserShoot")
    explosion_sound = Helpers.getSound("explosion")
    damage_sound = Helpers.getSound("explosion1")

    # looping the function
    explosionList = []

    running = True
    while running:
        screen.fill((200, 200, 200))
        screen.blit(bg, (0, 0))
        current_time = pygame.time.get_ticks()

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
        for enemy in ennemies:
            enemy.show()
            enemy.y += speed
            if(enemy.y > player.y-player.height and enemy.destroyed == False):
                running = False
                finish("lost", sound)

        # show the bullets if exist

        for bullet in Bullet.bullets:
            if(bullet.destroy):
                continue
            bullet.show()

            for enemy in ennemies:
                if((enemy.x < bullet.x < (enemy.x+enemy.width)) and (enemy.y < bullet.y < (enemy.y + enemy.height)) and (not enemy.destroyed) and (not bullet.destroy)):
                    enemy.strength -= 1
                    bullet.destroy = True
                    if(enemy.strength == 0):
                        player.score += 1
                        explosion_sound.play()
                        enemy.destroy()
                        end_time = current_time + 500  # 1000 milliseconds = 1 seconds
                        explosionList.insert(
                            0, (end_time, enemy.x, enemy.y))

                    else:
                        damage_sound.play()
                if(player.score == len(ennemies)):
                    for bullet in Bullet.bullets:
                        bullet.destroy = True
                    running = False
                    finish("win", sound)

        for i in range(len(explosionList)):
            if current_time < explosionList[i][0]:
                screen.blit(
                    Helpers.getImg("explosion"), (explosionList[i][1], explosionList[i][2]))
            else:
                explosionList = explosionList[:i]
                break
        display_score(700, 10, player.score)
        pygame.display.update()


main_menu(screen)
