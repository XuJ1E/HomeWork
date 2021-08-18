#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/8/18 上午11:36
# @Author  : XuJieYa
# @FileName: minium-type2.py
# @Software: PyCharm
import statistics
from statistics import LinearRegression

from sklearn import linear_model

reg = linear_model.LinearRegression()
reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])

LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
reg.coef_array([0.5, 0.5])
