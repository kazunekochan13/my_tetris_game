import pygame
from piece_coords import piece_coords

class piece():

	def __init__(self, x, y, width, coords):
		self.x = x
		self.y = y
		self.width = width
		self.coords = coords
		self.coords_list = coords.value

	def draw(self, win):
		i = 0
		while i < 4:
			pygame.draw.rect(win, (128, 0, 0), (self.x + (self.coords_list[i][0] * self.width), self.y + (self.coords_list[i][1] * self.width), self.width, self.width)) # basic square
			pygame.draw.rect(win, (80, 0, 0), (self.x + (self.coords_list[i][0] * self.width), self.y + (self.coords_list[i][1] * self.width), self.width, self.width), 2) # basic dark outline
			i += 1

	def update_left(self):
		self.x -= self.width

	def update_right(self):
		self.x += self.width

	def rotate(self):
		if not(self.coords.name == "o0"):

			if self.coords.name == "i0":
				self.coords = piece_coords.i1
			elif self.coords.name == "i1":
				self.coords = piece_coords.i0

			elif self.coords.name == "s0":
				self.coords = piece_coords.s1
			elif self.coords.name == "s1":
				self.coords = piece_coords.s0

			elif self.coords.name == "z0":
				self.coords = piece_coords.z1
			elif self.coords.name == "z1":
				self.coords = piece_coords.z0

			elif self.coords.name == "t0":
				self.coords = piece_coords.t1
			elif self.coords.name == "t1":
				self.coords = piece_coords.t2
			elif self.coords.name == "t2":
				self.coords = piece_coords.t3
			elif self.coords.name == "t3":
				self.coords = piece_coords.t0

			elif self.coords.name == "j0":
				self.coords = piece_coords.j1
			elif self.coords.name == "j1":
				self.coords = piece_coords.j2
			elif self.coords.name == "j2":
				self.coords = piece_coords.j3
			elif self.coords.name == "j3":
				self.coords = piece_coords.j0

			elif self.coords.name == "l0":
				self.coords = piece_coords.l1
			elif self.coords.name == "l1":
				self.coords = piece_coords.l2
			elif self.coords.name == "l2":
				self.coords = piece_coords.l3
			elif self.coords.name == "l3":
				self.coords = piece_coords.l0

			self.coords_list = self.coords.value
