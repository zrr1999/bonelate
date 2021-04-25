#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/4/24 21:46
# @Author : 詹荣瑞
# @File : tokenizer.py
# @desc : 本代码未经授权禁止商用
import pyparsing as pp


class Tokenizer(object):
    parser = pp.Forward()
    left = pp.Suppress("{{")
    right = pp.Suppress("}}")
    variable = pp.Regex(r"[._A-Za-z0-9\u4e00-\u9fa5]+")  # 包含数字、字母、下划线、小数点或汉字的变量
    tag = (left + variable + right).addParseAction(
        lambda tokens: [["v", tokens[0]]]
    )
    bracket_tag = (pp.Suppress("{{{") + variable + pp.Suppress("}}}")).addParseAction(
        lambda tokens: [["lv", tokens[0]]]
    )
    open_tag = left + pp.oneOf(["#", "^", "!#"]) + variable + right
    close_tag = left + "/" + variable + right
    literal = (pp.Regex(r"[^{}]+") | pp.Regex(r"[{][^{}]*}")).addParseAction(
        lambda tokens: [["l", tokens[0]]]
    )
    block = (open_tag + parser + close_tag.suppress()).addParseAction(
        lambda tokens: [[tokens[0], tokens[1:]]]
    )
    parser <<= (block | bracket_tag | tag | literal)[...].leaveWhitespace()
    parser = parser.parseString

    def __call__(self, template: str) -> list:
        return self.parser(template)


tokenize = Tokenizer()
