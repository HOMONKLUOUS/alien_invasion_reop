class GameState:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        '''
        i add high score in the game but unlike the self.score should't be reset so i added hie'''

        self.reset_state()
        self.high_score = 0

    def reset_state(self):
        self.ship_left = self.settings.ship_limit
        self.score = 0