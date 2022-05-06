# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# Time       ：2022/4/30 9:50
# Author     ：XuJ1E
# version    ：python 3.8
# File       : square_img.py
"""
from PIL import Image
import os
import numpy as np


def _square(img):
    w, h = img.size
    s = min(h, w)
    sh = (h - s) / 2.0
    sw = (w - s) / 2.0
    cropped_img = img.crop((sw, sh, sw + s, sh + s))
    return cropped_img


def _shrink(cropped_img, side):
    return cropped_img.resize((side, side), resample=Image.LANCZOS)


def square_and_shrink(side, input_dir, output_dir):
    for f in os.listdir(input_dir):
        img = Image.open(input_dir + f)
        cropped_img = _square(img)
        resized_img = _shrink(cropped_img, side)
        resized_img.save(output_dir + f)
    print('Refining the image-----------------')


square_and_shrink(256, './img/', './img_square/')
