#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/8/16 下午1:43
# @Author  : XuJieYa
# @FileName: responsibility.py
# @Software: PyCharm
from abc import ABCMeta, abstractmethod


class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self, day):
        pass


class GeneralManager(Handler):
    def handle_leave(self, day):
        if day <= 10:
            print("总经理准假%d天" % day)
        else:
            print("你还是走吧---")


class DepartmentManager(Handler):
    def __init__(self):
        self.next = GeneralManager()

    def handle_leave(self, day):
        if day <= 5:
            print("部门经理准假%d天" % day)
        else:
            print("去找总经理吧---")
            self.next.handle_leave(day)


class ProjectDirector(Handler):
    def __init__(self):
        self.next = DepartmentManager()

    def handle_leave(self, day):
        if day <= 1:
            print("项目主管准假%d天" % day)
        else:
            print("去找上级领导吧---")
            self.next.handle_leave(day)


day = 8
h = ProjectDirector()
h.handle_leave(day)