import os

from collections.abc import Callable

import requests
from loguru import logger
from lite_tools import get_ua, try_get


root = os.path.dirname(__file__)  # 需要在 common.py 同级目录创建一个 config.json 配置文件 内容是 {"cookie": "你的页面cookie"}


def __each_page(challenge: int, cal_js: Callable = None, other_headers: dict = None, page: int = 1) -> int:
    url = f'http://spider.wangluozhe.com/challenge/api/{challenge}'
    payload = {"page": page, "count": 10}
    if cal_js is not None:
        sign = cal_js()
        payload.update({"_signature": sign})
    base_headers = {
        "user-agent": get_ua(),
        "Cookie": try_get(os.path.join(root, "config.json"), "cookie", options={"mode": "file"}),
        "Host": "spider.wangluozhe.com",
        "Origin": "http://spider.wangluozhe.com",
        "Referer": f"http://spider.wangluozhe.com/challenge/{challenge}"
    }
    if other_headers:
        for header_key, header_value in other_headers.items():
            if header_key in base_headers:  # 这变动只会出现在cookie部分 在原cookie后面追加字符串cookie
                base_headers[header_key] += f"; {header_value}"
            else:
                base_headers[header_key] = header_value
    resp = requests.post(
        url,
        data=payload,
        headers=base_headers
    )
    data = resp.json()
    if not data:
        return 0
    logger.debug(f"题目:[{challenge}] 页码:[{page:>2}] 结果:{data}")
    value = 0
    for item in data['data']:
        value += item['value']
    return value


def match_run(challenge: int, cal_js: Callable = None, other_headers: dict = None, page: int = None):
    value = 0
    if page:
        value = __each_page(challenge, cal_js, other_headers, page)   # 指定页码
        logger.success(f"第[{page}]页单独 计算结果是: {value}")
        return value

    for page in range(1, 101):
        value += __each_page(challenge, cal_js, other_headers, page)  # 不指定页码会翻全部页码并统计

    logger.success(f"计算结果是: {value}")
