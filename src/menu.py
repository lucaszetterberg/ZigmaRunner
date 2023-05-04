import pygame, sys
from constants import *


def menu(game_over):
    title_font = pygame.font.Font('freesansbold.ttf', 50)
    menu_font = pygame.font.Font('freesansbold.ttf', 30)

    title_text = title_font.render('Zigma Runner', True, white)
    title_rect = title_text.get_rect()
    title_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)

    start_text = menu_font.render('Press SPACE to start', True, white)
    start_rect = start_text.get_rect()
    start_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    quit_text = menu_font.render('Press Q to quit', True, white)
    quit_rect = quit_text.get_rect()
    quit_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
    
    small_font = pygame.font.Font('freesansbold.ttf', 20)
    
    ##highscore_text = font.render("Highscore: " + str(highscore), True, (255,255,255))
    game_over_text = menu_font.render("Game Over", True, black)
    restart_text = small_font.render("Press R to restart game, press Q to quit, press M to return to main menu", True, black)
    
    ##highscore_rect = highscore_text.get_rect()
    ##highscore_rect.center = (950, 40)
    
    game_over_rect = game_over_text.get_rect()
    game_over_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    restart_rect = restart_text.get_rect()
    restart_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
   

    while True:
        
        if not game_over:
                SCREEN.fill((black))
                SCREEN.blit(title_text, title_rect)
                SCREEN.blit(start_text, start_rect)
                SCREEN.blit(quit_text, quit_rect)
                SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        elif game_over:
                SCREEN.blit(game_over_text, game_over_rect)
                SCREEN.blit(restart_text, restart_rect)
                ##SCREEN.blit(highscore_text, highscore_rect)
                SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    return 2
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r and game_over:
                    return 2
                if event.key == pygame.K_m and game_over:
                    return 1
            
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        pygame.display.update()
