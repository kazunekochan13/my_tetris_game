import pygame
from piece_coords import piece_coords

class piece():

	def __init__(self, x, y, width, screen_width, screen_height, coords):
		self.x = x
		self.y = y
		self.width = width
		self.screen_width = screen_width
		self.screen_height = screen_height
		self.coords = coords
		self.coords_list = coords.value
		self.find_edges()

	def draw(self, win):
		i = 0
		while i < 4:
			pygame.draw.rect(win, (128, 0, 0), (self.x + (self.coords_list[i][0] * self.width), self.y + (self.coords_list[i][1] * self.width), self.width, self.width)) # basic square
			pygame.draw.rect(win, (80, 0, 0), (self.x + (self.coords_list[i][0] * self.width), self.y + (self.coords_list[i][1] * self.width), self.width, self.width), 2) # basic dark outline
			i += 1

	def find_left_edge(self):
		self.left = self.x + (self.coords_list[0][0] * self.width)

	def find_right_edge(self):
		self.right = self.x + (self.coords_list[3][0] * self.width) + self.width

	def find_top_edge(self):
		temp = self.y + self.coords_list[0][1] * self.width
		for coord in self.coords_list:
			if self.y + coord[1] * self.width < temp:
				temp = self.y + coord[1] * self.width
		self.top = temp

	def find_bottom_edge(self):
		temp = self.y + (self.coords_list[0][1] * self.width) + self.width
		for coord in self.coords_list:
			if self.y + (coord[1] * self.width) + self.width > temp:
				temp = self.y + (coord[1] * self.width) + self.width
		self.bottom = temp

	def find_edges(self):
		self.find_left_edge()
		self.find_right_edge()
		self.find_top_edge()
		self.find_bottom_edge()

	def has_hit_bottom(self):
		return self.bottom >= self.screen_height

	def update(self, y):
		self.y += y
		self.find_edges()

	def update_left(self):
		if self.left > 0:
			self.x -= self.width
			self.find_edges()

	def update_right(self):
		if self.right < self.screen_width:
			self.x += self.width
			self.find_edges()

	def check_sides(self):
		run_left = True
		run_right = True
		while run_left:
			if self.left < 0:
				self.update_right()
			else:
				run_left = False
		while run_right:
			if self.right > self.screen_width:
				self.update_left()
			else:
				run_right = False

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
			self.find_edges()
			self.check_sides()