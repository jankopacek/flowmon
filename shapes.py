### #!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import uuid
import math

this_module = sys.modules[__name__]

class ValidationException(Exception):
    """
    ValidationException
    """

class Shape():
    """
    Base shape class
    """
    shape_id = None

    def __init__(self, *args, **kwargs):
        self.shape_id = uuid.uuid4()

    @staticmethod
    def get_shape(shape_type, *args):
        """
        e.g. Shape.get_shape('circle', '2')
        Basic creational method
        """
        try:
            return getattr(this_module, shape_type.capitalize())(*args)
        except AttributeError:
            raise ValidationException("No such shape defined: {}".format(shape_type))
        except TypeError as e:
            raise ValidationException("Bad arguments: {}".format(e))

    def get_positive_float(self, param):
        try:
            ret = float(param)
        except (ValueError, TypeError):
            raise ValidationException("Param not float!")
        if ret < 0:
            raise ValidationException("Param should be positive!")
        return ret

    def calc_circumference(self):
        """
        Calculates circumference of shape
        """
        raise NotImplementedError

    def calc_area(self):
        """
        Calculates area of shape
        """
        raise NotImplementedError

class Square(Shape):
    """
    Square shape
    """
    line_length = None

    def __init__(self, line_length, *args, **kwargs):
        super().__init__()
        self.line_length = self.get_positive_float(line_length)

    def calc_circumference(self):
        return 4 * self.line_length

    def calc_area(self):
        return self.line_length ** 2

class Rectangle(Shape):
    """
    Rectangle shape
    """
    line_a_length = line_b_length = None

    def __init__(self, line_a_length, line_b_length, *args, **kwargs):
        super().__init__()
        self.line_a_length = self.get_positive_float(line_a_length)
        self.line_b_length = self.get_positive_float(line_b_length)

    def calc_circumference(self):
        return 2 * self.line_a_length + 2 * self.line_b_length

    def calc_area(self):
        return self.line_a_length * self.line_b_length

class Triangle(Shape):
    """
    Triangle shape
    """
    line_a_length = line_b_length = line_c_length = None

    def __init__(self, line_a_length, line_b_length, line_c_length, *args, **kwargs):
        super().__init__()
        self.line_a_length = self.get_positive_float(line_a_length)
        self.line_b_length = self.get_positive_float(line_b_length)
        self.line_c_length = self.get_positive_float(line_c_length)

    def calc_circumference(self):
        return self.line_a_length + self.line_b_length + self.line_c_length

    def calc_area(self):
        s = self.calc_circumference()/2
        return math.sqrt(s * (s - self.line_a_length) * (s - self.line_b_length) * (s - self.line_c_length))

class Circle(Shape):
    """
    Circle shape
    """
    radius = None

    def __init__(self, radius, *args, **kwargs):
        super().__init__()
        self.radius = self.get_positive_float(radius)

    def calc_circumference(self):
        return 2 * math.pi * self.radius

    def calc_area(self):
        return math.pi * self.radius ** 2
