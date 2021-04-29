#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/4/24 21:46
# @Author : 詹荣瑞
# @File : tokenizer.py
# @desc : 本代码未经授权禁止商用
import pyparsing as pp

white = pp.White()[0, 1].suppress().setName("White")
lbrace = pp.oneOf(["{", "<"]).suppress()
rbrace = pp.oneOf(["}", ">"]).suppress()
double_lbrace = (lbrace * 2 + white).setName("LeftBrace")
double_rbrace = (white + rbrace * 2).setName("RightBrace")


class Tokenizer(object):
    parser = pp.Forward().setName("Tokenizer")
    variable = pp.Regex(r"[-_.A-Za-z0-9\u4e00-\u9fa5]+").setName("Variable")  # 包含数字、字母、下划线、小数点或汉字的变量
    literal = (pp.Regex(r"[^{}]+") | pp.Regex(r"[{][^{}]*}")).addParseAction(
        lambda tokens: [["l", tokens[0]]]
    ).setName("Others")
    tag = (double_lbrace + variable + double_rbrace).addParseAction(
        lambda tokens: [["v", tokens[0]]]
    ).setName("VariableTag")
    bracket_tag = (lbrace + tag + rbrace).addParseAction(
        lambda tokens: [["l", "{"], *tokens, ["l", "}"]]
    ).setName("BracketTag")
    token_list = (lbrace + ~pp.Suppress("{") + parser + rbrace).addParseAction(
        lambda tokens: [["l", "{"], *tokens, ["l", "}"]]
    ).setName("TokenList")
    open_tag = (double_lbrace + pp.oneOf(["!", "?"]) + variable + double_rbrace).setName("OpenTag")
    close_tag = (double_lbrace + pp.Literal("/") + variable + double_rbrace).setName("CloseTag")
    block = (open_tag + parser + close_tag.suppress()).addParseAction(
        lambda tokens: [[tokens[0], tokens[1:]]]
    ).setName("Block")
    single_parser = block | bracket_tag | token_list | tag | literal
    parser <<= single_parser[...].leaveWhitespace()

    def __call__(self, template: str) -> list:
        return self.parser.parseString(template)


tokenize = Tokenizer()
