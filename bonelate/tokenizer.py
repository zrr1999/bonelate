#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/4/24 21:46
# @Author : 詹荣瑞
# @File : tokenizer.py
# @desc : 本代码未经授权禁止商用
import pyparsing as pp

white = pp.Suppress(pp.White()[0, 1])
lbrace = pp.Suppress(pp.oneOf(["{", "<"]))
rbrace = pp.Suppress(pp.oneOf(["}", ">"]))
double_lbrace = lbrace * 2 + white
double_rbrace = white + rbrace * 2


class Tokenizer(object):
    parser = pp.Forward()
    variable = pp.Regex(r"[-_.A-Za-z0-9\u4e00-\u9fa5]+")  # 包含数字、字母、下划线、小数点或汉字的变量
    literal = (pp.Regex(r"[^{}]+") | pp.Regex(r"[{][^{}]*}")).addParseAction(
        lambda tokens: [["l", tokens[0]]]
    )
    tag = (double_lbrace + variable + double_rbrace).addParseAction(
        lambda tokens: [["v", tokens[0]]]
    )
    bracket_tag = (lbrace + double_lbrace + variable + rbrace + double_rbrace).addParseAction(
        lambda tokens: [["lv", tokens[0]]]
    )
    token_list = (lbrace + ~pp.Suppress("{") + parser + rbrace).addParseAction(
        lambda tokens: [["l", "{"], *tokens, ["l", "}"]]
    )
    open_tag = double_lbrace + pp.oneOf(["!", "?"]) + variable + double_rbrace
    close_tag = double_lbrace + "/" + variable + double_rbrace
    block = (open_tag + parser + close_tag.suppress()).addParseAction(
        lambda tokens: [[tokens[0], tokens[1:]]]
    )
    parser <<= (block | bracket_tag | token_list | tag | literal)[...].leaveWhitespace()
    parser = parser.parseString

    def __call__(self, template: str) -> list:
        return self.parser(template)


tokenize = Tokenizer()
