#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/5/5 16:43
# @Author : 詹荣瑞
# @File : formula.py
# @desc : 本代码未经授权禁止商用
import sympy as sp
from .plugin import Plugin


class SympyPlugin(Plugin):
    def __init__(self):
        super().__init__(sp.Expr)

    def transform(self, data):
        data = sp.latex(data)
        return data
