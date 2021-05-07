#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/4/28 17:45
# @Author : 詹荣瑞
# @File : number.py
# @desc : 本代码未经授权禁止商用
from .plugin import Plugin


class NumberPlugin(Plugin):

    def __init__(self, float_precision: int = 4):
        super().__init__(float)
        self.precision = float_precision

    def transform(self, data: float) -> str:
        data = format(data, f".{self.precision}f")
        return data
