from Button import Button
from Enemy import Ennemy
from Helpers import getImg


class Startup:
    def __init__(self, screen, level):
        self.screen = screen
        self.level = level

    def init_ennemies(self):
        with open('db/levels.txt', 'r') as f:
            levels = f.read()
            level_data = levels.split('\n')[self.level]
            ennemies_data = level_data.split(',')
        # create ennemy
        print(ennemies_data)
        ennemies = []
        for e in ennemies_data:
            aux = str(e).split(" ")
            x = int(aux[0])
            y = int(aux[1])
            strength = int(aux[2])
            ennemies.append(Ennemy(x, y, strength, screen=self.screen))
        return ennemies

    def init_level(self):
        background = getImg('background')

        pick = getImg('pick')
        lvl1 = getImg('num1').convert_alpha()
        lvl2 = getImg('num2').convert_alpha()
        lvl3 = getImg('num3').convert_alpha()
        lvl4 = getImg('num4').convert_alpha()
        lvl5 = getImg('num5').convert_alpha()
        btn_lvl1 = Button.Button(100, 250, lvl1, 0.2, screen=self.screen)
        btn_lvl2 = Button.Button(225, 250, lvl2, 0.2, screen=self.screen)
        btn_lvl3 = Button.Button(350, 250, lvl3, 0.2, screen=self.screen)
        btn_lvl4 = Button.Button(475, 250, lvl4, 0.2, screen=self.screen)
        btn_lvl5 = Button.Button(600, 250, lvl5, 0.2, screen=self.screen)
        running = True
        while running:
            self.screen.fill((200, 200, 200))
            self.screen.blit(background, (0, 0))
            self.screen.blit(pick, (50, 50))
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
