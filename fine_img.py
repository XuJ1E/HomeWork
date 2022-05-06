# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# Time       ：2022/4/20 18:34
# Author     ：XuJ1E
# version    ：python 3.8
# File       : fine_img.py
"""
from PIL import Image as ImagePIL
import os
import time


def transfer(infile, outfile):
    im = ImagePIL.open(infile)
    im.save(outfile, dpi=(96.0, 96.0))  # 500.0,500.0分别为想要设定的dpi值


if __name__ == '__main__':
    for root, dirs, files in os.walk("F:/datasets/unclothes/"):  # ori_img为需要修改的图片存储的文件夹名字
        print(f'This file has about {len(files)}')
        for item in files:
            list = item.split(".")
            if list[-1] == "jpg":
                try:
                    new_name = list[0] + ".jpg"
                    print(f"Load the image:{new_name}")
                    # os.rename("./data/datasets/unclothes" + item, "./data/datasets/unclothes" + new_name)
                    print(new_name)
                    transfer("F:/datasets/unclothes/" + new_name, "F:/datasets/unclothes/" + new_name)
                except:
                    print(f'This image has some problem, then del {item}')
                    time.sleep(1)
                    del item
                    continue
