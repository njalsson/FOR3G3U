import pygame
from pygame.locals import *

"""
leikur 1 i verk 2
game of dice
"""
pygame.init()
gamescreen = pygame.display.set_mode((640,480))
pygame.display.set_caption('dices')
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
purple = (100,0,230)
running = True
"""
main game loop
"""

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
	gamescreen.fill(purple)
	pygame.display.update()

pygame.quit()
quit()