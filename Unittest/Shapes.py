# Using TDD, create a Rectangle class. It should be initialized with width and height.
# It should have the following methods: get_area, get_perimeter.
# Create a Square class.
# It should be initialized with length.


class Parallelogram:
    def __init__(self, width=None, height=None, side=None):
        self.width = width
        self.height = height
        self.side = side

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        if self.side is not None:
            return 2 * self.width + 2 * self.side

        return 2 * self.width + 2 * self.height


class Rectangle(Parallelogram):
    def __init__(self, width, height):
        super(Rectangle, self).__init__(width, height)
        self.width = width
        self.height = height


class Square(Rectangle):
    def __init__(self, side):
        super(Square, self).__init__(side, side)


class Shapetest:
    def __init__(self, shape_class, **kwargs):
        self.shape_class = shape_class(**kwargs)

st = Shapetest(Square, side=2)
    # assert st.side == 2