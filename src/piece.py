import pygame

class piece():

	def __init__(self, x, y, width, coords):
		self.x = x
		self.y = y
		self.width = width
		self.coords = coords

	def draw(self, win):
		i = 0
		while i < 4:
			pygame.draw.rect(win, (128, 0, 0), (self.x + (self.coords[i][0] * self.width), self.y + (self.coords[i][1] * self.width), self.width, self.width)) # basic square
			pygame.draw.rect(win, (80, 0, 0), (self.x + (self.coords[i][0] * self.width), self.y + (self.coords[i][1] * self.width), self.width, self.width), 2) # basic dark outline
			i += 1

	def update(self, x, y, is_skip=False):
		if not(is_skip):
			self.x += x
			self.y += y
		else: # skipped to the bottom
			self.y += y