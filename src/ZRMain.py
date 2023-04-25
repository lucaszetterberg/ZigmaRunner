import pygame 
import random
from PIL import Image

pygame.init()

screenWidth = 1200
screenHeight = 700

black = (0,0,0)

screen = pygame.display.set_mode([screenWidth, screenHeight])
pygame.display.set_caption("Zigma runner")
background = black
fps = 60 
font = pygame.font.Font("freesansbold.ttf",16)
timer = pygame.time.Clock()

image = Image.open("\..\images\background.jpg")

gameRunning = True

while gameRunning:
    timer.tick(fps)
    screen.fill(background)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
    
    pygame.display.flip()
pygame.quit()