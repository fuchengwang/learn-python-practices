"""

73. Write a Python program to calculate midpoints of a line.

"""


class point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def midpoints(self, p):

        x = (self.x + p.x) / 2
        y = (self.y + p.y) / 2
        return point(x, y)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

p1 = point(1, 1)
p2 = point(3, 3)
print(p1.midpoints(p2))

