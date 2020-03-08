# -*- encoding: utf-8 -*-
"""
@File: main.py
@Time: 2020/03/08 23:55:27
@Author: Virace
@WebSite: virace.cc
@Version: 0.0.1
"""

# here put the import lib
import re
import argparse
import requests

API = 'http://steamworkshop.download/online/steamonline.php'


def get_one(url):
    try:
        _id = re.compile(r'id=(\d+)').findall(url)[0]
    except IndexError:
        pass
    else:
        res = requests.post(API, data={"item": _id, "app": 294100},
                            headers={"Content-Type": "application/x-www-form-urlencoded"})
        res.raise_for_status()
        regx = re.compile(r"(https|http?://[^\s]+)'").findall(res.text)
        if len(regx) > 0:
            return regx[0]


# print(get_one('https://steamcommunity.com/sharedfiles/filedetails/?id=1201382956'))
parser = argparse.ArgumentParser(description="Batch download for the Steam Workshop.")
parser.add_argument('file')
cli_args = parser.parse_args()
if cli_args.file.find('https://steamcommunity.com/') != -1:
    # 地址
    print(get_one(cli_args.file))
else:
    # 文件
    with open(cli_args.file, encoding='utf-8') as file:
        urls = file.read().split('\n')
        for item in urls:
            print(get_one(item))

print('Done.')
