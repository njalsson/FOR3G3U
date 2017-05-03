import pygame
import random
from pygame.locals import *


# min utgafa af space invaders
# 2.5.17

class invaders:
	def __init__(self,gamescreen,color):
		self.y = random.randint(0, displaywidth - 60) # they can spawn anywhere on the screen
		self.x = -40
		self.width = 30
		self.height = 30
		self.color = color # purple is the one
		self.screen = gamescreen


	def update(self): #change their location a little bit each frame
		self.x = -1
		self.y += random.randint(-1,1)

	def draw(self):
		pygame.draw.rect(self.gamescreen, self.color, (self.x, self.y, self.width, self.height), 0)
	
class rocket:
	#setja inni sitt eigid skjal seinna
	def __init__(self, gamescreen, red):
		self.screen = gamescreen
		self.color = red
		self.x = displaywidth/2
		self.y = displayheight-40
		self.height = 20
		self.width = 20
		self.arrayofbullets = []
		self.newbullet = 0
	def update(self, xdiff):
		self.x += xdiff

	def draw(self):
		pygame.draw.rect(self.screen, self.color, (self.x,self.y,self.width,self.height), 0)
		#pygame.draw.rect()
	def shoot(self):
		newbullet = bullet(self.screen, black, self.x, self.y)
		self.arrayofbullets.append(newbullet)

	def handle(self):
		for x in self.arrayofbullets:
			x.update()
			x.draw()

class bullet:
	def __init__(self,gamescreen, black, x, y):
		self.width = 5
		self.height = 5
		self.x = x
		self.y = y
		self.screen = gamescreen
		self.color = black

	def update(self):
		self.y -= 1

	def draw(self):
		pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), 0)
		
#main loop
pygame.init()
#constant variables
displaywidth,  displayheight = 640,480
gamescreen = pygame.display.set_mode((displaywidth,displayheight))
pygame.display.set_caption('invaders')

#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
purple = (100,0,230)

#creating the user rocket
user = rocket(gamescreen, red)
xdiff = 0
running = True
while running:
	xdiff = 0
	for event in pygame.event.get():
		#geta haett i leik
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
			#movement og skjota
			if event.key == pygame.K_SPACE:
				#user skytur skoti upp
				user.shoot()
			if event.key == pygame.K_a:
				#faera user 5 til 10 px til vinstri
				xdiff = 5
				pass
			if event.key == pygame.K_d:
				xdiff = -5
				#til haegri
				pass


	gamescreen.fill(white)
	user.update(xdiff)
	user.draw()
	user.handle()
	pygame.display.update()

pygame.quit()
quit()


