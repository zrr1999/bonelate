#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/4/24 14:58
# @Author : 詹荣瑞
# @File : example.py
# @desc : 本代码未经授权禁止商用
from bonelate import render
from minibonelate import render as mini_render


test_string = [
        "{{person}} is awesome.",
        "{{#persons}} awesome {{/persons}}",
        "{{#persons}}{{name}} is awesome.{{/persons}}",
        "{{!#undefined}} undefined{{/undefined}}",
        "{{!#not_person}} not_person{{/not_person}}",
        "{{!#persons}} error{{/persons}}",
        "{{!#undefined}} undefined {{person}} {{/undefined}}",
        """
        {{#persons}}{{name}} is awesome.{{/persons}}
        {{person}} is beautiful.
        {{#is_person}}{{.}} is a person.{{/is_person}}
        """,
    ]
for t in test_string:
    print(render(t, {
        "persons": [{"name": "Xiao Ming"}, {"name": "Yuan Longping"}],
        "person": "Xiao Ming",
        "is_person": "Xiao Ming",
        "not_person": False
    }))
    print(mini_render(t, {
        "persons": [{"name": "Xiao Ming"}, {"name": "Yuan Longping"}],
        "person": "Xiao Ming",
        "is_person": "Xiao Ming",
        "not_person": False
    }))

