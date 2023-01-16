import math

class Node:
    def __init__(self, y, x, f, g, h, parent, state=0):
        self._y = y
        self._x = x
        self._state = state
        self._neighbors = []
        self._f = f
        self._g = g
        self._h = h
        self._parent = parent

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, n):
        self._y = n if 0 <= n < 20 else self._y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, n):
        self._x = n if 0 <= n < 20 else self._x

    @property
    def f(self):
        return self._f

    @f.setter
    def f(self, x):
        self._f = x if 0 <= x < 20 else self._f

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, x):
        self._g = x if 0 <= x < 20 else self._g

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, x):
        self._h = x if 0 <= x < 20 else self._h

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state):
        self._state = new_state if 0 <= new_state <= 6 else self._state

    @property
    def neighbors(self):
        return self._neighbors

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, p):
        self._parent = p if isinstance(p, Node) else None

    def add_neighbor(self, neighbor):
        if isinstance(neighbor, Node) and neighbor.state != 1:
            self._neighbors.append(neighbor)

    def distance(self, n):
        """
        Calculates the euclidean distance between two nodes.
        :param n: Node
        :return distance: float
        """
        if isinstance(n, Node):
            return math.dist([self.row, self.col], [n.row, n.col])

    def is_same(self, other):
        """
        Returns with True if the node from the parameter is the same as the self.
        :param other: Node
        :return: bool
        """
        if isinstance(other, Node):
            return self._x == other.x and self._y == other.y
        else:
            return False


# n0 = Node(7, 3, 1, 1, 1, None, 2)
# n3 = Node(7, 3, 1, 1, 1, None, 2)
# n1 = Node(3, 7, 1, 1, 1, None, 2)
#
# print(n0.is_same(n3))
