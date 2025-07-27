import pygame.font
import json
from pathlib import Path

class Scoreboard:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.state

        # Font settings

        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the image
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        # make image of the high score in the window

        #make high score round and formated with commas
        high_score = round(self.stats.highscore, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True,
        self.text_color, self.settings.bg_color)
        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.highscore:
            #update the score
            self.stats.change("aliens_game/alien_invasion/highscore.json", self.stats.score)
            
            self.prep_high_score()


    def show_score(self):
        #Draw score to the screen.
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
