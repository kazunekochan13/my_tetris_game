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
i_coords = [[-(block_width * 2), 0], [-(block_width), 0], [0, 0], [block_width, 0]]
j_coords = [[-(block_width), 0], [0, 0], [block_width, 0], [block_width, block_width]]
l_coords = [[-(block_width), 0], [-(block_width), block_width], [0, 0], [block_width, 0]]
o_coords = [[-(block_width), 0], [-(block_width), block_width], [0, 0], [0, block_width]]
s_coords = [[-(block_width), block_width], [0, 0], [0, block_width], [block_width, 0]]
t_coords = [[-(block_width), 0], [0, 0], [0, block_width], [block_width, 0]]
z_coords = [[-(block_width), 0], [0, 0], [0, block_width], [block_width, block_width]]

def draw_shapes():
	i = 0
	while i < 4:
		pygame.draw.rect(win, (128, 0, 0), (block_x + z_coords[i][0], block_y + z_coords[i][1], block_width, block_width)) # basic square
		pygame.draw.rect(win, (80, 0, 0), (block_x + z_coords[i][0], block_y + z_coords[i][1], block_width, block_width), 2) # basic dark outline
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