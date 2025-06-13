class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

v1 = Vector2D(10,10)
v2 = Vector2D(20,20)

v3 = v1 + v2
v4 = v1 - v2
print('v3 :', v3)
print('v4 :', v4)
