class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return iter((self.x, self.y))

    def __getitem__(self, key):
        return (self.x, self.y)[key]

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __rsub__(self, other):
        return Vector(other.x - self.x, other.y - self.y)

    def __mul__(self, other):
        assert type(other) in (int, long, float)
        return Vector(self.x * other, self.y * other)

    __rmul__ = __mul__

    def __imul__(self, other):
        assert type(other) in (int, long, float)
        self.x *= other
        self.y *= other
        return self

    def __repr__(self):
        return "(%.2f, %.2f)" % (self.x, self.y)
