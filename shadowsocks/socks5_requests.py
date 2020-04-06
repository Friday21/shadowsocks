#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
"""
pip install pysocks
"""

URL = 'https://www.baidu.com/'


def socks5_request():
    resp = requests.get(URL, proxies={'http': 'socks5://127.0.0.1:1088', 'https': 'socks5://127.0.0.1:1088'})
    print(resp.status_code)


if __name__ == '__main__':
    socks5_request()
