import pygame
import numpy

class grid():

	# class represents tetris grid of 'unfocused' pieces. ie. pieces that are set in place in the grid and not moving
	# 0 in grid represents no rect whilst 1 represents there being a rect in that space

	def __init__(self, x, y, width):
		self.width = width
		self.x = int(x / self.width)
		self.y = int(y / self.width)
		self.rect_pieces = []
		self.rect_pieces_colour1 = []
		self.rect_pieces_colour2 = []
		self.piece_grid = numpy.zeros((self.x, self.y))

	def draw(self, win):
		for i in range(0, len(self.rect_pieces)):
			pygame.draw.rect(win, self.rect_pieces_colour1[i], self.rect_pieces[i]) # basic square
			pygame.draw.rect(win, self.rect_pieces_colour2[i], self.rect_pieces[i], 2) # basic dark outline
		#for rect in self.rect_pieces:
		#	pygame.draw.rect(win, (128, 0, 0), rect) # basic square
		#	pygame.draw.rect(win, (80, 0, 0), rect, 2) # basic dark outline

	def set_piece(self, piece):
		# add new rect in pieces.rect_list to rect_pieces to keep track
		# convert rect_list of piece into positions in the grid
		for rect in piece.rect_list:
			self.rect_pieces.append(rect)
			self.rect_pieces_colour1.append(piece.rgb1)
			self.rect_pieces_colour2.append(piece.rgb2)
			temp_x = int(rect.x / self.width)
			temp_y = int(rect.y / self.width)
			self.piece_grid[temp_x, temp_y] = 1

	def is_row_full(self):
		pass

	def draw_to_console(self): # left in for testing purposes
		rows = self.piece_grid.shape[0]
		cols = self.piece_grid.shape[1]
		str_row = ""
		print(str_row)
		for j in range(0, cols):
			for i in range(0, rows):
				str_row += str(int(self.piece_grid[i, j]))
			print(str_row)
			str_row = ""