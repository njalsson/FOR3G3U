import pygame
from pygame.locals import *
import sys
#from gameobjects import *
pygame.init()
#declaring colors
BLACK = (0,0,0)
WHITE = ( 255,255,255)
GREY_COLOR = (70,80,90)
YELLOW_COLOR = (255,255,0)
#declaring size
DISPLAY_SIZE = (640, 480)
#variables for player image and location
player = pygame.image.load('images/player1.png')
x_coord = 120
y_coord = 30
x_vel = 0
y_vel = 0
player = pygame.image.load('images/player1.png')
#player = Player(playerImage)

running = True
key = pygame.key.get_pressed()
my_font = pygame.font.SysFont("Comic Sans MS", 30)

screen = pygame.display.set_mode(DISPLAY_SIZE)
# game loop about to start
screen.fill(GREY_COLOR)
clock = pygame.time.Clock()
fps = 30

while True:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	key = pygame.key.get_pressed()

	if key[pygame.K_a]:
		x_coord -= 1
	if key[pygame.K_s]:
		y_coord += 1
	if key[pygame.K_d]:
		x_coord += 1
	if key[pygame.K_w]:
		y_coord -= 1
	if key[pygame.K_SPACE]:
		print('todo: gera skot')

	screen.fill(WHITE)
	screen.blit(player,(x_coord,y_coord))

	pygame.display.flip()
	clock.tick(fps)

pygame.quit()