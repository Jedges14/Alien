
import pygame 
from settings import Settings
from ship import Ship
import game_pads as gp
from score_sheet import Scoring 
from pygame.sprite import Group 
from beutt import Buttons
from score_sheet import wins_loss
def run_game():
    pygame.init() 
    
    game_settings=Settings()
    screen=pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Jedges' Space Wars")
    #show button on screen
    butt=Buttons(game_settings, screen, "Let War Reign!")
    
    #MAke the ship
    ship=Ship(game_settings, screen)
    #make a group to store the bullets
    bullets= Group()
    aliens=Group()
    
    gp.create_fleet(game_settings, screen, ship, aliens)
    sets=Scoring(game_settings)
    wl=wins_loss(game_settings, screen, sets)

    
    while True:
        gp.check_events(game_settings, screen, sets, wl, butt, ship, aliens, bullets)
        if sets.game_active:
            ship.update()
            gp.update_bullets(game_settings, screen, sets, wl, ship, aliens, bullets)
            gp.update_aliens(game_settings, sets, wl, screen, ship, aliens, bullets)
        
        
        gp.screen_update(game_settings,screen, sets, wl, ship, aliens, bullets, butt)
            #gp. hits(game_settings, sets, screen, ship, aliens, bullets) #test code prolly will be deleted
    
run_game()


