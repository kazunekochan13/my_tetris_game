import pygame
from piece_coords import piece_coords
import math

class piece():

	def __init__(self, x, y, width, screen_width, screen_height, coords, rgb1, rgb2):
		self.x = x
		self.y = y
		self.width = width
		self.screen_width = screen_width
		self.screen_height = screen_height
		self.coords = coords
		self.coords_list = coords.value
		self.rect_list = []
		for coord in coords.value:
			self.rect_list.append(pygame.Rect((self.x + (coord[0] * self.width), self.y + (coord[1] * self.width), self.width, self.width)))
		self.rgb1 = rgb1
		self.rgb2 = rgb2
		self.find_edges()
		self.rad = math.radians(90) # rotation by 90 degrees. math functions only use radians

	def draw(self, win):
		for rect in self.rect_list:
			pygame.draw.rect(win, self.rgb1, rect) # basic square
			pygame.draw.rect(win, self.rgb2, rect, 2) # basic dark outline

	def find_edges(self):
		self.left = self.rect_list[0].x
		self.right = self.rect_list[0].x + self.width
		self.top = self.rect_list[0].y
		self.bottom = self.rect_list[0].y + self.width
		for rect in self.rect_list[1:]: # starts iterating from second item in list
			if rect.x < self.left:
				self.left = rect.x
			elif rect.x + self.width > self.right:
				self.right = rect.x + self.width
			if rect.y < self.top:
				self.top = rect.y
			elif rect.y + self.width > self.bottom:
				self.bottom = rect.y + self.width

	def has_hit_bottom(self):
		return self.bottom >= self.screen_height

	def update_down(self, y):
		self.y += y
		for rect in self.rect_list:
			rect.move_ip(0, y)
		self.find_edges()

	def update_left(self):
		if self.left > 0:
			self.x -= self.width
			for rect in self.rect_list:
				rect.move_ip(-self.width, 0)
			self.find_edges()

	def update_right(self):
		if self.right < self.screen_width:
			self.x += self.width
			for rect in self.rect_list:
				rect.move_ip(self.width, 0)
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
		for rect in self.rect_list:
			rect.x -= self.x
			rect.y -= self.y
			x_new = rect.x * math.cos(self.rad) - rect.y * math.sin(self.rad)
			y_new = rect.x * math.sin(self.rad) + rect.y * math.cos(self.rad)
			rect.x = x_new + self.x
			rect.y = y_new + self.y
		self.find_edges()
		self.check_sides()

	def has_collide(self, pieces):
		for rect in self.rect_list:
			for piece in pieces:
				if not(rect.collidelist(piece.rect_list) == -1):
					return True
		return False