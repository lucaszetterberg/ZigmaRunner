import pygame
from constants import *

#Player class, includes all features and functions regarding the player character
class Player:
    PLAYER_X = 80
    PLAYER_Y = 430
    PLAYER_Y_SLIDE = 470
    JUMP_VEL = 8.5

    def __init__(self):
        self.slide_img = SLIDING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.player_slide = False
        self.player_run = True
        self.player_jump = False

        self.step_index = 0
        self.image = self.run_img[0]
        self.player_rect = self.image.get_rect()
        self.player_rect.x = self.PLAYER_X
        self.player_rect.y = self.PLAYER_Y
        self.jump_vel = self.JUMP_VEL

    #Updates animation of player according to action
    def update(self, keyboardInput):
        if self.player_slide:
            self.slide()
        if self.player_run:
            self.run()
        if self.player_jump:
            self.jump()
        if self.step_index >= 10:
            self.step_index = 0

        if keyboardInput[pygame.K_UP] or keyboardInput[pygame.K_SPACE] and not self.player_jump:
            self.player_slide = False
            self.player_run = False
            self.player_jump = True
        elif keyboardInput[pygame.K_DOWN] and not self.player_jump:
            self.player_slide = True
            self.player_run = False
            self.player_jump = False
        elif not (self.player_jump or keyboardInput[pygame.K_DOWN]):
            self.player_slide = False
            self.player_run = True
            self.player_jump = False  

    #Slide function allows player to slide and shows slide pose
    def slide(self):
        self.image = self.slide_img[0]
        self.player_rect = self.image.get_rect()
        self.player_rect.x = self.PLAYER_X
        self.player_rect.y = self.PLAYER_Y_SLIDE
        self.step_index += 1
    
    #Run function switches pose of player to simulate the player running
    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.player_rect = self.image.get_rect()
        self.player_rect.x = self.PLAYER_X
        self.player_rect.y = self.PLAYER_Y
        self.step_index += 1

    #Jump function allows player to jump and ascend from groundlevel, also shows jump pose when in action
    def jump(self):
        self.image = self.jump_img
        if self.player_jump:
            self.player_rect.y -= int(self.jump_vel * 4)
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.player_jump = False
            self.jump_vel = self.JUMP_VEL

    #Draws player to screen according to action and position
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.player_rect.x, self.player_rect.y))