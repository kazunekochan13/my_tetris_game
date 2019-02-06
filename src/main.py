import pygame
from piece import piece
from piece_coords import piece_coords
from random import seed, randint

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
	for shape in pieces:
		shape.draw(win)
	pygame.display.update()

def update():
	global piece_focus
	
	"""if not(piece_focus.has_hit_bottom()):
		piece_focus.update_down(2)
	else:
		pieces.append(piece(block_x, 0, block_width, screen_x, screen_y, generate_random_piece()))
		piece_focus = pieces[-1]"""

def generate_random_piece():
	rand = randint(0,7)
	if rand == 0:
		rand_piece = piece_coords.o
	elif rand == 1:
		rand_piece = piece_coords.i
	elif rand == 2:
		rand_piece = piece_coords.s
	elif rand == 3:
		rand_piece = piece_coords.z
	elif rand == 4:
		rand_piece = piece_coords.j
	elif rand == 5:
		rand_piece = piece_coords.l
	else:
		rand_piece = piece_coords.t
	return rand_piece

pygame.init()
screen_x = 504
screen_y = 756
win = pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()
run = True

seed(1)
block_width = 42
block_x = block_width * 6
block_y = 256
pieces = []
pieces.append(piece(block_x, block_y, block_width, screen_x, screen_y, piece_coords.j))
piece_focus = pieces[0]
while run:

	clock.tick(30)

	for event in pygame.event.get(): # checking for events
		if event.type == pygame.QUIT:
			run = False
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				piece_focus.update_left()
			elif event.key == pygame.K_RIGHT:
				piece_focus.update_right()
			elif event.key == pygame.K_DOWN:
				# piece_focus.update_jump(pieces) # check collision with list of pieces on screen
				pass
			elif event.key == pygame.K_SPACE:
				piece_focus.rotate()

	update()
	draw()

pygame.quit()