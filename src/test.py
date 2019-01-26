# script to test out features of the game

import pygame
from piece import piece
from piece_coords import piece_coords

pygame.init()
screen_x = 504
screen_y = 756
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

# keys reference: need to be global
left_key_loop = False
right_key_loop = False
left_start_time = pygame.time.get_ticks()
right_start_time = pygame.time.get_ticks()

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
	shape.draw(win)
	# draw_shapes()
	pygame.display.update()

def key_press(lkl, lst, rkl, rst):
	global left_key_loop, left_start_time
	keys = pygame.key.get_pressed()
	if keys[pygame.K_a]: # move left
		if left_key_loop == False:
			left_start_time = pygame.time.get_ticks()
			left_key_loop = True
			shape.update_left()
		elif left_key_loop == True and (pygame.time.get_ticks() - left_start_time) >= 500:
			left_key_loop = False
			shape.update_left()
		
	elif keys[pygame.K_d] and not(rkl):
		shape.update_right()


clock = pygame.time.Clock()
run = True
shape = piece(block_x, block_y, block_width, piece_coords.l0)
while run:

	clock.tick(30)

	for event in pygame.event.get(): # checking for events
		if event.type == pygame.QUIT:
			run = False
		#elif event.type == pygame.KEYUP:
			#if event.key == pygame.K_a:
				#left_key_loop = False
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				shape.update_left()
			elif event.key == pygame.K_d:
				shape.update_right()
			elif event.key == pygame.K_SPACE:
				shape.rotate()
		
	# key_press(left_key_loop, left_start_time, right_key_loop, right_start_time)
	
	draw()

pygame.quit()