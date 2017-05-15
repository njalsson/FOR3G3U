import pygame
from random import randint
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
		pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), 0)

	def collision(self, ball):
		self.currentball = pygame.Rect(self.x, self.y, self.width, self.height)



class Ball:
	def __init__(self, gamescreen, color):
		self.xvol = 3
		self.yvol = 10
		# if self.xvol == 0:
		# 	self.xvol = 3
		# if self.yvol == 0:
		# 	self.yvol = 3
		self.x = displaywidth / 2
		self.y = displayheight / 2
		self.height = 20
		self.width = 20
		self.color = color
		self.screen = gamescreen

	def update(self):
		self.x += self.xvol
		self.y += self.yvol
		if self.x < 0 or self.x >= 620:
			self.xvol *= -1
		if self.y <= 10 or self.y >= 460:
			self.yvol *= -1
	def draw(self):
		pygame.draw.ellipse(self.screen, self.color, (self.x, self.y, self.width, self.height))

	def rect(self):
		return pygame.Rect(self.x, self.y, self.width, self. height)



#main loop
pygame.init()
#constant variables
displaywidth,  displayheight = 640,480
smallfont = pygame.font.SysFont("monospace", 19)
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
	xdiff = 0

	for event in pygame.event.get():
		#geta haett i leik
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
			if event.key == pygame.K_a:
				#faera user 5 til 10 px til vinstri
				xdiff = -20
			if event.key == pygame.K_d:
				xdiff = 20
				#til haegri

	gamescreen.fill(black)
	scoretext = "score is {}".format(score)
	scoretext2 = smallfont.render(scoretext, 1, white)
	gamescreen.blit(scoretext2, (50, 50))

	ball.update()
	ballrect = ball.rect()
	player.collision(ballrect)
	player.update(xdiff)
	player.draw()
	ball.draw()
	pygame.display.update()
	clock.tick(30)
pygame.quit()
quit()
