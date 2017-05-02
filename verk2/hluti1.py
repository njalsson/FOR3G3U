import pygame
import random
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
smallfont = pygame.font.SysFont("monospace", 19)
clock = pygame.time.Clock()

"""
main game loop
"""
arrayofcomputerdice = []
arrayofuserdice = []
drawdice = False
endgame = False
texti = "1 to play, 2 to throw all, 3 to throw one, 4 to reset"
textonscreen = smallfont.render(texti, 1, white)
while running:
	clock.tick(1)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
			if event.key == pygame.K_1:
				#roll dice for computer
				for x in range(6):
					arrayofcomputerdice.append(random.randint(1,6))
				#throw dice for user, but only 5
				for x in range(5):
					arrayofuserdice.append(random.randint(1,6))
				drawdice = True
			if event.key == pygame.K_2:
				if drawdice:
					arrayofuserdice = []
					for x in range(6):
						arrayofuserdice.append(random.randint(1,6))
					endgame = True

				
				#throw all of user dice
			if event.key == pygame.K_3:
				arrayofuserdice.append(random.randint(1,6))
				endgame = True
				#throw one user dice
			if event.key == pygame.K_4:
				arrayofuserdice = []
				arrayofcomputerdice = []
				endgame = False
				drawdice = False

	gamescreen.fill(purple)
	gamescreen.blit(textonscreen, (10,10))
	compabove = smallfont.render("computer rolls below", 1, white)
	userbelow = smallfont.render("user rolls below", 1, white)
	gamescreen.blit(userbelow, (10, 110))
	gamescreen.blit(compabove, (10, 50))
	if drawdice:
		for x in range(6):
			#draw 6 dice on screen
			currentcomputerdiceroll = arrayofcomputerdice[x];
			currenttexttowriteout = smallfont.render(str(currentcomputerdiceroll), 1, white)
			gamescreen.blit(currenttexttowriteout, (30 * x + 10, 80))
		for x in range(len(arrayofuserdice)):
			print(arrayofuserdice[x])
			currentuserdiceroll = arrayofuserdice[x];
			currenttexttowriteout = smallfont.render(str(currentuserdiceroll), 1, white)
			gamescreen.blit(currenttexttowriteout, (30 * x + 10, 140))

		#if he has chosen to reroll, and has a full set of rolled dices we announce winner
		if endgame:
			sumofuserscore, sumofcompscore = 0, 0
			for x in range(6):
				sumofcompscore += arrayofcomputerdice[x]
				sumofuserscore += arrayofuserdice[x]
			if sumofuserscore > sumofcompscore:
				announcement = "user wins"
			elif sumofcompscore > sumofuserscore:
				announcement = "computer wins"
			else:
				announcement = "no one won the game"
			sumtextcomp = " => {}".format(sumofcompscore)
			sumtextuser = " => {}".format(sumofuserscore)
			comprscoretext = smallfont.render(sumtextcomp, 1, white)
			userscoretext = smallfont.render(sumtextuser, 1, white)
			announcetext = smallfont.render(announcement, 1, white)
			gamescreen.blit(comprscoretext, (180, 80))
			gamescreen.blit(userscoretext, (180, 140))
			gamescreen.blit(announcetext, (200, 250))
				 
	pygame.display.update()

pygame.quit()
quit()


