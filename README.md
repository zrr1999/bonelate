# Bonelate

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Bonelate 是一个针对 LaTeX 的轻逻辑模版解析引擎，类似于 mustache。
与采取 mustache 的其他模版解析引擎相比（例如chevron或pymustache），
Bonelate 针对 LaTeX 的语法做了很多优化，使 LaTeX 模板文件在不渲染的情况下也可使用 LaTeX 工具编译通过。

## 背景

Bonelate 是从 BoneTeX 模板块分离出来的项目，可以独立使用。

## 优势

Bonelate 是参考 mustache 且针对 LaTeX 的语法微调了标记符，
原本的`{{#partial}}`改为`{{!partial}}`，从而在不渲染的情况下 LaTeX 编译时也不会报错。
通过 Bonelate，用户可以很方便的将现有 LaTeX 项目渐进地转换为 BoneTeX 项目。

## 安装 [![Downloads](https://pepy.tech/badge/bonelate)](https://pepy.tech/project/bonelate)

这个项目使用 [Python](https://www.python.org/downloads/) 开发，请确保你本地安装了它。

使用PyPI安装

```sh
$ pip install bonelate[all]
```

源码安装

```sh
$ git clone git@gitee.com:zrr1999/bonelate.git
$ cd bonelate
$ pip install .
```

## 使用说明
### 支持语法
1. 模板变量渲染 `{{keyName}}`
2. 模板块渲染 `{{!keyName}}sth.{{/keyName}}`
以!开始、以/结束表示模板块，它会根据当前上下文中的键值来对区块进行一次或多次渲染。
它的功能很强大，有类似if、foreach的功能。
3. 失效渲染`{{?keyName}} {{/keyName}}`
该语法与模板块渲染类似，不同在于它是当keyName值为空或否定值时才渲染输出该区块内容。
3. 视图渲染 `{{.}}`
可以循环输出整个数组。

### 简单示例

运行如下代码
```python
from bonelate import render, parse

test_string = r"\LaTeX{} is a {{var}} typesetting system.{{!vars}}.{{/vars}}"
print(render(test_string, {
    "var": "high-quality",
    "vars": list(range(10)),
}))
```

得到渲染结果
```tex
\LaTeX{} is a high-quality typesetting system...........
```


### 命令行示例

如果你的环境变量中有 python 脚本目录，你可以使用

```sh
$ bonelate render ./examples/ml_work/bonework.tex ./examples/ml_work/data.json
```

如果没有的话，你需要使用如下命令

```sh
$ python bonelate render ./examples/ml_work/bonework.tex ./examples/ml_work/data.json
```


## 更新日志
#### 0.1.0 (2021.5.2)
1. 重构 tokenizer，现在命名为parser。
2. 增加了 partial 语法。
3. 增加了 docs 目录。
4. 增加了更多例子。
5. 修改了单元测试。

#### 0.0.2 (2021.4.29)
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