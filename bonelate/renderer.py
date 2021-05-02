#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/3/31 20:26
# @Author : 詹荣瑞
# @File : renderer.py
# @desc : 本代码未经授权禁止商用
from bonelate.parser import parse
from typing import Union, Iterable, Callable
from bonelate.plugins import NumberPlugin


class Renderer(object):

    def __init__(self, data: dict, plugins: Iterable[Callable] = ()):
        self.data = data
        self.scopes = [data]
        for p in plugins:
            self.data = p(self.data)

    def __call__(self, template: list) -> str:
        return self.render(template)

    def block_render(self, flag, value):
        scope = self.scopes[-1]
        if flag == "v":
            if value == ".":
                return str(scope)
            else:
                values = value.split(".")
                for v in values:
                    if v in scope:
                        scope = scope[v]
                    else:
                        return ""
                return str(scope)
        if flag == "p":
            # print(parse(scope[value]))
            return self.render(parse(scope[value]))
            # if value == ".":
            #     return str(scope)
            # else:
            #     values = value.split(".")
            #     for v in values:
            #         if v in scope:
            #             scope = scope[v]
            #         else:
            #             return ""
            #     return str(scope)
        elif flag == "!":
            output = ""
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
            return output
        else:  # flag == "?"
            name, contents = value[0], value[1:]
            values = name.split(".")
            for v in values:
                if v not in scope or not scope[v]:
                    return self.render(contents)
                else:
                    scope = scope[v]
            return ""

    def render(self, template: list) -> str:
        output = ""
        for flag, value in template:
            if flag == "l":
                output += value
            else:
                output += self.block_render(flag, value)
        return output


def render_file(path: str, data: dict):
    with open(path + ".blt", encoding="utf-8") as file:
        template = file.read()
    with open(path + ".tex", mode="w", encoding="utf-8") as file:
        file.write(render(template, data))


def render(template: Union[str, list], data: dict) -> str:
    if isinstance(template, str):
        template = parse(template)
    return Renderer(data, [
        NumberPlugin(float_precision=2)
    ]).render(template)
