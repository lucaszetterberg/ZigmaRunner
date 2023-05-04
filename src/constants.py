import pygame,os



pygame.init()
## Visual assets 
CLOUD = pygame.image.load(os.path.join("images", "Cloud.png"))
BG = pygame.image.load(os.path.join("src", "Track.png"))
RUNNING = [pygame.image.load(os.path.join("images", "ZigmaRun1.png")), pygame.image.load(os.path.join("images", "ZigmaRun2.png"))]
JUMPING = pygame.image.load(os.path.join("images", "ZigmaJump.png"))
SLIDING = [pygame.image.load(os.path.join("images", "ZigmaSlide.png"))]
SMALL_OBSTACLES = [pygame.image.load(os.path.join("images", "LargeCactus1.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("images", "LargeCactus1.png")), pygame.image.load(os.path.join("images", "LargeCactus2.png")), pygame.image.load(os.path.join("images", "LargeCactus3.png"))]

## Positioning for visual assets
x_pos_bg = 0
y_pos_bg = 380

## Screen parameters
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1200
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

## Fonts
font = pygame.font.Font('freesansbold.ttf', 20)
font = pygame.font.Font("freesansbold.ttf",16)

## Colours
black = (0,0,0)
white = (200,200,200)

## Background
##MAIN_BG = pygame.image.load(os.path.join("images", "Desert2.png"))
##MAIN_BG = pygame.transform.scale(MAIN_BG, SCREEN.get_size())



