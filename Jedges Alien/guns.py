import pygame 
from pygame.sprite import Sprite 

class Bullet(Sprite):
    '''manage bullet from the ship'''
    def __init__(self, game_settings,screen, ship):
        '''putting the bullet at the ship position'''
        super().__init__()
        self.screen=screen
        
        ##Create a bullet rectangle at 0, 0 and then set position
        self.rect=pygame.Rect(0,0,game_settings.bullet_width, game_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.centery=ship.rect.centery   #likely to be taken out
        self.rect.top=ship.rect.top
        
        #store the bullet post as float
        self.y=float(self.rect.y)
        
        self.color=game_settings.bullet_color
        self.speed_rate=game_settings.bullet_speed_factor
        
    def update(self):
        '''Move bullet up the screen'''
        #change the positiion
        self.y -= self.speed_rate
        self.rect.y=self.y
        
    def draw_bullet(self):
        '''drawing the bullet on the screen'''
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        
        