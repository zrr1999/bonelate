#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/4/28 17:45
# @Author : 詹荣瑞
# @File : number.py
# @desc : 本代码未经授权禁止商用
from .plugin import Plugin


class NumberPlugin(Plugin):

    def __init__(self, precision: int = 4):
        self.precision = precision

    def transform(self, data):
        if isinstance(data, float):
            data = format(data, f".{self.precision}f")
        elif isinstance(data, dict):
            for key, value in data.items():
                data[key] = self.transform(value)
        elif isinstance(data, list):
            for index, d in enumerate(data):
                data[index] = self.transform(d)
        return data
