#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/4/24 21:46
# @Author : 詹荣瑞
# @File : parser.py
# @desc : 本代码未经授权禁止商用
from bonelate.rule import Rule
import pyparsing as pp

WHITE = pp.Regex(r"\s*").suppress().setName("White")
VARIABLE = pp.Regex(r"[.A-Za-z0-9-_&\u4e00-\u9fa5]+")
LBRACE = pp.oneOf(["{", "<"]).suppress()
RBRACE = pp.oneOf(["}", ">"]).suppress()

DOUBLE_LBRACE = LBRACE * 2 + WHITE
DOUBLE_RBRACE = WHITE + RBRACE * 2
TRIPLE_LBRACE = LBRACE * 3 + WHITE
TRIPLE_RBRACE = WHITE + RBRACE * 3
OPTION = (pp.Suppress(":") + VARIABLE)[0, 1].addParseAction(
    lambda tokens: tokens or ""
)

TAG = (DOUBLE_LBRACE + VARIABLE + DOUBLE_RBRACE).addParseAction(
    lambda tokens: [["v", tokens[0]]]
)
OPEN_TAG = DOUBLE_LBRACE + pp.oneOf(["!", "?"]) + VARIABLE + OPTION + DOUBLE_RBRACE + pp.Suppress("\n")[0, 1]
CLOSE_TAG = DOUBLE_LBRACE + pp.Literal("/") + VARIABLE + DOUBLE_RBRACE

literal = Rule("Others", pp.Regex(r"[^{}]+") | pp.Regex(r"[{][^{}]*}"), [
    lambda tokens: [["l", tokens[0]]]
])
variable_tag = Rule("Variable", TAG)
partial_tag = Rule("Partial", DOUBLE_LBRACE + pp.Literal(">").suppress() + VARIABLE + DOUBLE_RBRACE, [
    lambda tokens: [["p", tokens[0]]]
])
token_list = Rule("TokenList", lambda parser: LBRACE + ((~pp.Suppress("{") + parser) | TAG) + RBRACE, [
    lambda tokens: [["l", "{"], *tokens, ["l", "}"]]
])
block = Rule("Block", lambda parser: OPEN_TAG + parser + CLOSE_TAG.suppress(), [
    lambda tokens: [[[tokens[0], tokens[2]], [tokens[1], *tokens[3:]]]]
])


class Parser(object):
    rules = [block, token_list, partial_tag, variable_tag, literal]

    def __init__(self):
        self.tokenizer = pp.Forward().setName("Tokenizer")
        _rules = [r(self.tokenizer) for r in self.rules]
        self.tokenizer <<= pp.MatchFirst(_rules)[...].leaveWhitespace()

    def __call__(self, template: str) -> list:
        return self.tokenizer.parseString(template)

    def use(self, rule: Rule):
        self.rules.append(rule)
        self.tokenizer = pp.Forward().setName("Tokenizer")
        _rules = [r(self.tokenizer) for r in self.rules]
        self.tokenizer <<= pp.MatchFirst(_rules)[...].leaveWhitespace()
        return self


parse = Parser()
