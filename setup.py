#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/3/18 21:43
# @Author : 詹荣瑞
# @File : setup.py
# @desc : 本代码未经授权禁止商用
import bonetex
from setuptools import setup, find_packages

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()
extras = {}
setup(
    name="Bonelate",
    version=bonetex.__version__,
    author="六个骨头",
    author_email="2742392377@qq.com",
    description="Bonelate 是一个基于 pyparsing 针对 LaTeX 的 mustache 模版语言的实现。",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/zrr1999/bonetex",
    # 你要安装的包，通过 setuptools.find_packages 找到当前目录下有哪些包
    packages=find_packages(),
    package_data={
        '': ['*.txt'],
        # 包含demo包data文件夹中的 *.dat文件
        'demo': ['data/*.dat'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    platforms="any",
    install_requires=["pyparsing"],
    extras_require=extras,
    entry_points={
        'console_scripts': [
            'bonetex=bonetex:main',
        ]
    }
)
