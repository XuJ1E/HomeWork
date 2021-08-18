#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/8/18 上午11:40
# @Author  : XuJieYa
# @FileName: K-临近算法.py
# @Software: PyCharm
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import os


# Tanimoto距离 计算数据集间的距离
def tanimoto(data, person1, person2):
    n = len(person2)
    combine = [person2[item] for item in range(n) if data.iloc[person1][item] == person2[item]]
    return float(len(combine)) / (2 * n - len(combine))


# kNN核心预测函数 predict(数据集,目标变量,测试数据行,kNN数,计算距离函数)
def predict(data, target, test_data, cnt=3, calculate=tanimoto):
    k = []
    n = len(data)
    for i in range(n):
        score = calculate(data, i, test_data)
        k.append((score, target.iloc[i]))
    k.sort(reverse=True)  # k 获得所有距离元组列表
    rank = k[:cnt]  # rank 获得排序后的前cnt个列表
    only_labels = set(target)  # only_labels 获得唯一标签集合
    dic_labels = {}  # dic_labels 获得标签出现次数
    for i in only_labels:  # 初始化字典
        dic_labels[i] = 0
    for i in rank:  # 计算出现次数
        dic_labels[i[1]] += 1
    result = [(j, i) for i, j in dic_labels.items()]  # i:类 j:次数		需要交换位置以便排序
    result.sort(reverse=True)
    return result[0][1]


# 测试错误率函数 errop_test(数据集DataFrame,目标变量Series)
def error_test(df_data, df_target):
    train_X, test_X, train_y, test_y = train_test_split(df_data, df_target, test_size=0.1, random_state=10)
    error = 0
    n = len(test_X)
    for i in range(n):
        print("{} 条数据运行中...".format(i))
        value = predict(train_X, train_y, test_X.iloc[i], 5)
        if (value != test_y.iloc[i]):
            error += 1
            print("预测值：{0}，真实值：{1}".format(value, test_y.iloc[i]))
    error_rate = error / float(n)
    print("测试结果所得错误率为：{}".format(error_rate))


# 读取文件内容
def img2vector(filename):
    returnVect = np.zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32 * i + j] = int(lineStr[j])
    return returnVect


# 处理数据格式，然后测试错误率
def handwriting():
    train_hwtarget = []
    train_hwdata = []
    train_filelists = os.listdir(r"./digits/trainingDigits")  # 获取数据集
    n = len(train_filelists)
    for i in range(n):
        train_hwdata.append(img2vector(r'./digits/trainingDigits/{0}'.format(train_filelists[i]))[0])
        train_hwtarget.append(int(train_filelists[i].split('_')[0]))
    train_data = pd.DataFrame(train_hwdata)
    train_target = pd.Series(train_hwtarget)
    test_hwtarget = []
    test_hwdata = []
    test_filelists = os.listdir(r"./digits/testDigits")  # 根据文件名获取目标变量
    m = len(test_filelists)
    for i in range(m):
        test_hwdata.append(img2vector(r'./digits/testDigits/{0}'.format(test_filelists[i]))[0])
        test_hwtarget.append(int(test_filelists[i].split('_')[0]))
    test_data = pd.DataFrame(test_hwdata)
    test_target = pd.Series(test_hwtarget)
    print("下面开始进行测试：")

    # error_test(train_data,train_target)		#方法一：直接利用训练数据集 进行划分后求错误率

    error = 0
    for i in range(m):  # 方法二：训练数据集只训练，利用已知答案测试数据集来求错误率
        value = predict(train_data, train_target, test_data.iloc[i, :], 5, tanimoto)
        print("{} 条数据运行中...".format(i))
        if (value != test_target.iloc[i]):
            error += 1
            print("预测错误：预测值：{0}，真实值：{1}".format(value, test_target.iloc[i]))
    error_rate = error / float(m)
    print("测试结果所得错误率为：{}".format(error_rate))


if __name__ == "__main__":
    # 手写数字
    handwriting()