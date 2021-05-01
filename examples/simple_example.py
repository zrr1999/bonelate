#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/4/24 14:58
# @Author : 詹荣瑞
# @File : simple_example.py
# @desc : 本代码未经授权禁止商用
from bonelate import render, parse
test_string = [
        "I ({{{cannot}}}) be seen!\t",
        "{{ person}} is awesome.",
        "| {{{ string }}} |",
        "{{ !persons  }}awesome {{/persons}}",
        "{{!persons}}{{name}} is awesome. {{/persons}}",
        "{{?undefined}}undefined{{/undefined}}",
        "{{?false}}{{false}}{{/false}}",
        "{{?persons}}empty{{/persons}}",  # empty
        "{{?undefined}}undefined {{person}}{{/undefined}}",
        """
        {{!persons}}{{name}} is awesome.{{/persons}}
        {{person}} is beautiful.
        {{!undefined}}123{{/undefined}}
        {{!is_person}}{{.}} is a person.{{/is_person}}
        """,
    ]
for t in test_string:
    print(render(t, {
        "persons": [{"name": "Xiao Ming"}, {"name": "Yuan Long"}],
        "person": "Xiao Ming",
        "is_person": "Xiao Ming",
        "false": False,
        "string": 3.4234
    }))

