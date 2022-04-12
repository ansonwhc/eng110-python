# research TDD
# the name of the file starts with "test_unitest" + "file_name"
# the tests class init the unittest superclass

from simple_calc import SimpleCalc
import unittest


class Calctests(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 4), 16)

    def test_division(self):
        self.assertEqual(self.calc.division(4, 2), 2)
