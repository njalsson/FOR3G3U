import pygame
import random
from pygame.locals import *


# min utgafa af space invaders
# 2.5.17

class invaders:
	def __init__(self,gamescreen,color):
		self.y = -10
		self.x = random.randint(0,580)# they can spawn anywhere on the screen
		self.width = 30
		self.height = 30
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
		self.color = color # purple is the one
		self.screen = gamescreen


	def update(self): #change their location a little bit each frame
		self.y = self.y + 1
		self.x += random.randint(-1,1)

	def draw(self):
		pygame.draw.rect(self.screen, self.color, (self.x,self.y, self.width, self.height), 0)
	
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

	def handlebullets(self):
		for x in self.arrayofbullets:
			x.update()
			x.draw()
	def checkcollisionofbulletsandinvaders(self, arrayofinvaders):
		# O(nm)
		self.arrafofinvaders = arrayofinvaders
		for x in self.arrayofbullets:
			for y in self.arrayofinvaders:
				pass

		pass


class bullet:
	def __init__(self,gamescreen, black, x, y):
		self.width = 5
		self.height = 5
		self.x = x
		self.y = y
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
		self.screen = gamescreen
		self.color = black

	def update(self):
		self.y -= 3

	def draw(self):
		pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), 0)
	
#main loop
pygame.init()
#constant variables
displaywidth,  displayheight = 640,480
gamescreen = pygame.display.set_mode((displaywidth,displayheight))
pygame.display.set_caption('invaders')
clock = pygame.time.Clock()


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
arrafofinvaders = []
running = True
while running:
	clock.tick(60)
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
				xdiff = -2
				pass
			if event.key == pygame.K_d:
				xdiff = 2
				#til haegri
				pass
			if event.key == pygame.K_s:
				xdiff = 0

	#10% chance evere frame that a invader spawnes
	chance = random.randint(1,30)
	if chance == 1:
		#create a invader
		#shitty random generator
		invaderrect = 0
		newinvader = invaders(gamescreen, purple)
		arrafofinvaders.append(newinvader)

	gamescreen.fill(white)
	user.update(xdiff)
	user.draw()
	user.handlebullets()
	for x in arrafofinvaders:
		x.update()
		x.draw()
	pygame.display.update()

pygame.quit()
quit()


