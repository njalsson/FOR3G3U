import pygame

pygame.init()

GREY_COLOR = (70,80,90)
YELLOW_COLOR = (255,255,0)
DISPLAY_SIZE = (640, 480)

running = True

screen = pygame.display.set_mode(DISPLAY_SIZE)
screen.fill(GREY_COLOR)

my_font = pygame.font.SysFont("Comic Sans MS", 30)

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = False

	elif event.type == pygame.MOUSEMOTION:
		screen.fill((70,80,90))
		label = my_font.render(str(event.pos),1,YELLOW_COLOR)
		screen.blit(label,(230,100))

	pygame.display.flip()

pygame.quit()