#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/5/1 12:59
# @Author : 詹荣瑞
# @File : rule.py
# @desc : 本代码未经授权禁止商用
import pyparsing as pp
from dataclasses import dataclass
from typing import Callable, Union, Iterable
FLAG_VARIABLE = "v"
FLAG_PARTIAL = "p"
FLAG_START_ = "!"
FLAG_START = "?"
FLAG_CLOSE = "/"
SCOPE_RULE = []


@dataclass
class Rule(object):
    name: str
    parser: Union[Callable[[pp.ParserElement], pp.ParserElement], pp.ParserElement]
    actions: Iterable[Callable] = ()

    def __call__(self, parser: pp.ParserElement = None) -> pp.ParserElement:
        # 获取 parser 对象并设置名称
        if isinstance(self.parser, pp.ParserElement):
            parser = self.parser.setName(self.name)
        else:
            parser = self.parser(parser).setName(self.name)

        return parser.addParseAction(*self.actions)


