import pygame,os

pygame.init()
## Visual assets 
CLOUD = pygame.image.load(os.path.join("images", "Cloud.png"))
BG = pygame.image.load(os.path.join("images", "Track.png"))
RUNNING = [pygame.image.load(os.path.join("images", "ZigmaRun1.png")), pygame.image.load(os.path.join("images", "ZigmaRun2.png"))]
JUMPING = pygame.image.load(os.path.join("images", "ZigmaJump.png"))
SLIDING = [pygame.image.load(os.path.join("images", "ZigmaSlide.png"))]
SMALL_OBSTACLES = [pygame.image.load(os.path.join("images", "SmallRock1.png")), pygame.image.load(os.path.join("images", "SmallRock2.png")), pygame.image.load(os.path.join("images", "SmallRock3.png"))]
OBSTACLES = [pygame.image.load(os.path.join("images", "LargeCactus1.png")), pygame.image.load(os.path.join("images", "LargeCactus2.png")), pygame.image.load(os.path.join("images", "LargeCactus3.png"))]
AIR_OBSTACLES = [pygame.image.load(os.path.join("images", "Dust1.png")), pygame.image.load(os.path.join("images", "Dust2.png"))]

## Positioning for visual assets
x_pos_bg = 0
y_pos_bg = 490

## Screen parameters
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1200
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

## Fonts
font = pygame.font.Font('freesansbold.ttf', 20)
font = pygame.font.Font("freesansbold.ttf",16)
title_font = pygame.font.Font('freesansbold.ttf', 50)
menu_font = pygame.font.Font('freesansbold.ttf', 30)
small_font = pygame.font.Font('freesansbold.ttf', 20)
 
## Colours
black = (0,0,0)
white = (200,200,200)
sand = (194, 178, 128)

## Background
MAIN_BG = pygame.image.load(os.path.join("images", "Desert2.png"))
MAIN_BG = pygame.transform.scale(MAIN_BG, SCREEN.get_size())

## Menu Parameters (includes text and positions of text)
title_text = title_font.render('Zigma Runner', True, white)
title_rect = title_text.get_rect()
title_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)

start_text = menu_font.render('Press SPACE to start', True, white)
start_rect = start_text.get_rect()
start_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

quit_text = menu_font.render('Press Q to quit', True, white)
quit_rect = quit_text.get_rect()
quit_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)

game_over_text = menu_font.render("Game Over", True, black)
restart_text = small_font.render("Press R to restart game, press Q to quit, press M to return to main menu", True, black)

game_over_rect = game_over_text.get_rect()
game_over_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
restart_rect = restart_text.get_rect()
restart_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
