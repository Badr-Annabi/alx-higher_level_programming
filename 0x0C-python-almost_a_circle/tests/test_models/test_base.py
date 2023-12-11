#!/usr/bin/python3
"""
    This is a unittest file for class Base
"""
import unittest
import inspect
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    """Test cases"""
    def setUp(self):
        Base.__nb_objects = 0
        pass
        
    def test_base_is_class(self):
        self.assertTrue(inspect.isclass(Base))

    def test_base_is_not_none(self):
        b = Base()
        self.assertIsNotNone(b)

    def test_base_is_instance(self):
        b = Base()
        self.assertTrue(isinstance(b, Base))

    def test_base_is_type(self):
        b = Base()
        self.assertTrue(type(b) is Base)

    def test_create_instance_without_passing_id(self):
        obj_b = Base()
        self.assertIsNotNone(obj_b.id)

    def test_create_instance_with_passing_id(self):
        obj = Base(id=5)
        self.assertEqual(obj.id, 5)

    def test_create_instance_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_create_instance_incremental_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id + 1, obj2.id)

    def test_create_instance_nb_objects(self):
        obj_id = Base()
        self.assertEqual(obj_id.id, Base._Base__nb_objects)

    def test_D_constructor(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_D_constructor_args_2(self):
        '''Tests constructor signature with 2 notself args.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        msg = "__init__() takes from 1 to 2 positional arguments but 3 \
were given"
        self.assertEqual(str(e.exception), msg)

#     "------------Tests for task 15 ----------"

#     def test_to_json_string(self):
#         ''' Tests to_json_string() method '''
#         with self.assertRaises(TypeError) as ex:
#             Base.to_json_string()
#         msg = "Base.to_json_string() missing 1 required positional argument: \
# 'list_dictionaries'"
#         self.assertEqual(str(ex.exception), msg)

#         self.assertEqual(Base.to_json_string(None), "[]")
#         self.assertEqual(Base.to_json_string([]), "[]")

#         data = [{'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}]
#         self.assertEqual(len(Base.to_json_string(data)), len(str(data)))

#         data = [{"testtest": 989898}]
#         self.assertEqual(Base.to_json_string(data), '[{"testtest": 989898}]')

#         data = [{}]
#         self.assertEqual(Base.to_json_string(data), '[{}]')

#         r = Rectangle(1, 2, 3, 4)
#         dic = r.to_dictionary()
#         json_dic = Base.to_json_string([dic])
#         dic = str([dic])
#         dic = dic.replace("'", '"')
#         self.assertEqual(dic, json_dic)

#         r1 = Rectangle(1, 2, 3, 4)
#         r2 = Rectangle(1, 2)
#         r3 = Rectangle(2, 4, 6)
#         dictionary = [
#                 r1.to_dictionary(
#                     ), r2.to_dictionary(), r3.to_dictionary()]
#         json_dictionary = Base.to_json_string(dictionary)
#         dictionary = str(dictionary)
#         dictionary = dictionary.replace("'", '"')
#         self.assertEqual(dictionary, json_dictionary)

#     '========= Test for task 17 ==============='

#     def test_from_json_string(self):
#         ''' Tests from_json_string method '''
#         with self.assertRaises(TypeError) as ex:
#             Base.from_json_string()
#         msg = "Base.from_json_string() missing" \
#               " 1 required positional argument:" \
#               " 'json_string'"
#         self.assertEqual(str(ex.exception), msg)

#         self.assertEqual(Base.from_json_string(None), [])
#         self.assertEqual(Base.from_json_string(""), [])

#         s = '[{"x":1, "y": 2, "width": 3, "id": 4, "height": 5}]'
#         d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]

#         self.assertEqual(Base.from_json_string(s), d)

#         s = '[{}, {}]'
#         d = [{}, {}]

#         self.assertEqual(Base.from_json_string(s), d)

#     '========= Test for task 16 ==============='

#     def test_save_to_file(self):
#         ''' Tests save to file '''

#         d = [{'id': 4, 'width': 3, 'height': 5, 'x': 1, 'y': 2}]
#         r = Rectangle(3, 5, 1, 2, 4)
#         Rectangle.save_to_file([r])

#         with open("Rectangle.json", "r") as file:
#             self.assertEqual(str(d).replace("'", '"'), file.read())

#         Rectangle.save_to_file(None)
#         with open("Rectangle.json", "r") as file:
#             self.assertEqual(file.read(), "[]")

#         d = [{'id': 1, 'size': 2, 'x': 5, 'y': 0}]
#         sq = Square(2, 5, 0, 1)

#         Square.save_to_file([sq])

#         with open("Square.json", "r") as file:
#             self.assertEqual(file.read(), str(d).replace("'", '"'))

#         Square.save_to_file(None)
#         with open("Square.json", "r") as file:
#             self.assertEqual(file.read(), "[]")


if __name__ == "__main__":
    unittest.main()
