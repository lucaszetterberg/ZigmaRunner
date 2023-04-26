import pygame
import random
import ZRMain

class Obstacle:
    def __init__(self, image, type):
        self.image
        self.type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = ZRMain.screenWidth
        
    def update(self):
        self.rect.x -= ZRMain.gameSpeed
        if self.rect.x < -ZRMain.screenWidth:
            obstacles.pop()
    
    def draw(self, ZRMain):
        ZRMain.screen.blit(self.image[self.type], self.rect)

class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325
        
class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300
