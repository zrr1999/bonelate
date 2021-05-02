#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/5/2 17:24
# @Author : 詹荣瑞
# @File : simple_example.py
# @desc : 本代码未经授权禁止商用
from bonelate import render, parse

test_string = r"\LaTeX{} is a {{var}} typesetting system.{{!vars}}.{{/vars}}"
print(render(test_string, {
    "var": "high-quality",
    "vars": list(range(10)),
}))
