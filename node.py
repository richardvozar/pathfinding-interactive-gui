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
    def row(self):
        return self._y

    @row.setter
    def row(self, n):
        self._y = n if 0 <= n < 20 else self._y

    @property
    def col(self):
        return self._x

    @col.setter
    def col(self, n):
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
        self._state = new_state if 0 <= new_state <= 3 else self._state

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


n0 = Node(7, 3, 1, 1, 1, None, 2)
n1 = Node(3, 7, 1, 1, 1, None, 2)
n2 = Node(-5, -9, 1, 1, 1, None, 3)
n3 = Node(-9, -5, 1, 1, 1, None, 3)

print(n1.__dict__)
print(n2.__dict__)

print(n1.distance(n2))
print(n0.distance(n3))
