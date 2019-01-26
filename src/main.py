import pygame
from piece import piece
from piece_coords import piece_coords

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
	if not(piece_focus.has_hit_bottom()):
		piece_focus.update(2)
	else:
		pieces.append(piece(block_x, 0, block_width, screen_x, screen_y, piece_coords.i0))
		piece_focus = pieces[-1]
		# create a new shape
		pass

pygame.init()
screen_x = 504
screen_y = 756
win = pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()
run = True

block_width = 42
block_x = block_width * 6
block_y = 256
pieces = []
pieces.append(piece(block_x, block_y, block_width, screen_x, screen_y, piece_coords.j0))
piece_focus = pieces[0]
while run:

	clock.tick(30)

	for event in pygame.event.get(): # checking for events
		if event.type == pygame.QUIT:
			run = False
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				piece_focus.update_left()
			elif event.key == pygame.K_d:
				piece_focus.update_right()
			elif event.key == pygame.K_SPACE:
				piece_focus.rotate()

	#update()
	draw()

pygame.quit()