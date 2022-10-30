import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    # один пришелец
    def __init__(self, ai_game):
        # создание и начальная позиция пришельца
        super().__init__()
        self.screen = ai_game.screen
        # загрузка изобр и создание прямоугольника
        self.image = pygame.image.load('Images/alien8.jpg')
        self.rect = self.image.get_rect()
        # каждый пришелец в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # точная горизонт позиция пришельца
        self.x = float(self.rect.x)