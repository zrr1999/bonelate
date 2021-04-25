#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/4/25 19:56
# @Author : 詹荣瑞
# @File : tex_example.py
# @desc : 本代码未经授权禁止商用
from bonelate import render, tokenize

with open("./tex_example.tex", encoding="utf-8") as file:
    test_string = file.read()
print(tokenize(test_string))
print(render(test_string, {
    "accuracy": [
        {"method": "sklearn 逻辑回归", "results": [
            {"val": 90, "train": 80, "test": 80},
            {"val": 90, "train": 80, "test": 80},
            {"val": 90, "train": 80, "test": 80},
            {"val": 90, "train": 80, "test": 80},
            {"val": 90, "train": 80, "test": 80},
        ]},
        {"method": "sklearn 高斯朴素贝叶斯", "results": [
            {"val": 90, "train": 80, "test": 90},
            {"val": 90, "train": 80, "test": 80},
            {"val": 90, "train": 80, "test": 80},
            {"val": 90, "train": 80, "test": 80},
            {"val": 90, "train": 80, "test": 80},
        ]},
        {"method": "个人实现逻辑回归", "results": [
            {"val": 90, "train": 80, "test": 85},
            {"val": 90, "train": 80, "test": 80},
            {"val": 90, "train": 80, "test": 80},
            {"val": 90, "train": 80, "test": 80},
            {"val": 90, "train": 80, "test": 80},
        ]},
        {"method": "个人实现高斯判别分析", "results": [
            {"val": 90, "train": 80, "test": 50},
            {"val": 90, "train": 80, "test": 80},
            {"val": 90, "train": 80, "test": 80},
            {"val": 90, "train": 80, "test": 80},
            {"val": 90, "train": 80, "test": 80},
        ]},
    ]}))
