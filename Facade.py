#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 下午8:32
# @Author  : XuJieYa
# @FileName: Facade.py
# @Software: PyCharm

class CPU:
    def run(self):
        print("CPU开始运行")

    def stop(self):
        print("CPU停止运行")


class Disk:
    def run(self):
        print("硬盘开始运行")

    def stop(self):
        print("硬盘停止运行")


class Memory:
    def run(self):
        print("内存上电")

    def stop(self):
        print("内存掉电")


class Computer:
    # 初始化定义（实际指继承父类）
    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


computer = Computer()
computer.run()
computer.stop()