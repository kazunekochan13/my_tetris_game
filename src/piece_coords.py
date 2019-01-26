from enum import Enum

class piece_coords(Enum):
	o0 = [[-(1), 0], [-(1), 1], [0, 0], [0, 1]]

	i0 = [[-(1 * 2), 0], [-(1), 0], [0, 0], [1, 0]]
	i1 = [[0, -(2)], [0, -(1)], [0, 0], [0, 1]]

	s0 = [[-(1), 1], [0, 0], [0, 1], [1, 0]]
	s1 = [[0, -(1)], [0, 0], [1, 0], [1, 1]]

	z0 = [[-(1), 0], [0, 0], [0, 1], [1, 1]]
	z1 = [[-(1), 0], [-(1), 1], [0, -(1)], [0, 0]]

	j0 = [[-(1), 0], [0, 0], [1, 0], [1, 1]]
	j1 = [[-(1), 1], [0, -(1)], [0, 0], [0, 1]]
	j2 = [[-(1), -(1)], [-(1), 0], [0, 0], [1, 0]]
	j3 = [[0, -(1)], [0, 0], [0, 1], [1, -(1)]]

	l0 = [[-(1), 0], [-(1), 1], [0, 0], [1, 0]]
	l1 = [[-(1), -(1)], [0, -(1)], [0, 0], [0, 1]]
	l2 = [[-(1), 0], [0, 0], [1, -(1)], [1, 0]]
	l3 = [[0, -(1)], [0, 0], [0, 1], [1, 1]]

	t0 = [[-(1), 0], [0, 0], [0, 1], [1, 0]]
	t1 = [[-(1), 0], [0, -(1)], [0, 0], [0, 1]]
	t2 = [[-(1), 0], [0, -(1)], [0, 0], [1, 0]]
	t3 = [[0, -(1)], [0, 0], [0, 1], [1, 0]]

