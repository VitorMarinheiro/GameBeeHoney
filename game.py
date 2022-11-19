from obj import Obj, Bee, Text
import random


class Game:

    def __init__(self):

        self.bg = Obj("assets/bg.png", 0, 0)
        self.bg2 = Obj("assets/bg.png", 0, 0)

        self.spider = Obj("assets/spider1.png", random.randrange(0, 290), -50)
        self.flower = Obj("assets/flower1.png", random.randrange(0, 290), -50)
        self.bee = Bee("assets/bee1.png", 150, 600)

        self.change_scene = False

        self.score = Text("0", 120)
        self.lifes = Text("3", 60)

    def draw(self, window):
        self.bg.drawing(window)
        self.bg2.drawing(window)
        self.bee.drawing(window)
        self.spider.drawing(window)
        self.flower.drawing(window)
        self.score.draw(window, 160, 50)
        self.lifes.draw(window, 50, 50)

    def update(self):
        self.move_bg()
        self.move_spiders()
        self.move_flower()
        self.bee.colision(self.spider.group, "Spider", True)
        self.bee.colision(self.flower.group, "Flower", True)
        self.spider.anim("spider", 8, 4)
        self.flower.anim("flower", 5, 2)
        self.bee.anim("bee", 1, 4)
        self.score.update(str(self.bee.pts))
        self.lifes.update(str(self.bee.life))
        self.gameover()


    def move_bg(self):
        self.bg.sprite.rect[1] += 10
        self.bg2.sprite.rect[1] += 10

        if self.bg.sprite.rect[1] >= 640:
            self.bg.sprite.rect[1] = 0

        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -640

    def move_spiders(self):
        self.spider.sprite.rect[1] += 10

        if self.spider.sprite.rect[1] >= 700:
            self.spider.sprite.kill()
            self.spider = Obj("assets/spider1.png", random.randrange(0, 290), -50)

    def move_flower(self):
        self.flower.sprite.rect[1] += 6

        if self.flower.sprite.rect[1] >= 700:
            self.flower.sprite.kill()
            self.flower = Obj("assets/flower1.png", random.randrange(0, 290), -50)

    def gameover(self):
        if self.bee.life <= 0:
            self.change_scene = True
