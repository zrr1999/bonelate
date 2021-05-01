#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/5/1 18:49
# @Author : 詹荣瑞
# @File : main.py
# @desc : 本代码未经授权禁止商用
from bonelate import render_file


render_file("./main", {
    "layers": [
        {"count": 5},
        {"count": 5},
        {"count": 3, "title": r"Latent\\Representation"},
        {"count": 5},
        {"count": 5},
    ],
})
