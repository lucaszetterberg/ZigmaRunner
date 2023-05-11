import pygame, sys
from constants import *

# Displays a simple menu
def menu(game_over):
    while True:
        
        # Different types of menus depending on situation
        if not game_over:
                SCREEN.fill((black))
                SCREEN.blit(title_text, title_rect)
                SCREEN.blit(start_text, start_rect)
                SCREEN.blit(quit_text, quit_rect)
                SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        elif game_over:
                SCREEN.blit(game_over_text, game_over_rect)
                SCREEN.blit(restart_text, restart_rect)
                SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
                
        # Takes user input and performs action according to user 
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
