#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/4/25 22:15
# @Author : 詹荣瑞
# @File : utils.py
# @desc : 本代码未经授权禁止商用
def get_scope(scope, key: str):
    if key == ".":
        return scope
    elif isinstance(scope, dict):
        keys = key.split(".")
        for v in keys:
            if v in scope:
                scope = scope[v]
            else:
                return
        return scope


def get_string(scope, key: str) -> str:
    scope = get_scope(scope, key)
    if scope is None:
        return ""
    else:
        return str(scope)
