import pygame.font


class Button():
    def __init__(self, ai_game, msg):
        """инициализация атрибутов кнопки"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # конопка: размер и свойства
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # построение кнопки по центру экрана
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        '''преобразование msg в прямоугольник с текстом по ценру'''
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        # отображение кнопки
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

