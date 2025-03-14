# Point #
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
        self.y = y # test


p1 = Point(1, 2)  # create a new instance
p2 = Point(3, 4)

print(p1.x, p1.y)  # access attributes
print(p1)

