import pygame


class Obj:

    def __init__(self, image, x, y):

        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)

        self.sprite.image = pygame.image.load(image)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y

        self.frame = 1
        self.tick = 0

    def drawing(self, window):
        self.group.draw(window)

    def anim(self, image, tick, frames):
        self.tick += 1
        if self.tick >= tick:
            self.tick = 0
            self.frame += 1

        if self.frame > frames:
            self.frame = 1

        self.sprite.image = pygame.image.load("assets/"+ image + str(self.frame)+".png")


class Bee(Obj):

    def __init__(self, image, x, y):
        super().__init__(image, x, y)

        pygame.mixer.init()
        self.sound_pts = pygame.mixer.Sound("assets/sounds/score.ogg")
        self.sound_block = pygame.mixer.Sound("assets/sounds/bateu.ogg")

        self.life = 3
        self.pts = 0

    def move_bee(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 35
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 27

    def colision(self, group, name, remove):

        collision = pygame.sprite.spritecollide(self.sprite, group, remove)
        # Ultimo parametro é para destruir o objeto ou nao

        if name == "Flower" and collision:
            self.pts += 1
            self.sound_pts.play()
        if name == "Spider" and collision:
            self.life -= 1
            self.sound_block.play()


class Text:

    def __init__(self, text, size):

        pygame.font.init()
        self.font = pygame.font.SysFont("Arial bold", int(size))
        self.render = self.font.render(text, True, (255, 255, 255))

    def draw(self, window, x, y):
        window.blit(self.render, (x, y))

    def update(self, text):
        self.render = self.font.render(text, True, (255, 255, 255))