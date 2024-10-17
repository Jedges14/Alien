import pygame.font
'''Class to control the buttons play reset etc'''                
class Buttons():
    def __init__(self, game_settings, screen, msg):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        
        #size of the buttons
        self.width=200
        self.height=60
        self.button_color=0,0,0
        self.text_colour=0,255,255
        self.face=pygame.font.SysFont('Cambria', 40)
        
        '''Building the rect for the button'''
        self.rect=pygame.Rect(0,0, self.width, self.height)
        self.rect.center=self.screen_rect.center
        
        self.prep_msg(msg)
        
    def prep_msg(self,msg):
        '''gives image  of the message'''
        self.msg_image=self.face.render(msg, True, self.text_colour, self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center
        
    def draw(self):
        '''button first then message'''
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
