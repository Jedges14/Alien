import sys
from guns import Bullet
import pygame 
from aliens import Alien
import time

def screen_update(game_settings,screen,sets, wl, ship, aliens, bullets, butt):
    screen.fill(game_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)
    #Redraw the bullets behind the ship and the aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    wl.show_board()
    
    if not sets.game_active:
        butt.draw()
        #Make the most recently drawn screen visible
    pygame.display.flip()
    
def check_keydown_events(event, game_settings, screen, ship, bullets):
    '''activates when the dxn keys are pressed'''
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_UP:
        ship.moving_up=True
    elif event.key==pygame.K_DOWN:
        ship.moving_down=True
    elif event.key==pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)
        
def fire_bullet(game_settings, screen, ship, bullets):
    '''Fire a bullet if limit not reached.'''
        #bullet limiting
    if len(bullets)< game_settings.bullet_max:
    #add the new bullet
        new=Bullet(game_settings, screen, ship)
        bullets.add(new)
        
def check_keyup_events(event, ship):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False
    elif event.key==pygame.K_UP:
        ship.moving_up=False
    elif event.key==pygame.K_DOWN:
        ship.moving_down=False

        
def check_events(game_settings, screen, sets, wl, butt, ship, aliens, bullets):
    '''for quits and other stuff'''
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets)    
        elif event.type==pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y=pygame.mouse.get_pos()
            check_play(game_settings, screen, sets, wl, butt, ship, aliens, bullets, mouse_x, mouse_y)
            
            
def check_play(game_settings, screen, sets, wl, butt, ship, aliens, bullets, mouse_x, mouse_y):
    '''Starts when let it reign plays'''
    button_clicked=butt.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not sets.game_active:  #butt.rect.collidepoint(mouse_x, mouse_y):
        #set game settings to original
        game_settings.initialize_dynamic_settings()
        #hide the mouse
        pygame.mouse.set_visible(False)
        #reset
        sets.reset_sets()
        pygame.mouse.set_visible(False)
        sets.reset_sets()
        sets.game_active=True
        
        wl.show_board()
        wl.show_high_score()
        wl.show_level()
        wl.show_ships()
        
        #empty the alien and bullet group to reset
        aliens.empty()
        bullets.empty()
        
        #resetting
        create_fleet(game_settings, screen, ship, aliens )
        ship.center_ship()
        
    
    
def update_bullets(game_settings, screen,sets, wl, ship, aliens, bullets):
    '''get rid of old bullets to prevent lag'''
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    check_bullets_alien_collision(game_settings, screen, sets,wl, ship, aliens, bullets)
   
    
def check_bullets_alien_collision(game_settings, screen, sets, wl, ship, aliens, bullets):
    
    #check if bullet hit alien, and delete both
    collisions=pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            sets.score += game_settings.alien_points
            wl.board()
        check_high_score(sets, wl)
    if len(aliens)==0:
        #destroy all and creat new level 
        bullets.empty()
        game_settings.speed_increase()
        sets.level += 1
        wl.show_level()
        
        create_fleet(game_settings, screen, ship, aliens)
    
              
def get_number_aliens_x(game_settings, alien_width):
    available_space_x=game_settings.screen_width - (1*alien_width)
    number_aliens_x=int(available_space_x / (2* alien_width))
    return number_aliens_x

def get_number_rows(game_settings, ship_height, alien_height):
    '''Determine the number of rows of aliens that fit the screen'''
    available_space_y=(game_settings.screen_height-(2*alien_height)-ship_height) #calculating available vertical space
    number_rows=int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(game_settings, screen, aliens, alien_number, row_number):
    alien=Alien(game_settings, screen)
    alien_width=alien.rect.width
    alien.x=alien_width +  2* alien_width * alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)
    


def create_fleet(game_settings, screen, ship, aliens):
    '''Creating the full fleet of aliens to fill the screen'''
    #space between alien is equal to one alien width
    alien=Alien(game_settings, screen)
    number_aliens_x= get_number_aliens_x(game_settings, alien.rect.width)
    number_rows=get_number_rows(game_settings, ship.rect.height, alien.rect.height)
    #create the first row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(game_settings, screen, aliens, alien_number, row_number)
            
def check_fleet_edges(game_settings, aliens):
    '''Respond if the alien has reached the edge'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_settings, aliens)
            break
        
def change_fleet_direction(game_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1  
    
    
def hits(game_settings, sets, wl, screen, ship, aliens, bullets):
    '''identify when collision occurs and delete one ship'''
    if sets.ships_remain>0:
        sets.ships_remain -=1  #reduce by one
        
        #update the board
        wl.show_ships()
        aliens.empty()
        bullets.empty()#likely to leave in peace
        create_fleet(game_settings, screen, ship, aliens)
        ship.center_ship()
        time.sleep(0.5) #use the sleep attribute to pause or slow down game a bit for regrouping
    else:
        sets.game_active=False
        pygame.mouse.set_visible(True)
    
def alien_bottom(game_settings, sets, wl, screen, ship, aliens, bullets):
    '''Collision of alien with screen base'''
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            '''ship will be hit indirectly'''
            hits(game_settings, sets, wl, screen, ship, aliens, bullets)
            break
    
       
def update_aliens(game_settings, sets, wl, screen, ship, aliens, bullets):
    '''update the positions and check if the fleet is at the edge'''
    check_fleet_edges(game_settings, aliens)
    aliens.update()  
    if pygame.sprite.spritecollideany(ship, aliens):
        hits(game_settings, sets, wl, screen, ship, aliens, bullets) #checks for bullet alien
    alien_bottom(game_settings, sets, wl,  screen, ship, aliens, bullets) #checks for screen base alien collision
    
def check_high_score(sets, wl):
    '''ensure there is a high score'''
    if sets.score > sets.high_score:
        sets.high_score = sets.score
        wl.show_high_score()
           
            

                    