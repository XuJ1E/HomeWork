#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/8/16 下午2:05
# @Author  : XuJieYa
# @FileName: *observer.py
# @Software: PyCharm
'''
当一个抽象模型有两个方面，其中一个模型依赖于另一个方面，将这两者封装在独立的对象中\
以促使他们可以各自独立地改变和复用。
当一个对象的改变需要同时改变其他对象，而不知道具体有多少对象有待于改变。
目标和观察者之间的抽象耦合最小。
支持广播通信。
'''
from abc import ABCMeta, abstractmethod


class Observe(metaclass=ABCMeta):
    @abstractmethod
    def update(self, notice):
        pass


# 抽象的发布者
class Notice:
    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def detach(self, obs):
        self.observers.remove(obs)

    def notify(self):
        for obs in self.observers:
            obs.update(self)


# 具体的发布者
class StaffNotice(Notice):
    def __init__(self, company_info=None):
        super().__init__()
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notify()


# 具体的订阅者
class Staff(Observe):
    def __init__(self):
        self.company_info = None

    def update(self, notice):
        self.company_info = notice.company_info


notice = StaffNotice("初始化公司信息")
s1 = Staff()
s2 = Staff()
notice.attach(s1)
notice.attach(s2)
notice.company_info = "公司今年发展的非常不错，多亏了大家的努力，在此特意感谢大家的奉献"
print(s1.company_info)
print(s2.company_info)
notice.detach(s2)
notice.company_info = "公司今天发奖金"
print(s1.company_info)
print(s2.company_info)
