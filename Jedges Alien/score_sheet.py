import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoring():
    def __init__(self, game_settings):
        self.game_settings=game_settings
        self.reset_sets()   #rresets after the collision
        self.game_active= False
        self.high_score=0
        
    def reset_sets(self):
        '''resets the game whent the limit of is achieved'''
        self.ships_remain=self.game_settings.ship_limit
        self.score=0
        #show level starting at 1
        self.level=1
        
class wins_loss():
    '''jotting wins and losses'''
    def __init__(self, game_settings, screen, sets):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.game_settings=game_settings
        self.sets=sets
        
        #setting the font for scoring information
        self.text_colour=(0, 0, 0)
        self.font=pygame.font.SysFont('Times New Roman', 28)
        
        self.board()
        self.show_high_score()
        self.show_level()
        self.show_ships()
        
    def board(self):
        '''draw the score on pygame screen'''
        sc=str(self.sets.score)
        rounded_points=int(round(self.sets.score, -1))
        sc= "{:,}".format(rounded_points)
        self.score_image=self.font.render(sc, True, self.text_colour, self.game_settings.bg_color)
        #pput the score at the top left corner
        self.score_rect=self.score_image.get_rect()
        self.score_rect.left=self.screen_rect.left + 20
        self.score_rect.top= 15
        
    def show_board(self):
        '''show the score on the screen'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        #pasting the ships on the screen
        self.ships.draw(self.screen)
        
        
    def show_high_score(self):
        '''image of the high score in screen top center'''
        high_score=int(round(self.sets.high_score, -1))
        high_sc="{:,}".format(high_score)
        self.high_score_image=self.font.render(high_sc, True, self.text_colour, self.game_settings.bg_color)
        
        #placing at the center
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.score_rect.top
        
    def show_level(self):
        '''level in image'''
        self.level_image= self.font.render(str(self.sets.level), True, self.text_colour, self.game_settings.bg_color)
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.score_rect.right
        self.level_rect.top=self.score_rect.bottom - 1
        
    def show_ships(self):
        '''make images of ship to show how many remaining after collision'''
        self.ships=Group()
        for ship_number in range(self.sets.ships_remain):
            ship=Ship(self.game_settings, self.screen)
            ship.rect.x= self.screen_rect.width - (ship_number * ship.rect.width) - ship.rect.width
            ship.rect.y= 10
            self.ships.add(ship)