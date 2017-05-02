import pygame
from random import randint
#inna er buinn ad banna mig til 2021 fyrir ad gera lykilord rangt einu sinni, svo eg man ekki alveg hvernig lysingin er en herna er min utgafa af thessum leik

pygame.init()

displayheight = 480
displaywidth = 640

gamescreen = pygame.display.set_mode((displaywidth,displayheight))
pygame.display.set_caption('whackamouse')
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
purple = (100,0,230)
running = True
score = 0
iscatbool = False
mouse = pygame.draw.rect(gamescreen, blue, (40, 40, 35, 35), 0)
smallfont = pygame.font.SysFont("monospace", 19)
clock = pygame.time.Clock()
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False

	#draw 64 boxes, 90% chance its mouse, 10% its cat
	#if user hovers over the mouse it gets a score
	#if user hovers over the cat it loses all score
	currentmousepos = randint(1,64) # choosing where the mouse lives
	clock.tick(1) #setting fps to 1
	gamescreen.fill(white) #clearing screen
	currentheigth = 50
	for x in range(8):
		currentwidth = 40
		for y in range(8):
			if (x * y) + y == currentmousepos:
				currentmousepos = randint(1,64) # choosing where the mouse lives
				iscat = randint(1,10)
				if iscat != 1:
					mouse = pygame.draw.rect(gamescreen, blue, (currentwidth, currentheigth, 35, 35), 0)
				else:
					mouse = pygame.draw.rect(gamescreen, black, (currentwidth, currentheigth, 35, 35), 0)
					iscatbool = True


			else:
				pygame.draw.rect(gamescreen, red, (currentwidth, currentheigth, 35, 35), 1)
			currentwidth += 40
		currentheigth += 40

	if mouse.collidepoint(pygame.mouse.get_pos()) and iscatbool:
		score = 0
	elif mouse.collidepoint(pygame.mouse.get_pos()) and not  iscatbool:
		score += 1
	scoretext = "score is {}".format(score)
	scoretext2 = smallfont.render(scoretext, 1, black)
	gamescreen.blit(scoretext2, (400, 50))
	pygame.display.update()	
quit()