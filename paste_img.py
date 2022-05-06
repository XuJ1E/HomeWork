# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# Time       ：2022/5/6 13:50
# Author     ：XuJ1E
# version    ：python 3.8
# File       : paste_img.py
"""
from PIL import Image
import os


def Square_Generated(read_file):  # 创建一个函数用来产生所需要的正方形图片转化
    image = Image.open(read_file)  # 导入图片
    w, h = image.size  # 得到图片的大小
    # print(w,h)
    new_image = Image.new('RGB', size=(max(w, h), max(w, h)), color='white')  # 创建新的一个图片，大小取长款中最长的一边，color决定了图片中填充的颜色
    # print(background)
    length = int(abs(w - h)//2)  # 在较短一侧进行对称填充
    box = (length, 0) if w < h else (0, length)  # 放在box中
    new_image.paste(image, box)  # 产生新的图片
    new_image = new_image.resize((256, 256))  # 对图片进行缩放处理，这一步可以省略，GPU内存不足了，只能缩小跑CNN，试试效果
    return new_image


source_path = './datasets/unclothes_new/'  # 矩形图片存放的路径
save_path = './datasets/unclothes_new_out/'  # 新产生的正方形图片存放的路径
if not os.path.exists(save_path):
    os.mkdir(save_path)

file_names = os.listdir(source_path)  # 获取矩形图片的名字
for i in range(len(file_names)):  # 循环批量处理
    img = Square_Generated(source_path + file_names[i])  # 通过函数批量获取新的正方形图片
    img.save(save_path + file_names[i], 'PNG')  # 保存图片
    print('number', i)
    print(img)
