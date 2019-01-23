# script to test out features of the game

import pygame

pygame.init()
screen_x = 504
screen_y = 768
win = pygame.display.set_mode((screen_x, screen_y))

# shapes reference
block_width = 42
block_x = block_width * 6
block_y = 256

def draw_shapes():
	i = 0
	while i < 4:
		b_x = block_x
		b_y = block_y + (i * block_width)
		pygame.draw.rect(win, (128, 0, 0), (b_x, b_y, block_width, block_width)) # basic square
		pygame.draw.rect(win, (80, 0, 0), (b_x, b_y, block_width, block_width), 2) # basic dark outline
		i += 1
	
def draw_background(): # drawing the stripe background
	win.fill((0, 125, 125))
	i = 0
	bg_x = block_width
	while i < 6:
		pygame.draw.rect(win, (0, 90, 90), (bg_x, 0, block_width, screen_y))
		bg_x += block_width * 2
		i += 1

def draw():
	draw_background()
	draw_shapes()
	pygame.display.update()

clock = pygame.time.Clock()
run = True
while run:

	clock.tick(30)

	for event in pygame.event.get(): # checking for events
		if event.type == pygame.QUIT:
			run = False

	draw()

pygame.quit()