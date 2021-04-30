#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/4/27 19:45
# @Author : 詹荣瑞
# @File : test_bonelate.py
# @desc : 本代码未经授权禁止商用
import pytest
import yaml
import bonelate


class TestBonelate(object):

    @staticmethod
    def _test_yaml(path: str):
        with open(path) as file:
            tests = yaml.load(file, Loader=yaml.FullLoader)['tests']
        # for test in tests:
        #     context = test['data']
        #     if 'lambda' in context:
        #         context['lambda'] = eval(context['lambda']['python'])
        for test in tests:
            context = test['data']
            template = test['template']
            expected = test['expected']
            # partials = test['partials'] if 'partials' in test else {}
            result = bonelate.render(template, context)
            assert result == expected

    def test_interpolation(self):
        self._test_yaml("./specs/interpolation.yml")

    def test_inverted(self):
        self._test_yaml("./specs/inverted.yml")


if __name__ == '__main__':
    with open("./specs/interpolation.yml") as file:
        tests = yaml.load(file, Loader=yaml.FullLoader)['tests']
    for test in tests:
        context = test['data']
        template = test['template']
        expected = test['expected']
        print(template, context)
        print("->")
        print(expected)
