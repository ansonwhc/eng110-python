from scrabble_calc import Scrabble
import unittest


class Scrabbletests(unittest.TestCase):

    scrabble = Scrabble()

    def test_calc_str(self):
        self.assertEqual(self.scrabble.score_calculator("Sparta"), 8)

    def test_calc_space_in_str(self):
        self.assertEqual(self.scrabble.score_calculator("Sparta "), 8)

    def test_calc_out_type(self):
        self.assertIsInstance(self.scrabble.score_calculator("Sparta"), (int, float))

    def test_calc_incor_type(self):
        self.assertRaises(AssertionError, self.scrabble.score_calculator, "123")
