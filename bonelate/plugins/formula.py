#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/5/5 16:43
# @Author : 詹荣瑞
# @File : formula.py
# @desc : 本代码未经授权禁止商用
import sympy as sp
from .plugin import Plugin


class SympyPlugin(Plugin):
    def transform(self, data):
        if isinstance(data, sp.Expr):
            data = sp.latex(data)
        elif isinstance(data, dict):
            for key, value in data.items():
                data[key] = self.transform(value)
        elif isinstance(data, list):
            for index, d in enumerate(data):
                data[index] = self.transform(d)
        return data
