class Settings():
    '''A class to store all settings for Alien Invasion'''
    def __init__(self):
        '''Initialize the game's settings'''
        # Screen settings
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(255, 255, 255)
        
        #ship
        self.speed_rate=1.5
        self.ship_limit=3
        #bullet settings
        self.bullet_speed_rate=3.1
        self.bullet_width=15
        self.bullet_height=10
        self.bullet_color=255, 255,0
        self.bullet_max=26
        #alien movement
        self.alien_speed_rate=1
        self.fleet_drop_speed=10
        
        self.speedup_scale=1.1
        #increasing points with increasing levels
        self.score_scale=1.9
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        '''for the settings to change through out the game'''
        self.ship_speed_factor=2
        self.bullet_speed_factor=3.5
        self.alien_speed_factor=1
        #fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction=1
        
        self.alien_points=50
        
    def speed_increase(self):
        '''for increasing the settings of speed'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points=int(self.alien_points * self.score_scale)
        
        
        
        
        
        