import random


# session 1
# topic: POINT

class Point:
    # anything you put here is a class """..."""
    """
    Class modelling a real life 2D point
    """
    a = 7  # it is outside the init, therefore it is a general attribute (not unique for each individual instance)

    def __init__(self, x, y):  # if def is outside the class it is a function, now it is inside the class is a method,
        # for methods, the first parameters need to be called self, init is the blueprint for creating any type of
        # points
        """"
        Initialise the point instance
        :param x: the x-axis coordinate value
        :param y: the y-axis coordinate value
        """
        self.x = x
        self.y = y  # test


p1 = Point(1, 2)  # create a new instance
p2 = Point(3, 4)
p3 = Point("James", "Jane")  # this is valid, but prob not intended

print(p1.x, p1.y)  # access attributes
print(p1)


# session 2
class Point:
    """
    Class modeling a real life 20 point
    """

    def __init__(self, x, y):
        """
        Initialize the point instance
        :param x: the x-axis coordinate value
        :param y: the y-axis coordinate value
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Magic method that defines how a point is printed
        """
        return f"<{self.x}, {self.y}>"

    def __repr__(self):
        return self.__str__()

    def distance_orig(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __gt__(self, other):  # gt = greater than, use to compare
        """
        Magic method that is called when you do self>other
        :param other: the other point comparing against
        :return: True/False
        """
        return self.distance_orig() > other.distance_orig()

    def __eq__(self, other):  # eq = equal
        return self.distance_orig() == other.distance_orig()


points = []
for i in range(5):
    # create a random point
    p = Point(
        random.randint(-100, 100),
        random.randint(-100, 100)
    )
    # append it to the list
    points.append(p)

for point in points:
    print(point)

print(points)  # repr prints out the list
# points.sort()
p = Point(12, 5)
print(p.distance_orig())

print("unsorted points")
print(points)
print("sorted points")
points.sort()
print(points)

found_equal = 0
count = 0
while True:
    if found_equal == 10:
        break
    p1 = Point(
        random.randint(-100, 100),
        random.randint(-100, 100)
    )
    p2 = Point(
        random.randint(-100, 100),
        random.randint(-100, 100)
    )
    count += 1
    if p1 == p2:
        print(p1, p2)
        found_equal += 1

print(f"probability is 1 in {count/found_equal}")


# topic: COLOR POINT

# from point (file name) import Point (class name)
# I would need to do this if I created a new file, to import/inherit the class into this new file
# here I am using the same file, so no need

class ColorPoint(Point):
    def __init__(self, x, y, color):
        """
        Defines a color point x, y, color
        """
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"<{self.x}, {self.y}>({self.color})"

color_points = []
colors = ["red", "blue", "green", "yellow", "black", "white", "purple"]
for _ in range(5): # underscores is used to show the counter is not important
    p = ColorPoint(
        random.randint(-100, 100),
        random.randint(-100,100),
        random.choice(colors))
    color_points.append(p)
print("random color points:")
print(color_points)
color_points.sort()
print("color points in order:")
print(color_points)


# if I am importing from another file, I need to select everything from class and tab, and in this file write at the
# beginning