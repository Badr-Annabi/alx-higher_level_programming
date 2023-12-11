#!/usr/bin/python3
"""
    This is an unittest file testing Rectangle class
"""
import unittest
from unittest.mock import patch
from io import StringIO
import inspect
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_rectangle_is_class(self):
        self.assertTrue(inspect.isclass(Rectangle))

    def test_rectangle_is_subclass_base(self):
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(issubclass(Base, Rectangle))

    def test_is_instance(self):
        r = Rectangle(10, 12)
        self.assertTrue(isinstance(r, Rectangle))

    def test_is_type(self):
        r = Rectangle(15, 41)
        self.assertTrue(type(r) is Rectangle)

    def test_private_attribute(self):
        r = Rectangle(12, 4)
        self.assertEqual(r.id, r._Base__nb_objects)
        r1 = Rectangle(12, 4, 5)
        self.assertEqual(r1.id, r._Base__nb_objects)
        r2 = Rectangle(12, 4, 6, 7)
        self.assertEqual(r2.id, r._Base__nb_objects)
        r3 = Rectangle(12, 4, 8, 9, 98)

        self.assertEqual(r._Rectangle__width, 12)
        self.assertEqual(r._Rectangle__height, 4)
        self.assertEqual(r._Rectangle__x, 0)
        self.assertEqual(r._Rectangle__y, 0)

        self.assertEqual(r1._Rectangle__width, 12)
        self.assertEqual(r1._Rectangle__height, 4)
        self.assertEqual(r1._Rectangle__x, 5)
        self.assertEqual(r1._Rectangle__y, 0)

        self.assertEqual(r2._Rectangle__width, 12)
        self.assertEqual(r2._Rectangle__height, 4)
        self.assertEqual(r2._Rectangle__x, 6)
        self.assertEqual(r2._Rectangle__y, 7)

        self.assertEqual(r3._Rectangle__width, 12)
        self.assertEqual(r3._Rectangle__height, 4)
        self.assertEqual(r3._Rectangle__x, 8)
        self.assertEqual(r3._Rectangle__y, 9)
        self.assertEqual(r3.id, 98)

    def test_getter(self):
        r = Rectangle(12, 4)
        self.assertEqual(r.id, r._Base__nb_objects)
        r1 = Rectangle(12, 4, 5)
        self.assertEqual(r1.id, r._Base__nb_objects)
        r2 = Rectangle(12, 4, 6, 7)
        self.assertEqual(r2.id, r._Base__nb_objects)
        r3 = Rectangle(12, 4, 8, 9, 98)

        self.assertEqual(r.width, 12)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 0)

        self.assertEqual(r2.width, 12)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 6)
        self.assertEqual(r2.y, 7)

        self.assertEqual(r3.width, 12)
        self.assertEqual(r3.height, 4)
        self.assertEqual(r3.x, 8)
        self.assertEqual(r3.y, 9)
        self.assertEqual(r3.id, 98)

    def test_setter(self):
        r = Rectangle(10, 5)
        r.width = 12
        self.assertEqual(r.id, r._Base__nb_objects)

        r1 = Rectangle(10, 5)
        r1.width = 12
        r1.height = 4
        self.assertEqual(r1.id, r._Base__nb_objects)

        r2 = Rectangle(10, 5)
        r2.width = 12
        r2.height = 4
        r2.x = 6
        self.assertEqual(r2.id, r._Base__nb_objects)

        r3 = Rectangle(10, 5)
        r3.width = 12
        r3.height = 4
        r3.y = 9
        r3.x = 8
        r3.id = 98

        self.assertEqual(r.width, 12)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        self.assertEqual(r2.width, 12)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 6)
        self.assertEqual(r2.y, 0)

        self.assertEqual(r3.width, 12)
        self.assertEqual(r3.height, 4)
        self.assertEqual(r3.x, 8)
        self.assertEqual(r3.y, 9)
        self.assertEqual(r3.id, 98)

    def test_raises(self):

        """ TypeError Exception """
        with self.assertRaises(TypeError) as context:
            r = Rectangle("string", 5)
        self.assertEqual(str(context.exception), "width must be an integer")

        with self.assertRaises(TypeError) as context:
            r1 = Rectangle(5, "string")
        self.assertEqual(str(context.exception), "height must be an integer")

        with self.assertRaises(TypeError) as context:
            r2 = Rectangle(5, 5, "string")
        self.assertEqual(str(context.exception), "x must be an integer")

        with self.assertRaises(TypeError) as context:
            r3 = Rectangle(5, 5, 5, "string")
        self.assertEqual(str(context.exception), "y must be an integer")

        """ ValueError Exception """
        with self.assertRaises(ValueError) as context:
            r = Rectangle(-5, 5)
        self.assertEqual(str(context.exception), "width must be > 0")

        with self.assertRaises(ValueError) as context:
            r1 = Rectangle(5, -5)
        self.assertEqual(str(context.exception), "height must be > 0")

        with self.assertRaises(ValueError) as context:
            r = Rectangle(0, 5)
        self.assertEqual(str(context.exception), "width must be > 0")

        with self.assertRaises(ValueError) as context:
            r1 = Rectangle(5, 0)
        self.assertEqual(str(context.exception), "height must be > 0")

        with self.assertRaises(ValueError) as context:
            r2 = Rectangle(5, 5, -5)
        self.assertEqual(str(context.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as context:
            r3 = Rectangle(5, 5, 5, -5)
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_area(self):
        r1 = Rectangle(3, 2)
        r2 = Rectangle(8, 7, 0, 0, 12)
        area1 = r1.area()
        area2 = r2.area()

        self.assertEqual(area1, 6)
        self.assertEqual(area2, 56)

    def display(self):
        with patch('sys,stdout', new=StringIO()) as fake_stdout:
            r1 = Rectangle(4, 6)
            r2 = Rectangle(2, 2)
            r1.display()
            r2.display()
            self.assertEqual(
                    fake_stdout.getvalue(
                        ), "####\n####\n####\n####\n####\n####\n##\n##\n")


if __name__ == '__main__':
    unittest.main()
