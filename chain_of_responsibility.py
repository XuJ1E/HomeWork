#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 下午8:59
# @Author  : XuJieYa
# @FileName: chain_of_responsibility.py
# @Software: PyCharm
from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        f = open(self.filename, 'r', encoding='utf-8')
        print("---读取文件内容---")
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, 'w', encoding='utf-8')
        f.write(content)
        f.close()


class VirtualProxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

    def set_content(self, content):
        if not subj:
            self.subj = RealSubject(self.filename)
        return self.subj.set_content()


class ProtectedProxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = RealSubject(self.filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):
        raise PermissionError("暂无写入权限")



subj = ProtectedProxy("./test.txt")
# subj.set_content("\nending---")
# subj.get_content()
print(subj.get_content())
subj.set_content("finally")