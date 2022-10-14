import pygame

class Ship():
    def __init__(self, ai_game):
        # инициал корабль и начальная позиция
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # загрузка изобр и создание прямоугольника
        self.image = pygame.image.load('Images/ship.bmp')
        self.rect = self.image.get_rect()
        # каждый новый корабль появляется у края экрана
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        # флаги перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''обновление позиции корабля с учетом флага'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x


    def blitme(self):
        # рисует корабль в текущей позиции
        self.screen.blit(self.image, self.rect)