#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/8/16 下午2:53
# @Author  : XuJieYa
# @FileName: strategy.py
# @Software: PyCharm
'''
定义一系列算法，把它们一个个封装起来，并且使它们可互相替换。\
本模式使得算法可独立于使用它的客户而变化。
'''
from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data):
        pass


class FastStrategy(Strategy):
    def execute(self, data):
        print("快速的策略处理%s" % data)


class SlowStrategy(Strategy):
    def execute(self, data):
        print("较慢的策略处理%s" % data)


class Context:
    def __init__(self, strategy, data):
        self.data = data
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.execute(self.data)


data = "[...]"
s1 = FastStrategy()
s2 = SlowStrategy()
context = Context(s1, data)
context.do_strategy()
context.set_strategy(s2)
context.do_strategy()