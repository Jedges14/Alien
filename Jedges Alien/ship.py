import pygame 
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, game_settings, screen):
        '''Initialize the ship and set its starting position.'''
        super().__init__()
        self.screen=screen
        self.game_settings=game_settings
        #Load the ship image and get its react.
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        #Start each new ship at the bottom center of the screen
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        # self.rect.centery=self.screen_rect.centery
        
        self.center=float(self.rect.centerx)
        self.Center=float(self.rect.centery)
        
        #movement
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
        
    def update(self):
        '''Update the ship position'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center +=self.game_settings.speed_rate
        if self.moving_left and self.rect.left > 0:
            self.center -=self.game_settings.speed_rate
        if self.moving_up and self.rect.top >0:
            self.Center -=self.game_settings.speed_rate
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.Center +=self.game_settings.speed_rate
            
            
        self.rect.centery=self.Center   
        self.rect.centerx=self.center
        
    def center_ship(self):
        '''return the ship back to center after collision'''
        self.rect.midbottom=self.screen_rect.midbottom
        self.centerx=self.screen_rect.centerx
        
        
        
    def blitme(self):
        '''Draw the skip at its current location.'''
        self.screen.blit(self.image, self.rect )
        
