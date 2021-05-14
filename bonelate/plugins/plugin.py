#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/4/28 17:41
# @Author : 詹荣瑞
# @File : plugin.py
# @desc : 本代码未经授权禁止商用
class Plugin(object):

    def __init__(self, type):
        self.type = type
        self.data = None

    def __call__(self, data: dict) -> dict:
        if isinstance(data, self.type):
            data = self.transform(data)
        elif isinstance(data, dict):
            for key, value in data.items():
                data[key] = self(value)
        elif isinstance(data, list):
            for index, d in enumerate(data):
                data[index] = self(d)
        return data

    def transform(self, data) -> str:
        raise NotImplementedError
