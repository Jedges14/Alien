import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
    '''A class to represent the alien fleet'''
    def __init__(self, game_settings, screen):
        super().__init__()
        self.screen=screen
        self.game_settings=game_settings
        
        #load the bmp image
        self.image=pygame.image.load('images/UFO.bmp')
        self.rect=self.image.get_rect()
        
        #start each new alien at the screen top
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        
        self.x=float(self.rect.x)
            
    def check_edges(self):
        '''Return True if alien is at edge of screen.'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True
        
    def update(self):
        '''Moving aliens down'''
        self.x += (self.game_settings.alien_speed_factor * self.game_settings.fleet_direction)
        #self.rect.y += self.game_settings.alien_speed_rate
        self.rect.x=self.x
        
    def blitme(self):
        '''Draw the image'''
        self.screen.blit(self.image, self.rect)