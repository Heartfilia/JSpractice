import sys
import execjs
from lite_tools import get_time
sys.path.append('../')
from common import match_run

with open('base.js', 'r', encoding='utf-8') as fp:
    js = fp.read()
jsx = execjs.compile(js)


def IIl111li(t: str):
    a = []
    for ind in range(0, 104, 8):
        if len(a) < ((ind >> 5) + 1):
            a.append(0)
        a[ind >> 5] |= (ord(str(int(t[ind//8]) & 255)) << ind % 32)
    return a


def lIIiiI1l(item_list: list):
    base_string = "0123456789abcdef"
    string = ""
    for ind in range(len(item_list) * 4):
        string += base_string[item_list[ind >> 2] >> ind % 4 * 8 + 4 & 15] + base_string[item_list[ind >> 2] >> ind % 4 * 8 & 15]
    return string


def cal_js():
    t = str(get_time()) + "000"
    tl = IIl111li(t)

    new_tl = jsx.call("iIIiIlli", tl)
    code = lIIiiI1l(new_tl)
    return code


match_run(1, cal_js)
