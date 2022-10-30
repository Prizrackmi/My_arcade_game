import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    '''
    Class game
    '''


    def __init__(self):
        '''
        initialaze game
        '''
        pygame.init()
        self.settings = Settings()
        # для перехода в оконный режим расскоментировать эту, и закомментировать след. 3 сторки: (пока так :) )
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height


        pygame.display.set_caption("Alien Invazion by Prizrack ;)")
        # параметр screen
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()



    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            # print(len(self.bullets))

    def _check_events(self):
            '''обработка нажатий'''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)




    def _check_keydown_events(self, event):

            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                self.fire_bullet()
            elif event.key == pygame.K_e:
                self.settings.bg_color = (255, 0, 255)
            elif event.key == pygame.K_r:
                self.settings.bg_color = self.settings.bg_color_def


    def _check_keyup_events(self, event):

            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False


    def fire_bullet(self):
        '''создание снаряда'''
        if len(self.bullets) < self.settings.bullets_allowd:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        # создание ряда кораблей с иньервалом в одну ширину корабля
        alien = Alien(self)
        alien_widht = alien.rect.width
        availble_space_x = self.settings.screen_width - (2 * alien_widht)
        number_aliens_x = availble_space_x // (2 * alien_widht)

        # создание ряда
        for alien_number in range(number_aliens_x):
            self._create_alien(alien_number)


    def _create_alien(self, alien_number):
            alien = Alien(self)
            alien_widht = alien.rect.width
            alien.x = alien_widht +2 * alien_widht * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)

    def _update_screen(self):
        '''обновление изображений на экране и отображение нового экрана'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
