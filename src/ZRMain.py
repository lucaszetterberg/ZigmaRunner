import pygame 
import random
import os

pygame.init()



## Global constants
x_pos_bg = 0
y_pos_bg = 380
points = 0
font = pygame.font.Font('freesansbold.ttf', 20)
gameSpeed = 30
black = (0,0,0)
white = (235,235,235)

CLOUD = pygame.image.load(os.path.join("src", "Cloud.png"))
BG = pygame.image.load(os.path.join("src", "Track.png"))

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
    JUMP_VEL = 8,5
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
        self.image = self.jump_img[0]
        if self.player_jump:
            self.player_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.player_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.player_rect.x, self.player_rect.y))
    


class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= gameSpeed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(3800, 3800)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


    ## Parameters for screen an player setup
    ## Objects for colours, placeholder for when images are added
    
        
        
def main(): 
    cloud = Cloud()
    
    ## Makes timer, sets gameRunning to true (if gameRunning is false the game will not run)
    timer = pygame.time.Clock()

    player = Player()
    GAMERUNNING = True
        

    gameRunning = True
    global gameSpeed, x_pos_bg, y_pos_bg, points
    def score():
        global points, gameSpeed
        points += 1
        if points % 100  == 0:
            gameSpeed += 1

        text = font.render("Points: " + str(points), True, (255,255,255))
        textRect = text.get_rect()
        textRect.center = (1100, 40)
        SCREEN.blit(text, textRect)


    def draw_background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= gameSpeed
    
    ## Main game loop, can be viewed as what is happening in each frame
    
    while GAMERUNNING:
        timer.tick(fps)
        SCREEN.fill((black))
        draw_background()
        cloud.draw(SCREEN)
        cloud.update()
        score()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                GAMERUNNING = False

        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)
        
        pygame.display.flip()
    
    pygame.quit()
    
main()
