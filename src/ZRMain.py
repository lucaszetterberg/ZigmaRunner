import pygame, random, os, sys
from constants import *
from menu import menu
from player import Player

pygame.init()

## Global variables
global gameSpeed, obstacles, game_over_game, highscore 

points = 0
gameSpeed = 15
game_over_game = False
highscore = 0

pygame.display.set_caption("Zigma runner")
obstacles = []
game_over = False

class Obstacle:
    def __init__(self, image, type):
        self.image
        self.type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        
    def update(self):
        self.rect.x -= gameSpeed
        if self.rect.x < -self.rect.width:
            obstacles.pop()
    
    def draw(self, ZRMain):
        SCREEN.blit(self.image[self.type], self.rect)

class SmallObstacles(Obstacle):
    def __init__(self, image):
        self.image = image
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 475
        
class LargeCactus(Obstacle):
    def __init__(self, image):
        self.image = image
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 407

class Stone(Obstacle):
    def __init__(self, image):
        self.image = image
        self.type = 3
        super().__init__(image, self.type)
        self.rect.y = 330
        
class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 200)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= gameSpeed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(3800, 3800)
            self.y = random.randint(50, 200)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

def draw_track():
    global x_pos_bg, y_pos_bg
    image_width = BG.get_width()
    SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
    SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
    if x_pos_bg <= -image_width:
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        x_pos_bg = 0
    x_pos_bg -= gameSpeed

def score():
    global points, gameSpeed, game_over, highscore
    points += 1
    if points > highscore:
        highscore = points
    if points % 100  == 0:
        gameSpeed += 1

    text = font.render("Points: " + str(points), True, (255,255,255))
    textRect = text.get_rect()
    textRect.center = (1100, 40)
    SCREEN.blit(text, textRect)

def Game(LARGE_OBSTACLES):
    global gameSpeed, obstacles, points, game_over
  
    points = 0
    fps = 60
    obstacles = []
    gameSpeed = 15
    game_over = False
    
    game_running = True

    timer = pygame.time.Clock()
    cloud = Cloud()
    player = Player()
    
    ## Main game loop, can be viewed as what is happening in each frame
    ##pygame.event.clear()
    while game_running:
        timer.tick(fps)
        SCREEN.fill((white))
        ##SCREEN.blit(MAIN_BG, (0,0))
        ##SCREEN.fill(sand, (0, 500, SCREEN.get_width(), SCREEN.get_height()))
        ## Uncomment to enable background picture
        draw_track()
        cloud.draw(SCREEN)
        cloud.update()
        score()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        keyboardInput = pygame.key.get_pressed()

        numb = random.randint(0,2)
        
        if len(obstacles) == 0 and numb == 0:
            obstacles.append(LargeCactus(LARGE_OBSTACLES))
        elif len(obstacles) == 0 and numb == 1:
             obstacles.append(Stone(LARGE_OBSTACLES))
        elif len(obstacles) == 0 and numb == 2:
            obstacles.append(SmallObstacles(SMALL_OBSTACLES))


        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.player_rect.colliderect(obstacle.rect):
                gameSpeed = 0
                return True
                
        player.draw(SCREEN)
        player.update(keyboardInput)
        
        pygame.display.flip()
    
    pygame.quit()
                  
def main():
    game_state = menu(game_over=False)
    while True:
        if game_state == 1:
            game_state = menu(game_over=False)
        elif game_state == 2:
            Delan = Game(OBSTACLES)
            if Delan:
                game_state = menu(game_over=True)

main()