import pyparsing as pp
from typing import Union

parser = pp.Forward()
left = pp.Suppress("{{")
right = pp.Suppress("}}")
variable = pp.Regex(r"[._A-Za-z0-9\u4e00-\u9fa5]+")  # 包含数字、字母、下划线、小数点或汉字的变量
tag = (left + variable + right).addParseAction(
    lambda tokens: [["v", tokens[0]]]
)
open_tag = left + pp.oneOf(["#", "!#"]) + variable + right
close_tag = left + "/" + variable + right
literal = (pp.Regex(r"[^{}]+") | pp.Regex(r"[{][^{}]}")).addParseAction(
    lambda tokens: [["l", tokens[0]]]
)
block = (open_tag + parser + close_tag.suppress()).addParseAction(
    lambda tokens: [[tokens[0], tokens[1:]]]
)
parser <<= (block | tag | literal)[...].leaveWhitespace()


def render(template: Union[str, list], data: dict) -> str:
    output = ""
    scopes = [data]
    if isinstance(template, str):
        template = parser.parseString(template)
    for flag, value in template:
        if flag == "l":
            output += value
        else:
            scope = scopes[-1]
            if flag == "v":
                if value == ".":
                    output += str(scope)
                else:
                    values = value.split(".")
                    for v in values:
                        if v in scope:
                            scope = scope[v]
                    output += str(scope)
            elif flag == "#":
                name, contents = value[0], value[1:]
                if name in scope:
                    scope = scope[name]
                    if isinstance(scope, list):
                        for s in scope:
                            scopes.append(s)
                            output += render(contents, s)
                            scopes.pop()
                    else:
                        scopes.append(scope)
                        output += render(contents, scope)
                        scopes.pop()
            else:  # flag == "!#"
                name, contents = value[0], value[1:]
                if name not in scope or not scope[name]:
                    output += render(contents, scope)
    return output
