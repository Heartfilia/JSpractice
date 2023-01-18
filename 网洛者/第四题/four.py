import sys
import execjs
from lite_tools import get_time
sys.path.append('../')
from common import match_run

with open('base.js', 'r', encoding='utf-8') as fp:
    js = fp.read()
jsx = execjs.compile(js)


def cal_js():
    key = f"{get_time()}000"
    new_tl = jsx.call("aes", key)
    return new_tl


match_run(4, cal_js)
