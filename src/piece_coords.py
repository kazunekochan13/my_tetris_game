from enum import Enum

class piece_coords(Enum):

	o = [[-(1), 0], [-(1), 1], [0, 0], [0, 1]]

	i = [[-(1 * 2), 0], [-(1), 0], [0, 0], [1, 0]]

	s = [[-(1), 1], [0, 0], [0, 1], [1, 0]]

	z = [[-(1), 0], [0, 0], [0, 1], [1, 1]]

	j = [[-(1), 0], [0, 0], [1, 0], [1, 1]]

	l = [[-(1), 0], [-(1), 1], [0, 0], [1, 0]]

	t = [[-(1), 0], [0, 0], [0, 1], [1, 0]]