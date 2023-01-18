import os

from collections.abc import Callable

import requests
from loguru import logger
from lite_tools import get_ua, try_get


root = os.path.dirname(__file__)


def match_run(timu: int, cal_js: Callable = None, other_headers: dict = None):
    value = 0
    for i in range(1, 101):
        url = f'http://spider.wangluozhe.com/challenge/api/{timu}'
        payload = {"page": i, "count": 10}
        if cal_js is not None:
            sign = cal_js()
            payload.update({"_signature": sign})
        base_headers = {
            "user-agent": get_ua(),
            "Cookie": f'session={try_get(os.path.join(root, "config.json"), "session", options={"mode": "file"})}',
            "Host": "spider.wangluozhe.com",
            "Origin": "http://spider.wangluozhe.com",
            "Referer": f"http://spider.wangluozhe.com/challenge/{timu}"
        }
        if other_headers:
            for header_key, header_value in other_headers.items():
                if header_key in base_headers:  # 这变动只会出现在cookie部分
                    origin_value = base_headers[header_key]
                    base_headers[header_key] = origin_value + f"; {header_value}"
                else:
                    base_headers[header_key] = header_value
        resp = requests.post(
            url, 
            data=payload, 
            headers=base_headers
        )
        data = resp.json()
        if not data:
            break
        logger.debug(f"题目:[{timu}] 页码:[{i:>2}] 结果:{data}")
        for item in data['data']:
            value += item['value']

    logger.success(f"计算结果是: {value}")
