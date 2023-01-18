import sys
import execjs

sys.path.append('../')
from common import match_run

with open('base.js', 'r', encoding='utf-8') as fp:
    js = fp.read()
jsx = execjs.compile(js)


def get_hexin():
    """还没有实现这里"""
    return jsx.call("")


# 这个题用jsdom可以做出来 但是我不想用jsdom  所以直接贴了一个固定值 后面补环境学完了会重新来弄这里
value = 0

for page in range(1, 101):
    value += match_run(6, other_headers={"hexin-v": get_hexin()}, page=page)

print(f"最终结果是: {value}")

# match_run(6, other_headers={"hexin-v": "AwxFPk7mgFXNsZfkSCyDkns43WE7RbDvsunEs2bNGLda8aJfjlWAfwL5lEG1"})  # 投机取巧的
