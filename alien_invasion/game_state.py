from pathlib import Path
import json
class GameState:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        # json file where player score saved!
        self.file = Path("aliens_game/alien_invasion/highscore.json")
        '''
        i add high score in the game but unlike the self.score should't be reset so :
        '''
        self.reset_state()
        self.Highscore = self.file.read_text()
        if self.Highscore.strip() != '':
            self.highscore = int(self.Highscore)
        else:
            self.highscore = 0  


    def reset_state(self):
        self.ship_left = self.settings.ship_limit
        self.score = 0


    # update the highscore gile now you can save your points even when you exit the game but it schow new highscore when you run the game again
    def change(self, file, new_score):
        with open (file, 'w') as f:
            json.dump(new_score, f)


