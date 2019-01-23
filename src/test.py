# script to test out features of the game

import pygame

pygame.init()
screen_x = 504
screen_y = 768
win = pygame.display.set_mode((screen_x, screen_y))

# shapes reference
block_width = 42
block_x = 252
block_y = 256

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
	#pygame.draw.rect(win, ())
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