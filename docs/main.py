#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/4/29 17:17
# @Author : 詹荣瑞
# @File : main.py
# @desc : 本代码未经授权禁止商用
from bonelate import render_file

data = {"sections": [
    {"content": r"Bonelate 是一个基于 pyparsing 针对 LaTeX 的类似 mustache 语言的模版渲染器。"
                r"与采取 mustache 的其他模板渲染器相比（例如chevron或pymustache），"
                r"Bonelate 针对 LaTeX 的语法做了很多优化，使模板文件在不渲染的情况下也可使用 LaTeX 工具编译通过。"
                r"同时Bonelate的实现极为简短，Tokenizer 类仅有 23 行，Renderer 类仅有51行。"},
    {"title": "优势", "content": "Bonelate 是参考 mustache 且针对 LaTeX 的语法微调了标记符，"
                               "原本的`{{#partial}}`改为`{{!partial}}`，"
                               "从而在不渲染的情况下 LaTeX 编译时也不会报错。"
                               "通过 Bonelate，用户可以很方便的将现有 LaTeX 项目渐进地转换为 BoneTeX 项目。"},
]}

render_file("./bonelate", data)
