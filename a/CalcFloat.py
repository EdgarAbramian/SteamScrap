import logging
import time
from random import randint
import socket

import requests
from urllib3 import HTTPSConnectionPool
import urllib3
from my_config import prox_list
from fake_useragent import UserAgent
from datetime import datetime

ua = UserAgent()

headers = {
    'Cookie': 'i18n_redirected=en; vuex={%22inventory%22:{%22siteInventory%22:{%22filters%22:{%22gameId%22:730}}%2C%22userInventory%22:{%22filters%22:{}}}%2C%22users%22:{%22analyticsAttributes%22:null}}; _ga=GA1.1.1050277151.1694977285; ga4={"client_id":"1050277151.1694977285"}; _scid=cc249994-ac40-4279-8b00-6eaf6d86b91e; _ym_uid=1694977288429233305; _ym_d=1694977288; _tt_enable_cookie=1; _ttp=W3TGJyZYNcA3TL8ABhPfYDw8mlH; _ym_isad=2; _fbp=fb.1.1694977290079.1377110986; _sctr=1%7C1694894400000; USER_DATA=%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%22510c9c83-22c6-45b4-b630-185855119d79%22%2C%22deviceAdded%22%3Afalse%7D; moe_uuid=510c9c83-22c6-45b4-b630-185855119d79; OPT_IN_SHOWN_TIME=1694977442962; SOFT_ASK_STATUS=%7B%22actualValue%22%3A%22dismissed%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D; sessionid=s%3AzdOSlstDs-aHbuZtCtW33yuaLMOLgd1Y.ksHD3uoPPyMobdd%2Fh%2FpFzwWMsblgRG4pV2x6LhFtZ1E; _scid_r=cc249994-ac40-4279-8b00-6eaf6d86b91e; _ga_RFHNPQTN51=GS1.1.1694977284.1.1.1694978231.52.0.0',
    'User-Agent': ua.random,
}

float_cheacker = 'https://tradeit.gg/api/steam/v1/steams/float-item-finder'

logging.basicConfig(level=logging.INFO, filename="dep_log.log", filemode="a")

s = requests.Session()
s.proxies.update(prox_list[randint(0, len(prox_list) - 1)])


def get_float(inspectLink):
    payload = {'inspectLink': inspectLink}
    try:
        get_float = s.get(url=float_cheacker, params=payload, headers=headers).json()
    except:
        s.proxies.update(prox_list[randint(0, len(prox_list))])
        get_float = s.get(url=float_cheacker, params=payload, headers=headers).json()

    return get_float['paintwear']


# with open('proxy.txt','r') as proxy:
#     proxys = proxy.read()
#     for proxy in proxys.split(';'):
#         print('{"https":'+'"'+f'http://{proxy.split(":")[2]}:{proxy.split(":")[3]}@{proxy.split(":")[0]}:{proxy.split(":")[1]}/'+'"'+'},')

#
# import json
#
# _all_cookies_ = {}
# with open('request.json') as f:
#     data = json.load(f)
# for i in (str(data['cookies']).split(';')):
#     _all_cookies_.update({i.split('=')[0]: i.split('=')[1]})
# _all_cookies_.update({"User-Agent": data['User-Agent']})
# print(_all_cookies_["User-Agent"])
#
#

import requests

r = requests.Session()
wrong_proxy = True
pr = [
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.t76.227.22:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.193.160.58:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.t76.227.22:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.t76.227.22:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.t76.227.22:30013/"},
]
# while wrong_proxy:
#     try:
#             r.proxies.update(pr[randint(0,len(pr)-1)])
#             wrong_proxy = False
#     except requests.exceptions.ProxyError:
#             print('requests.exceptions.ProxyError')


import re


def get_price(price_code):
    f = ''
    mas = re.findall(r'\d+', price_code)
    for i in mas:
        f += i

    return f


print(get_price('\r\n\t\t\t\t\t\t14,97₴\t\t\t\t\t'))
# print(float(f + i for i in re.findall(r'\d+', '\r\n\t\t\t\t\t\t16₴\t\t\t\t\t'))
