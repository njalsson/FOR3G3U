import pygame

#kóði stolinn frá sýnidæmi 
#linkur https://nam.inna.is/api/Attachment/DownloadFile/148019/442018?student=1&t=x7f5XwuUUr9Mg7zYy5raSmSJGiuGjtqr&t1=true

# 21.12.16
def sprite_loader(sp_width, sp_height, sheet_file):
    sprite_frames = []

    image = pygame.image.load(sheet_file).convert_alpha()
    width, height = image.get_size()

    for row in range(int(height / sp_height)):
        for col in range(int(width / sp_width)):
            sprite_frames.append(image.subsurface((col * sp_width, row * sp_height, sp_width, sp_height)))

    return sprite_frames

class Player(pygame.sprite.Sprite):
	def __init__(self, image, x, y):
		self.image = image		
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x

	def update(self):
        #Check Player Input
    	playerInput = self.checkPlayerInput()

        self.updatePosition(playerInput)


	def updatePosition(self, playerInput):
        left = playerInput[0]
        right = playerInput[1]
        up = playerInput[2]
        down = playerInput[3]
        shoot = playerInput[4]
        if self.projectileCall == True:
            self.projectileCall = False
        if shoot:
            self.projectileCall = True
        if left:
            self.rect.x -= 10
        if right:
            self.rect.x += 10
        if up:
            self.rect.y += 10
        if down:
            self.rect.x -= 10


    def checkPlayerInput(self):
	    left = pygame.key.get_pressed() [pygame.K_d]
	    right = pygame.key.get_pressed() [pygame.K_a]
	    up = pygame.key.get_pressed() [pygame.K_w]
	    down = pygame.key.get_pressed() [pygame.K_s]
	    shoot = pygame.key.get_pressed() [pygame.K_SPACE]
		return (left, right,up, down, shoot)


class projectiles(pygame.sprite.Sprite):
    def __init__(self, shooter):
        self.size = (8,8)
        self.rect = pygame.draw.rect(window,(70,80,90), (shooter.rect.x , shooter.rect.y), 10, 0)
        self.rect.x = shooter.rect.x
        self.rect.y = shooter.rect.y - shooter.image.get_height()

    def update(self):
            self.rect.y -= 5
            if self.rect.y <= 0 - self.image.get_height():
                self.kill()
