#!/usr/bin/python3
"""Module for Square unittest"""
import unittest
from models.base import Base
from models.square import Square
import io


class TestSquare(unittest.TestCase):
    """Test Base Class"""

    def setUp(self):
        Base.__nb_objects = 0
        pass

    '--------------- Test #2 ------------------'

    def test_class(self):
        """Test for Square Class"""
        self.assertEqual(str(
            Square), "<class 'models.square.Square'>")
    
    def test_inheritance(self):
        """Test inheritance Square->Base"""
        self.assertTrue(issubclass(Square, Base))
    
    def test_constructor(self):
        """Test constructor"""
        with self.assertRaises(TypeError) as e:
            r = Square()
    
    def test_constructor_args(self):
        """Test constructor"""
        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, 5, 8, 9)
        s = "__init__() takes from 2 to 5 positional arguments but 6 \
were given"

        self.assertEqual(str(e.exception), s)
    
    def test_raises(self):

        """ Test cases"""
        r = Square(10)
        self.assertEqual(str(type(r)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(r, Base))
        d = {'_Rectangle__height': 10, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(r.__dict__, d)
        with self.assertRaises(TypeError) as context:
            s = Square("string")
        self.assertEqual(str(context.exception), "width must be an integer")

        with self.assertRaises(TypeError) as context:
            s = Square(5, 5, "string")
        self.assertEqual(str(context.exception), "x must be an integer")

        with self.assertRaises(TypeError) as context:
            s = Square(5, 5, 5, "string")
        self.assertEqual(str(context.exception), "y must be an integer")

        """ ValueError Exception """
        with self.assertRaises(ValueError) as context:
            s = Square(-5, 5)
        self.assertEqual(str(context.exception), "width must be > 0")

        with self.assertRaises(ValueError) as context:
            s = Square(0, 5)
        self.assertEqual(str(context.exception), "width must be > 0")

        with self.assertRaises(ValueError) as context:
            s = Square(5, 5, -5)
        self.assertEqual(str(context.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as context:
            s = Square(5, 5, 5, -5)
        self.assertEqual(str(context.exception), "y must be >= 0")


if __name__ == '__main__':
    unittest.main()