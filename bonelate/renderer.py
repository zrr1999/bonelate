#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/3/31 20:26
# @Author : 詹荣瑞
# @File : renderer.py
# @desc : 本代码未经授权禁止商用
import pyparsing as pp
import re
from typing import Union


class Renderer(object):
    parser = pp.Forward()
    left = pp.Suppress("{{")
    right = pp.Suppress("}}")
    variable = pp.Regex(re.compile(r"[._A-Za-z\u4e00-\u9fa5]+"))
    tag = (left + variable + right).addParseAction(
        lambda tokens: [["v", tokens[0]]]
    )
    open_tag = left + pp.oneOf(["#", "^"]) + variable + right
    close_tag = left + "/" + variable + right
    literal = (pp.Regex(re.compile(r"[^{}]+")) | pp.Regex(re.compile(r"[{][^{}]}"))).addParseAction(
        lambda tokens: [["l", tokens[0]]]
    )
    block = (open_tag + parser + pp.Suppress(close_tag)).addParseAction(
        lambda tokens: [[tokens[0], tokens[1:]]]
    )

    def __init__(self, data: dict):
        self.parser <<= (self.block | self.tag | self.literal)[...].leaveWhitespace()
        self.data = data
        self.scopes = [data]

    def __call__(self, template: str) -> str:
        return self.render(template)

    def render(self, template: Union[str, list]) -> str:
        if isinstance(template, str):
            template = self.parser.parseString(template)
        output = ""
        for flag, value in template:
            if flag == "l":
                output += value
            else:
                scope = self.scopes[-1]
                if flag == "v":
                    if value == ".":
                        output += str(scope)
                    elif value in scope:
                        output += str(scope[value])
                elif flag == "#":
                    name, contents = value[0], value[1:]
                    if name in scope:
                        scope = scope[name]
                        if isinstance(scope, list):
                            for s in scope:
                                self.scopes.append(s)
                                output += self.render(contents)
                                self.scopes.pop()
                        else:
                            self.scopes.append(scope)
                            output += self.render(contents)
                            self.scopes.pop()
                else:  # flag == "^"
                    name, contents = value[0], value[1:]
                    if name not in scope or not scope[name]:
                        output += self.render(contents)

        return output


def render(template: str, data: dict) -> str:
    return Renderer(data).render(template)
