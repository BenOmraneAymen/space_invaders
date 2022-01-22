from Enemy import Enemy


class Startup:
    def __init__(self, screen, level):
        self.screen = screen
        self.level = level

    def init_ennemies(self):
        with open('db/levels.txt', 'r') as f:
            levels = f.read()
            level_data = levels.split('\n')[self.level-1]
            ennemies_data = level_data.split(',')
        # create ennemy
        # print(ennemies_data)
        ennemies = []
        for e in ennemies_data:
            aux = str(e).split(" ")
            x = int(aux[0])
            y = int(aux[1])
            strength = int(aux[2])
            ennemies.append(Enemy(x, y, strength, screen=self.screen))
        return ennemies
