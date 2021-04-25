# Bonelate

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Bonelate 是一个基于 pyparsing 针对 LaTeX 的 [mustache](http://mustache.github.io/) 模版语言变种的实现，与 [chevron](https://github.com/noahmorrison/chevron) 相比，实现更为简短，函数形式的实现仅有59行，见minibonelate.py。

## 背景

Bonelate 是从 BoneTeX 模板块分离出来的项目，可以独立使用。

## 优势

Bonelate 是兼容 mustache 的模板渲染器，且针对 LaTeX 的语法微调了标记符，例如将原本的`{{#partial}}`替换为`{{!partial}}`。通过 Bonelate，用户可以很方便的将现有 LaTeX 项目渐进地转换为 BoneTeX。

## 安装[![Downloads](https://pepy.tech/badge/bonelate)](https://pepy.tech/project/bonelate)

这个项目使用 [Python](https://www.python.org/downloads/) 开发，

建议使用pip安装本库。

```sh
$ pip install bonelate
```

## 使用说明

### 示例

```python
from bonelate import render


test_string = [
        "{{person}} is awesome.",
        "{{#persons}} awesome {{/persons}}",
        "{{#persons}}{{name}} is awesome.{{/persons}}",
        "{{!#undefined}} undefined{{/undefined}}",
        "{{!#not_person}} not_person{{/not_person}}",
        "{{!#persons}} error{{/persons}}",
        "{{!#undefined}} undefined {{person}} {{/undefined}}",
        """
        {{#persons}}{{name}} is awesome.{{/persons}}
        {{person}} is beautiful.
        {{#is_person}}{{.}} is a person.{{/is_person}}
        """,
    ]
for t in test_string:
    print(render(t, {
        "persons": [{"name": "Xiao Ming"}, {"name": "Yuan Longping"}],
        "person": "Xiao Ming",
        "is_person": "Xiao Ming",
        "not_person": False
    }))


```

## 更新日志


## 维护者

[@詹荣瑞](https://github.com/zrr1999)

## 如何贡献

非常欢迎你的加入！[提一个 Issue](https://github.com/zrr1999/bonelate/issues/new) 或者提交一个 Pull Request。

### 贡献者

感谢以下参与项目的人：

## 使用许可
[MIT](LICENSE) © Rongrui Zhan