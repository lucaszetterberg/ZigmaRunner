import pygame 
import random
import os

pygame.init()

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1200
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("images", "LargeCactus1.png"))]
JUMPING = pygame.image.load(os.path.join("images", "LargeCactus1.png"))
DUCKING = [pygame.image.load(os.path.join("images", "LargeCactus1.png"))]

SMALL_CACTUS = [pygame.image.load(os.path.join("images", "LargeCactus1.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("images", "LargeCactus1.png"))]

pygame.display.set_caption("Zigma runner")
fps = 60 
font = pygame.font.Font("freesansbold.ttf",16)

class Player:
    PLAYER_X = 80
    PLAYER_Y = 310

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.player_duck = False
        self.player_run = True
        self.player_jump = False

        self.step_index = 0
        self.image = self.run_img[0]
        self.player_rect = self.image.get_rect()
        self.player_rect.x = self.PLAYER_X
        self.player_rect.y = self.PLAYER_Y

    def update(self, keyboardInput):
        if self.player_duck:
            self.duck()
        if self.player_run:
            self.run()
        if self.player_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if keyboardInput[pygame.K_UP] or keyboardInput[pygame.K_SPACE] and not self.player_jump:
            self.player_duck = False
            self.player_run = False
            self.player_jump = True
        elif keyboardInput[pygame.K_DOWN] and not self.player_jump:
            self.player_duck = True
            self.player_run = False
            self.player_jump = False
        elif not (self.player_jump or keyboardInput[pygame.K_DOWN]):
            self.player_duck = False
            self.player_run = True
            self.player_jump = False

    def duck(self):
       pass

    def run(self):
        self.image = self.run_img[0]
        self.player_rect = self.image.get_rect()
        self.player_rect.x = self.PLAYER_X
        self.player_rect.y = self.PLAYER_Y
        self.step_index += 1

    def jump(self):
        pass
    
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.player_rect.x, self.player_rect.y))
        
        
def main(): 

    
    ## Makes timer, sets gameRunning to true (if gameRunning is false the game will not run)
    timer = pygame.time.Clock()
    player = Player()
    GAMERUNNING = True
        
    ## Main game loop, can be viewed as what is happening in each frame
    
    while GAMERUNNING:
        timer.tick(fps)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAMERUNNING = False

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)
        
        pygame.display.flip()
    pygame.quit()

main()