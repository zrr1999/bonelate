#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/4/28 19:13
# @Author : 詹荣瑞
# @File : __main__.py
# @desc : 本代码未经授权禁止商用
import typer
import json
import os
import bonelate

app = typer.Typer()


@app.command()
def render(source_path: str, data_path: str, target_path: str = None, yaml: bool = False):
    if target_path is None:
        (dir_path, name) = os.path.split(source_path)
        target_path = f"{dir_path}/rendered_{name}"
        print(target_path)
    with open(data_path, encoding="utf-8") as file:
        data = json.load(file)
    with open(source_path, encoding="utf-8") as file:
        test_string = file.read()
    with open(target_path, mode="w", encoding="utf-8") as file:
        file.write(bonelate.render(test_string, data))


@app.command()
def keep():
    pass


if __name__ == '__main__':
    app()
