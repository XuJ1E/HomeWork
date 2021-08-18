#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 下午2:23
# @Author  : XuJieYa
# @FileName: Bridge.py
# @Software: PyCharm
from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        pass


class Rectangle(Shape):
    name = "长方形"

    def draw(self):
        self.color.paint(self)


class Circle(Shape):
    name = "圆形"

    def draw(self):
        self.color.paint(self)


class Red(Color):
    def paint(self, shape):
        print("红色的%s" % shape.name)


class Green(Color):
    def paint(self, shape):
        print("绿色的%s" % shape.name)


shape = Rectangle(Red())
shape.draw()

shape2 = Circle(Green())
shape2.draw()
