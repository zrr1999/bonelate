# Bonelate

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Bonelate 是一个基于 pyparsing 针对 LaTeX 的类似 [mustache](http://mustache.github.io/) 语言的模版渲染器。
与采取 mustache 的其他模板渲染器相比（例如[chevron](https://github.com/noahmorrison/chevron)或[pymustache](https://github.com/lotabout/pymustache)），
Bonelate 针对 LaTeX 的语法做了很多优化，使模板文件在不渲染的情况下也可使用 LaTeX 工具编译通过。
且实现更为简短，Tokenizer 类仅有 23 行，Renderer 类仅有51行。
minibonelate.py中是单文件实现，仅有59行。

## 背景

Bonelate 是从 BoneTeX 模板块分离出来的项目，可以独立使用。

## 优势

Bonelate 是参考 mustache 且针对 LaTeX 的语法微调了标记符，
原本的`{{#partial}}`改为`{{!partial}}`，从而在不渲染的情况下 LaTeX 编译时也不会报错。
通过 Bonelate，用户可以很方便的将现有 LaTeX 项目渐进地转换为 BoneTeX 项目。

## 安装[![Downloads](https://pepy.tech/badge/bonelate)](https://pepy.tech/project/bonelate)

这个项目使用 [Python](https://www.python.org/downloads/) 开发，请确保你本地安装了它。

使用PyPI安装

```sh
$ pip install bonelate
```

源码安装

```sh
$ git clone git@github.com:zrr1999/bonelate.git
$ cd bonelate
$ pip install .
```

## 使用说明

### 简单示例

```python
from bonelate import render


test_string = """
        {{!persons}}{{name}} is awesome.{{/persons}}
        {{person}} is beautiful.
        {{!is_person}}{{.}} is a person.{{/is_person}}
        """
print(render(test_string, {
    "persons": [{"name": "Xiao Ming"}, {"name": "Yuan Long"}],
    "person": "Xiao Ming",
    "is_person": "Xiao Ming",
    "not_person": False
}))


```

### 命令行示例

```bash
$ python .\command.py render .\examples\ml_work\bonework.tex .\examples\ml_work\data.json
```



## 更新日志

0.0.2 (2021.4.27)



## 维护者

[@六个骨头](https://gitee.com/zrr1999)

## 如何贡献

非常欢迎你的加入！[提一个 Issue](https://github.com/zrr1999/bonelate/issues/new) 或者提交一个 Pull Request。

### 贡献者

感谢以下参与项目的人：

## 使用许可
[MIT](LICENSE) © Rongrui Zhan