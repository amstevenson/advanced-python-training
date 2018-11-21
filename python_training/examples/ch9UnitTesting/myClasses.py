class Point(object):
    points = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.points += 1

    def where_am_i(self):
        print('Point is at %i,%i' % (self.x, self.y))
        return "{}, {}".format(self.x, self.y)

    def move_by(self, dx,dy):
        self.x += dx
        self.y += dy


class Point3d(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)  # or Point.__init__(x,y)
        self.z = z

    def where_am_i(self):
        print('Point is at %i,%i,%i' % (self.x, self.y, self.z))
        return "{}, {}, {}".format(self.x, self.y, self.z)

if __name__ == '__main__':
    p2 = Point(5, 7)
    p2.move_by(1, 1)
    p2.where_am_i()

    p3 = Point3d(3, 4, 5)
    p3.move_by(1, 1)
    p3.where_am_i()
