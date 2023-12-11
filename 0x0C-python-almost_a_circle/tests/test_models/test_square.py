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

    # def test_class(self):
    #     """Test for Square Class"""
    #     self.assertEqual(str(
    #         Square), "<class 'models.square.Square'>")
    
    # def test_inheritance(self):
    #     """Test inheritance Square->Base"""
    #     self.assertTrue(isinstance(Square, Base))
    
