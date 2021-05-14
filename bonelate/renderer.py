#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/3/31 20:26
# @Author : 詹荣瑞
# @File : renderer.py
# @desc : 本代码未经授权禁止商用
import json
from typing import Union, Iterable, Callable
from bonelate.parser import parse
from bonelate.plugins import NumberPlugin, SympyPlugin
from bonelate.utils import get_scope, get_string


class Renderer(object):

    def __init__(self, data: dict, plugins: Iterable[Callable] = ()):
        self.data = data
        self.scopes = [data]
        for p in plugins:
            self.data = p(self.data)

    def __call__(self, template: list) -> str:
        return self.render(template)

    def block_render(self, flag, value) -> str:
        scope = self.scopes[-1]
        if flag == "v":
            return get_string(scope, value)
        elif flag == "p":
            # print(parse(scope[value]))
            return self.render(
                parse(get_string(scope, value))
            )
        elif flag[0] == "!":
            key, contents = value[0], value[1:]
            # print(key)
            scope = get_scope(scope, key)
            output = []
            if isinstance(scope, dict):
                self.scopes.append(scope)
                output += [self.render(contents)]
                self.scopes.pop()
            elif isinstance(scope, Iterable):
                for s in scope:
                    self.scopes.append(s)
                    output += [self.render(contents)]
                    self.scopes.pop()
            return flag[1].join(output)
        else:  # flag == "?"
            key, contents = value[0], value[1:]
            scope = get_scope(scope, key)
            if not scope:
                return self.render(contents)
            return ""

    def render(self, template: list) -> str:
        output = ""
        for flag, value in template:
            if flag == "l":
                output += value
            else:
                output += self.block_render(flag, value)
        return output

    def use_plugin(self, plugin):
        self.data = plugin(self.data)


def render(template: Union[str, list], data: dict) -> str:
    if isinstance(template, str):
        template = parse(template)
    return Renderer(data, [
        NumberPlugin(float_precision=2),
        SympyPlugin(),
    ]).render(template)


def render_file(path: str, data: Union[dict, str]):
    if isinstance(data, str):
        with open(data, encoding="utf-8") as file:
            data = json.load(file)
    path.replace(".blt", "")
    with open(path + ".blt", encoding="utf-8") as file:
        template = file.read()
    with open(path + ".tex", mode="w", encoding="utf-8") as file:
        file.write(render(template, data))
