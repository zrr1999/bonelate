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
def render(source_dir: str, target_path: str = None, yaml: bool = False):
    if target_path is None:
        target_path = f"{source_dir}/rendered.tex"
        print(target_path)
    with open(f"{source_dir}/template.tex", encoding="utf-8") as file:
        test_string = file.read()
    with open(f"{source_dir}/data.json", encoding="utf-8") as file:
        data = json.load(file)
    with open(target_path, mode="w", encoding="utf-8") as file:
        file.write(bonelate.render(test_string, data))


@app.command()
def watch():
    pass


if __name__ == '__main__':
    app()
