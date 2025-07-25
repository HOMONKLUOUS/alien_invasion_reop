import sys
import pygame
from time import sleep
from game_state import GameState
from setting import Setting
from SpaceShip import SpaceShipAlien
from bullet import Bullets
from alien import Aliens
from button import Button
from scoreboard import Scoreboard

class AlienInvation:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Setting()


        # screen

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        #caption

        pygame.display.set_caption("Alien Invation")

        # aliens _ spaceship & bullets

        self.SpaceShip = SpaceShipAlien(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.state = GameState(self)

        # Button

        self.play_button = Button(self, 'play')

        # scoreboard

        self.SB = Scoreboard(self)

        # check the game over

        self.game_active = False

        self._creat_fleet()

    def run_game(self):
        while True:
            self._check_events()

            if self.game_active:
                self._check_events()
                self.SpaceShip.Update()
                self.bullets.update()
                # removing bullet that rech the top of the screen 
                for bullet in self.bullets.copy():
                    '''
                    when we use list in for loop python expect that list will stay the same lenght
                    in that case we have to make copy of out list of bullets
                    '''
                    self._bullet_update()
                    if bullet.rect.bottom <= 0:
                        self.bullets.remove(bullet)
                    '''
                    we check how many bullets exist currently in the game and thay really dispeareed!
                    '''
                self._update_alien()
            self._update_screen()
            # it make loop to count 60 times per soccend <framerate: 60>
            self.clock.tick(60)

    def _bullet_update(self):
        '''
        The groupcollide check the position of the bullets and the aliens of they hit the two last arguments: True True
        if mean they both dispeadied for example if you want make powerfull bullet you should change to this False, True
        the alien will distroied but the bullet is still hier and can distroid more than that untill reach the top of the screen
        '''
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            '''
            In this part of code until now maybe can't calculate the truly score of player
            mybe is because of i don't any limit on firing bullets
            but don't be mad i solve this problem by collisions
            collision work like a dictionary and in my program the value of this dic is list of aliens that 
            remove sooo i just multiply this line to len of the aliens
            '''
            for aliens in collisions.values():
                self.state.score += self.settings.aliens_points * len(aliens)
            self.SB.prep_score()

        if not self.aliens:
            self.bullets.empty()
            self._creat_fleet()
            # for levelup
            self.settings.increase_speed()
    '''
    For each alien with check_edge method in aliens.py file check if they in adge of the screen
    that call the change_fleet_direction which is in this file this method change the settings.fleet_direction
    valuble in setting file which chnage the the direction of the aliens in x row.
    '''
    def _check_fleet_aliens(self):
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.flet_spped_drop
        self.settings.fleet_direction *= -1

    def _check_events(self):
        # to check user input
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit()

            if events.type == pygame.KEYDOWN:
                self._check_keydown_event(events)

            if events.type == pygame.KEYUP:
                self._check_keyup_event(events)

            # check the button paly
            if events.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_keydown_event(self, events):
        if events.key == pygame.K_RIGHT:
            # move the ship to the right
            self.SpaceShip.moving_right = True
        if events.key == pygame.K_LEFT:
            # moving the ship to the left
            self.SpaceShip.moving_left = True

        # press q to exit
        if events.key == pygame.K_q:
            sys.exit()

        # shooting with spacebar
        if events.key == pygame.K_SPACE:
            self._fire_bullets()

        '''
        we hide the mouse on the screen after the first time the player press the start button
        of course we can fix this with just if condition and will that but just think it be better
        if the player can start the game and play the game with just using a keyboard
        '''
        if events.key == pygame.K_s and not self.game_active:
            self.state.reset_state()
            self.game_active = True
            self.aliens.empty()
            self.bullets.empty()
            self._creat_fleet()
            self.SpaceShip.center_ship()
            # attention that if we start the game with the keyboeard the mouse will not hide so for that:
            pygame.mouse.set_visible(False)
            # Reset the game settings.
            self.settings.initialize_dynamic_setting()
            # reset the game score
            self.SB.prep_score()


    def _check_keyup_event(self, events):
        if events.key == pygame.K_RIGHT:
            self.SpaceShip.moving_right = False
        if events.key == pygame.K_LEFT:
            self.SpaceShip.moving_left = False

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.state.reset_state()
            self.game_active = True
            '''
            we need to reset the game when press the play button like when you lose!
            '''
            self.aliens.empty()
            self.bullets.empty()

            self._creat_fleet()
            self.SpaceShip.center_ship()

            # Reset the game settings.
            self.settings.initialize_dynamic_setting()

            #reset the game score
            self.SB.prep_score()

            #make mouse hide
            if self.game_active:
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)

    def _fire_bullets(self):
        # creat a new bullet and addet to the bullet group
        new_bullet = Bullets(self)
        self.bullets.add(new_bullet)

    def _creat_fleet(self):
        alien = Aliens(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height

        # we check to stay in row and height by adding the aliens in one row and calculaate the inner space
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            current_x = alien_width
            current_y += 2 * alien_height

    # create aliens in one row
    def _create_alien(self, x_position, y_position):
        new_alien = Aliens(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    # update the position the of all aliens in the feet
    def _update_alien(self):
        self._check_fleet_aliens()
        self.aliens.update()

        # the situation that aliens hit the ship we reset the game and players loses one of thier harts
        if pygame.sprite.spritecollideany(self.SpaceShip, self.aliens):
            self._ship_state()

        self._check_aliens_bottom()

    
    def _ship_state(self):
        # You lose one of your harts
        if self.state.ship_left > 0:
            self.state.ship_left -= 1
            # Reset the screen
            self.bullets.empty()
            self.aliens.empty()
            self._creat_fleet()
            self.SpaceShip.center_ship()

            sleep(0.5)

        else:
            self.game_active = False

    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_state()
                break

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        # we make shore that we draw bullet in update screen per space pressing!
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.SpaceShip.blitme()
        # showing the aliens spaceship in the screen
        self.aliens.draw(self.screen)
        # show the score information
        self.SB.show_score()
        # draw the play button if the game is inactive
        if not self.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

if __name__ == '__main__':
    '''we call AlienInvation with () to not act like a class 
    if we don't we get error that you miss self argument'''

    ai = AlienInvation()
    ai.run_game()
