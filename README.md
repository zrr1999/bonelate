# Bonelate

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Bonelate 是一个基于 pyparsing 针对 LaTeX 的类似 mustache 语言的模版渲染器。 与采取 mustache 的其他模板渲染器相比（例如chevron或pymustache）， Bonelate 针对 LaTeX 的语法做了很多优化，使模板文件在不渲染的情况下也可使用 LaTeX 工具编译通过。同时Bonelate的实现极为简短，Tokenizer 类仅有 23 行，Renderer 类仅有51行。

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

如果你的环境变量中有 python 脚本目录，你可以使用

```bash
$ bonelate render .\examples\ml_work\bonework.tex .\examples\ml_work\data.json
```

如果没有的话，你需要使用如下命令

```bash
$ python bonelate render .\examples\ml_work\bonework.tex .\examples\ml_work\data.json
```



## 更新日志

0.0.2 (2021.4.29)

1. 不再兼容mustache语法。
2. 增加了命令行指令。
3. 增加了更多例子。
4. 添加了单元测试（不完全）。
5. 修复了大括号内的内容不能正常解析的问题。
6. 修复了模板变量中含有空白符不能正常解析的问题。

## 维护者

[@六个骨头](https://gitee.com/zrr1999)

## 如何贡献

非常欢迎你的加入！[提一个 Issue](https://github.com/zrr1999/bonelate/issues/new) 或者提交一个 Pull Request。

### 贡献者

感谢以下参与项目的人：

## 使用许可
[MIT](LICENSE) © Rongrui Zhan