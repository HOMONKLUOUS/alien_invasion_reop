class Setting:
    def __init__(self):

        #screen_setting

        self.width = 1200
        self.height = 800
        self.bg_color = (0, 0, 0)
        
        self.ship_speed = 2.0

        #bullets_setting

        self.bullet_speed = 3.0
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)

        # aliens_setting

        self.flet_spped_drop = 10

        # shape limit

        self.ship_limit = 3

        # leveling up with by speeding up

        self.speedup = 1.1
        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        self.ship_speed = 2
        self.alien_speed = 2
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup
        self.alien_speed *= self.speedup
        
