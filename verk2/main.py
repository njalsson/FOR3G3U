import pygame
from pygame.locals import *

"""
leikur 1 i verk 2
game of dice
"""
pygame.init()
displaywidth,  displayheight = 640,480

gamescreen = pygame.display.set_mode((displaywidth,displayheight))
pygame.display.set_caption('dices')
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
purple = (100,0,230)
running = True
smallfont = pygame.font.SysFont("monospace", 20)

"""
main game loop
"""
texti = "1 to play, 2 to throw all, 3 to throw one, 4 to exit"
textonscreen = smallfont.render(texti, 1, white)
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	gamescreen.fill(purple)
	gamescreen.blit(textonscreen, (10,50))
	pygame.display.update()


pygame.quit()
quit()

