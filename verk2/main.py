import pygame
from pygame.locals import *

"""
leikur 1 i verk 2
game of dice
"""
pygame.init()
gamescreen = pygame.display.set_mode((640,480))
pygame.display.set_caption('dices')

running = True
"""
main game loop
"""

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
pygame.quit()
quit()