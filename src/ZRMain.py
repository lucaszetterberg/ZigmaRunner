import pygame 
import random
import os

pygame.init()

## Global constants
screenWidth = 1200
screenHeight = 700
SCREEN = pygame.display.set_mode((screenWidth, screenHeight))
gameSpeed = 30
CLOUD = pygame.image.load(os.path.join("Cloud.png"))




class Cloud:
    def __init__(self):
        self.x = screenWidth + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= gameSpeed
        if self.x < -self.width:
            self.x = screenWidth + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

def main(): 


    ## Parameters for screen an player setup
    player_x = 100
    player_y = 580
    deltaY = 0
    deltaX = 0
    gravity = 2
    x_pos_bg = 0
    y_pos_bg = 380
    cloud = Cloud()

    ## Objects for colours, placeholder for when images are added
    black = (0,0,0)
    white = (235,235,235)
    
    ## Makes screen
    screen = pygame.display.set_mode([screenWidth, screenHeight])
    pygame.display.set_caption("Zigma runner")
    background = black
    fps = 60 
    font = pygame.font.Font("freesansbold.ttf",16)
    
    ## Makes timer, sets gameRunning to true (if gameRunning is false the game will not run)
    timer = pygame.time.Clock()
    gameRunning = True
    
    ## Main game loop, can be viewed as what is happening in each frame
    while gameRunning:
        timer.tick(fps)
        screen.fill(background)
        floor = pygame.draw.rect(screen, white, [0, 600, screenWidth, 5])
        player = pygame.draw.rect(screen, white, [player_x, player_y, 20, 20])
        cloud.draw(SCREEN)
        cloud.update()
        
        ## Keylistening
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and deltaY == 0:
                    deltaY = 20
        
        ## If statement for gravity
        if deltaY > 0 or player_y < 580:
            player_y -= deltaY
            deltaY -= gravity
        
        ## I player for some reason gets placed under the floor, this if statement will place it back on it
        if player_y > 580:
            player_y = 580
        
        ## Tells the game that if player is on ground level it should stop falling
        if player_y == 580 and deltaY < 0:
            deltaY = 0
        
        pygame.display.flip()
    pygame.quit()
main()