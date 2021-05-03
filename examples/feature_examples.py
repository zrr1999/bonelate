#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/5/2 22:44
# @Author : 詹荣瑞
# @File : feature_examples.py
# @desc : 本代码未经授权禁止商用
from bonelate import render, parse

test_string = [
    "{{!mat:&}}{{.}}{{/mat}}",
    "{{!mat}}{{!.:&}} {{.}} {{/.}}\\\\\n{{/mat}}",
]
for t in test_string:
    # print(parse(t))
    print(render(t, {
        "mat": [[1, 2, 3], [1, 2, 3]],
    }))
