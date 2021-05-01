#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/4/30 23:54
# @Author : 詹荣瑞
# @File : token.py
# @desc : 本代码未经授权禁止商用
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Token(object):
    type: str
    level: int
    children: Optional[List["Token"]]
    meta: dict
    block: bool
