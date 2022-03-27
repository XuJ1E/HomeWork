# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# Time       ：2022/3/27 14:28
# Author     ：XuJie
# version    ：python 3.8
# File       : __init__.py.py
"""
import math
import random


class Chromosome(object):
    def __init__(self, bounds, precision):
        super(Chromosome, self).__init__()
        self.x1 = 1
        self.x2 = 1
        self.y = 0
        self.bounds = bounds

        self.code_x1 = ''
        self.code_x2 = ''
        temp1 = (bounds[0][1] - bounds[0][0])*precision
        self.code_x1_length = math.ceil(math.log(temp1, 2))

        temp2 = (bounds[1][1] - bounds[1][0])*precision
        self.code_x2_length = math.ceil(math.log(temp2, 2))

        self.rand_int()
        self.func()

    def rand_int(self):
        for i in range(self.code_x1_length):
            self.code_x1 += str(random.randint(0, 1))

        for i in range(self.code_x2_length):
            self.code_x2 += str(random.randint(0, 1))

    def decoding(self, code_x1, code_x2):
        self.x1 = self.bounds[0][1] + int(code_x1, 2)*(self.bounds[0][1] - self.bounds[0][0])/(2**self.code_x1_length - 1)
        self.x2 = self.bounds[1][0] + int(code_x2, 2)*(self.bounds[1][1] - self.bounds[1][0])/(2**self.code_x2_length - 1)

    def func(self):
        self.decoding(self.code_x1, self.code_x2)
        self.y = 21.5 + self.x1 * math.sin(4 * math.pi * self.x1) + self.x2 * math.sin(20 * math.pi * self.x2)
        # self.y = 21.5 + self.x1*math.sin(4*math.pi*self.x1) + self.x2*math.sin(20*math.pi*self.x2)