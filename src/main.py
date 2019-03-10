import pygame
from piece import piece
from piece_coords import piece_coords
from random import seed, randint
from grid import grid

def draw_background():
	win.fill((0, 125, 125))
	i = 0
	bg_x = block_width
	while i < 6:
		pygame.draw.rect(win, (0, 90, 90), (bg_x, 0, block_width, screen_y))
		bg_x += block_width * 2
		i += 1

def draw():
	draw_background()
	piece_grid.draw(win)
	#for shape in pieces:
	#	shape.draw(win)
	piece_focus.draw(win)
	pygame.display.update()

def update():
	global piece_focus
	if piece_focus.has_collide(pieces) or piece_focus.has_hit_bottom():
		add_new_piece()
	else:
		if speed_flag:
			piece_focus.update_down(42)
	"""if not(piece_focus.has_hit_bottom()):
		piece_focus.update_down(2)
	else:
		pieces.append(piece(block_x, 0, block_width, screen_x, screen_y, generate_random_piece()))
		piece_focus = pieces[-1]"""

def add_new_piece():
	global piece_focus
	pieces.append(piece_focus)
	piece_grid.set_piece(piece_focus)
	# piece_grid.draw_to_console() # test to check if grid is representing correctly
	piece_focus = generate_random_piece()

def generate_random_piece():
	rand = randint(0,7)
	if rand == 0:
		rand_piece = piece_coords.o
		rgb1 = (255, 255, 0)
		rgb2 = (128, 128, 0)
	elif rand == 1:
		rand_piece = piece_coords.i
		rgb1 = (0, 255, 255)
		rgb2 = (0, 128, 128)
	elif rand == 2:
		rand_piece = piece_coords.s
		rgb1 = (0, 255, 0)
		rgb2 = (0, 128, 0)
	elif rand == 3:
		rand_piece = piece_coords.z
		rgb1 = (255, 0, 0)
		rgb2 = (128, 0, 0)
	elif rand == 4:
		rand_piece = piece_coords.j
		rgb1 = (0, 0, 255)
		rgb2 = (0, 0, 128)
	elif rand == 5:
		rand_piece = piece_coords.l
		rgb1 = (255, 165, 0)
		rgb2 = (128, 38, 0)
	else:
		rand_piece = piece_coords.t
		rgb1 = (255, 0, 255)
		rgb2 = (128, 0, 128)
	return piece(block_x, 0, block_width, screen_x, screen_y, rand_piece, rgb1, rgb2)

pygame.init()
screen_x = 504
screen_y = 756
win = pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()
run = True

seed(1)
block_width = 42
block_x = block_width * 6
block_y = 252
pieces = []
piece_grid = grid(screen_x, screen_y, block_width)
piece_focus = generate_random_piece()
speed = 1
speed_num = 0
speed_flag = True
while run:

	clock.tick(30)

	if speed_num > 30:
		speed_num = 0
	if speed_num == 0:
		speed_flag = True
	else:
		speed_flag = False
	speed_num += 1

	for event in pygame.event.get(): # checking for events
		if event.type == pygame.QUIT:
			run = False
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				# need to have collision code here
				piece_focus.update_left()
			elif event.key == pygame.K_RIGHT:
				# need tp have collision code here
				piece_focus.update_right()
			elif event.key == pygame.K_DOWN:
				# piece_focus.update_jump(pieces) # check collision with list of pieces on screen
				pass
			elif event.key == pygame.K_SPACE:
				piece_focus.rotate()

	update()
	draw()

pygame.quit()