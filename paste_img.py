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


def Square_Generated(read_file):
    '''
        This is the func to transfer the nonsquare img to square img
    '''
    image = Image.open(read_file)  # import img
    w, h = image.size  # get the size of img
    # print(w,h)
    # Create a new img
    # take the size of the longest side of the length, color determines the color to fill the img
    new_image = Image.new('RGB', size=(max(w, h), max(w, h)), color='white')
    # print(background)
    length = int(abs(w - h)//2)  # Fill the shorter side symmetrically
    box = (length, 0) if w < h else (0, length)  # put it in the box
    new_image.paste(image, box)  # Generate new image
    new_image = new_image.resize((256, 256), Image.ANTIALIAS)
    return new_image


source_path = './clothes_bing/'  # path of nonsquare img
save_path = './clothes_bing_256_png/'  # path of generate square img
if not os.path.exists(save_path):
    os.mkdir(save_path)

source_path1 = './unclothes_bing/'
save_path1 = './unclothes_bing_256_png/'
if not os.path.exists(save_path1):
    os.mkdir(save_path1)


file_names = os.listdir(source_path)  # load the img name of nonsquare
for i in range(len(file_names)):
    img = Square_Generated(source_path + file_names[i])
    img.save(save_path + file_names[i], 'PNG')  # save square img
    print('Processing number', i)
    print(img.size)


file_names1 = os.listdir(source_path1)
for i in range(len(file_names1)):
    img = Square_Generated(source_path1 + file_names1[i])
    img.save(save_path1 + file_names1[i], 'PNG')
    print('Processing number', i)
    print(img.size)
