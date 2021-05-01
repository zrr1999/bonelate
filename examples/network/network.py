#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/5/1 18:49
# @Author : 詹荣瑞
# @File : main.py
# @desc : 本代码未经授权禁止商用
from bonelate import render_file


def list2dict(data: list) -> dict:
    for i, d in enumerate(data):
        if isinstance(d, int):
            data[i] = {"count": d}
        else:
            data[i] = {"count": d[0], "title": d[1]}

    return {
        "layers": data
    }


render_file("./network", list2dict([5, 5, [3, r"Latent\\Representation"], 5, 5]))
# 与如下代码等价
# render_file("./network", {
#     "layers": [
#         {"count": 5},
#         {"count": 5},
#         {"count": 3, "title": r"Latent\\Representation"},
#         {"count": 5},
#         {"count": 5},
#     ],
# })
