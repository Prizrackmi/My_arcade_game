import sys
from time import sleep
import pygame

from settings import Settings
from game_stats import GameStats
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

        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()



    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()


    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            # print(len(self.bullets))
        self._check_bullet_alion_collisions()

    def _check_bullet_alion_collisions(self):
            # проверка попаданий
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

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
        alien_widht, alien_height = alien.rect.size
        availble_space_x = self.settings.screen_width - (2 * alien_widht)
        number_aliens_x = availble_space_x // (2 * alien_widht)
        # количество рядов на экране
        ship_height = self.ship.rect.height
        availble_space_y = (self.settings.screen_height - (3 * alien_height) - (2* ship_height))
        nuber_rows = availble_space_y // (2 * alien_height)
        for row_number in range (nuber_rows):
                    # создание ряда
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)



    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_widht, alien_height = alien.rect.size
        alien.x = alien_widht + 2 * alien_widht * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + (2 * alien.rect.height) * row_number
        self.aliens.add(alien)


    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            # print("Ship hit!!!")
            self._ship_hit()
        self._check_aliens_bottom()

    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False


    def _check_aliens_bottom(self):
        ''' Проверка столкновения с нижним краем экрана'''
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break


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
