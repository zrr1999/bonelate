#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/4/28 17:41
# @Author : 詹荣瑞
# @File : plugin.py
# @desc : 本代码未经授权禁止商用
class Plugin(object):

    def __call__(self, data: dict) -> dict:
        return self.transform(data)

    def transform(self, data: dict) -> dict:
        raise NotImplementedError
