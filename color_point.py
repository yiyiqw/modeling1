# session 2 continued
# topic: COLOR POINT

# from point (file name) import Point (class name)
# I would need to do this if I created a new file, to import/inherit the class into this new file
# here I am using the same file, so no need
from point import Point
import random


class ColorPoint(Point):
    def __init__(self, x, y, color):
        """
        Defines a color point x, y, color
        """
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"<{self.x}, {self.y}>({self.color})"


if __name__ == '__main__':
    color_points = []
    colors = ["red", "blue", "green", "yellow", "black", "white", "purple"]
    for _ in range(5):  # underscores is used to show the counter is not important
        p = ColorPoint(
            random.randint(-100, 100),
            random.randint(-100, 100),
            random.choice(colors))
        color_points.append(p)
    print("random color points:")
    print(color_points)
    color_points.sort()
    print("color points in order:")
    print(color_points)

# if I am importing from another file, I need to select everything from class and tab, and in this file write at the
# beginning