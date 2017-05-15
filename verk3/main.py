import pygame
from pygame.locals import *
# singly player pong

class Player:
    def __init__(self, gamecreen, whitecolor):
        self.height = 20
        self.color = whitecolor
        self.width = 60
        self.x = 250
        self.y = 450
        self.screen = gamescreen
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


    def update(self, xdiff):
        self.x+=xdiff
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect, 0)

class Ball:
    def __init__(self, gamescreen, color):
        self.x = displaywidth / 2
        self.y = displayheight / 2
        self.height = 20
        self.width = 20
        self.color = color
        self.screen = gamescreen

    def update(self, xdiff, ydiff):
        self.x += xdiff
        self.y += ydiff
    def draw(self):
        pygame.draw.ellipse(self.screen, self.color, (self.x, self.y, self.width, self.height))




#main loop
pygame.init()
#constant variables
displaywidth,  displayheight = 640,480
gamescreen = pygame.display.set_mode((displaywidth,displayheight))
pygame.display.set_caption('pong')
clock = pygame.time.Clock()
score = 0

#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
purple = (100,0,230)
running = True
player = Player(gamescreen, white)
ball = Ball(gamescreen, white)

while running:
    for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
            if event.key == pygame.K_a:
                xdiff = -12
            if event.key == pygame.K_d:
        	    xdiff = 12

    gamescreen.fill(black)
    player.update(xdiff)
    player.draw()
    ball.draw()
    pygame.display.update()

pygame.quit()
quit()
