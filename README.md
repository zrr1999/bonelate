# Bonelate

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Bonelate 是一个针对 LaTeX 的轻逻辑模版解析引擎，类似于 mustache。
与采取 mustache 的其他模版解析引擎相比（例如chevron或pymustache），
Bonelate 针对 LaTeX 的语法做了很多优化，使 LaTeX 模板文件在不渲染的情况下也可使用 LaTeX 工具编译通过。

## 优势

Bonelate 针对 LaTeX 的语法设计了模板标记符，
使用 LaTeX 中非特殊字符作为标记符，例如`{{!partial}}`中的`!`，
从而在不解析渲染的情况下直接通过 LaTeX 引擎编译也不会报错。

## 安装 [![Downloads](https://pepy.tech/badge/bonelate)](https://pepy.tech/project/bonelate)

这个项目使用 [Python](https://www.python.org/downloads/) 开发，请确保你本地安装了它。

使用PyPI安装

```shell
$ pip install bonelate[all]
```

源码安装

```shell
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
    "vars": range(10),
}))
```

得到渲染结果
```latex
\LaTeX{} is a high-quality typesetting system...........
```


### 命令行示例

如果你的环境变量中有 python 脚本目录，你可以使用

```shell
$ bonelate render ./examples/ml_work
```

如果没有的话，你需要使用如下命令

```shell
$ python bonelate render ./examples/ml_work
```

## 更新日志

#### 0.1.2 (2021.5.14)

1. 优化了插件接口。
2. 修复了无法解析嵌套模板的问题。
3. 修改了render指令用法

#### 0.1.1 (2021.5.5)
1. 完善了README中的用法描述。
2. 增加了分隔符特性，{{var:sep}}。
3. 遍历渲染改为判断对象是否为Iterable。
4. 添加了用于处理Sympy公式的插件。
5. 修复部分bug。

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