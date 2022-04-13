from unittest import TestCase
import pytest
from Shapes import Rectangle, Square, Parallelogram


# unittest
class shapestest(TestCase):

    rectangle = Rectangle(3, 4)
    square = Square(5)

    def test_rec_area(self):
        self.assertEqual(self.rectangle.get_area(), 12)

    def test_rec_perim(self):
        self.assertEqual(self.rectangle.get_perimeter(), 14)


# func test
def test_rectangle_init():
    func_r = Rectangle(width=2, height=3)
    assert func_r.width == 2


def test_square_init():
    sq = Square(side=2)
    assert sq.width == 2


@pytest.fixture  # can be used as argument
def example_rectangle():
    return Rectangle(width=2, height=3)


@pytest.fixture
def example_square():
    return Square(side=2)


def test_rectangle_area(example_rectangle):
    assert example_rectangle.get_area() == 6


def test_rectangle_perim(example_rectangle):
    assert example_rectangle.get_perimeter() == 10


def test_square_area(example_square):
    assert example_square.get_area() == 4.


def test_square_perim(example_square):
    assert example_square.get_perimeter() == 8.


# init a class for testing
class Shapetest:
    def __init__(self, shape_class, **kwargs):
        self.shape_class = shape_class(**kwargs)

    def assert_area(self, ans_area):
        assert self.shape_class.get_area() == ans_area

    def assert_perim(self, ans_perim):
        assert self.shape_class.get_perimeter() == ans_perim

    def assert_missing_methods(self):
        # TODO: check for missing area and perim methods
        pass

    def assert_notimplemented_methods(self):
        # TODO: if user call a method that is not implemented
        pass


def test_rec():
    r = Shapetest(Rectangle, width=2, height=3)
    r.assert_area(6)
    r.assert_perim(10)


def test_sq():
    sq = Shapetest(Square, side=2)
    sq.assert_area(4)
    sq.assert_perim(8)

# TODO: test para class
# def test_para_init():
#     p = Parallelogram(width=)

