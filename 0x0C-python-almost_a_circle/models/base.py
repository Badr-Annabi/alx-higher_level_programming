#!/usr/bin/python3


""" Module that defines a Base Class  """
import os
import json
import csv
import turtle


class Base:
    """
        Class Base

        Attributes:  __nb_objects = 0
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(list_dicts)
                file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**dict_) for dict_ in list_dicts]
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as file:
            writer = csv.writer(file)
            list_obj = [bj.width, obj.height, obj.x, obj.y, obj.id]
            if list_objs is not None:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow(list_obj)
                    elif cls.__name__ == "Square":
                        writer.writerow([obj.size, obj.x, obj.y, obj.id])

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        if os.path.exists(filename):
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls(
                                int(row[0]), int(
                                    row[1]), int(
                                        row[2]), int(
                                            row[3]), int(
                                                row[4]),)
                    elif cls.__name__ == "Square":
                        instance = cls(
                                int(row[0]), int(
                                    row[1]), int(
                                        row[2]), int(
                                            row[3]))
                    instances.append(instance)
                return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        import time
        import random

        for rectangle in list_rectangles:
            turtle.fillcolor(random.choice(['red', 'yellow', 'green']))
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            turtle.begin_fill()
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)
            turtle.left(90)
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)
            turtle.left(90)
            turtle.end_fill()

        for square in list_squares:
            turtle.fillcolor(random.choice(['red', 'yellow', 'green']))
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            turtle.begin_fill()
            turtle.forward(square.size)
            turtle.left(90)
            turtle.forward(square.size)
            turtle.left(90)
            turtle.forward(square.size)
            turtle.left(90)
            turtle.forward(square.size)
            turtle.left(90)
            turtle.end_fill()
        time.sleep(5)
