import unittest
from my_module.my_shape import Circle, Rectangle

class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.54, places=2)

    def test_rectangle_area(self):
        rectangle = Rectangle(4, 6)
        self.assertEqual(rectangle.area(), 24)

    def test_rectangle_perimeter(self):
        rectangle = Rectangle(4, 6)
        self.assertEqual(rectangle.perimeter(), 20)

if __name__ == "__main__":
    unittest.main()
