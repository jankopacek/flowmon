import unittest
import math
import shapes

class TestShapes(unittest.TestCase):
    """
    For now only trivial implementation
    Run python tests.py
    """

    def test_square(self):
        s = shapes.Shape.get_shape('square', 2)
        self.assertEqual(s.calc_area(), 4, "Area calculation mismatch!")
        self.assertEqual(s.calc_circumference(), 8, "Circumference calculation mismatch!")

    def test_rectangle(self):
        s = shapes.Shape.get_shape('rectangle', 2, 3)
        self.assertEqual(s.calc_area(), 6, "Area calculation mismatch!")
        self.assertEqual(s.calc_circumference(), 10, "Circumference calculation mismatch!")

    def test_trianle(self):
        s = shapes.Shape.get_shape('triangle', 3, 4, 5)
        self.assertEqual(s.calc_area(), 6, "Area calculation mismatch!")
        self.assertEqual(s.calc_circumference(), 12, "Circumference calculation mismatch!")

    def test_circle(self):
        s = shapes.Shape.get_shape('circle', 2)
        self.assertEqual(s.calc_area(), 4 * math.pi, "Area calculation mismatch!")
        self.assertEqual(s.calc_circumference(), 4 * math.pi, "Circumference calculation mismatch!")

if __name__ == '__main__':
    unittest.main()