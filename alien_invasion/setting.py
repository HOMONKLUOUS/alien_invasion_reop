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

        self.alien_speed = 2.0
        self.flet_spped_drop = 10

        # Direction 1 is represent right and direction -1 represent left

        self.fleet_direction = 1

        # shipes limit

        self.ship_limit = 3

