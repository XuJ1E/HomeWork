#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/8/16 下午3:11
# @Author  : XuJieYa
# @FileName: template.py
# @Software: PyCharm
'''
定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。模板方法使得子类\
可以不改变一个算法的结构即可重新定义该算法的某些特定步骤。
角色：
    抽象类：定义抽象的原子操作（钩子操作）；实现一个模板方法作为算法的架构
    具体类：实现原子操作
使用场景：
    一次性实现一个算法的不变部分
    各个子类中的公共行为应该被提取出来并集中到一个公共父类中以避免代码重复
    控制子类扩展
'''
from abc import ABCMeta, abstractmethod
from time import sleep


class Window(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def repaint(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    # 模板方法
    def run(self):
        self.start()
        while True:
            try:
                self.repaint()
                sleep(1)
            except KeyboardInterrupt:
                break
        self.stop()


class MyWindow(Window):
    def __init__(self, msg):
        self.msg = msg

    def start(self):
        print("窗口初始化")

    def stop(self):
        print("窗口关闭")

    def repaint(self):
        print(self.msg)


MyWindow("hello---").run()