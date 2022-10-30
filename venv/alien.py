import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    # один пришелец
    def __init__(self, ai_game):
        # создание и начальная позиция пришельца
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # загрузка изобр и создание прямоугольника
        self.image = pygame.image.load('Images/alien8.jpg')
        self.rect = self.image.get_rect()
        # каждый пришелец в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # точная горизонт позиция пришельца
        self.x = float(self.rect.x)

    def update(self):
        # перемещение в стороны
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x


    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
