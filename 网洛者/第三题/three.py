import sys
import execjs
from lite_tools import get_time
sys.path.append('../')
from common import match_run

with open('base.js', 'r', encoding='utf-8') as fp:
    js = fp.read()
jsx = execjs.compile(js)


def cal_js():
    message = f"http://spider.wangluozhe.com/challenge/3|{get_time()}000"
    key = f"{get_time()}000"
    new_tl = jsx.call("encryptByDES", message, key)
    return new_tl


match_run(3, cal_js)
