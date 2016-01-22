# /usr/bin/env python3

"""
Refined Abstraction
"""


class CircleShape(object):
    def __init__(self, x, y, radius, drawing_api):
        self.x = x
        self.y = y
        self.radius = radius
        self.api = drawing_api

    # low-level: Implementation specific
    def draw(self):
        self.api.draw_circle(self.x, self.y, self.radius)

    # high-level: Abstraction specific
    def scale(self, pct):
        self.radius *= pct


class DrawingAPI1(object):
    def draw_circle(self, x, y, radius):
        print("API1.circle at {x},{y} {radius}".format(x=x, y=y, radius=radius))


class DrawingAPI2(object):
    def draw_circle(self, x, y, radius):
        print("API2.circle at {x},{y} {radius}".format(x=x, y=y, radius=radius))


def main():
    shapes = (
        CircleShape(1, 2, 3, DrawingAPI1()), CircleShape(5, 7, 11, DrawingAPI2())
    )

    for shape in shapes:
        shape.scale(2.5)
        shape.draw()


if __name__ == '__main__':
    main()
