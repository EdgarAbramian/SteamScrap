import logging
import time
from random import randint
import socket

import aiohttp
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
#         try:
#             print('{"https":'+'"'+f'http://{proxy.split(":")[2]}:{proxy.split(":")[3]}@{proxy.split(":")[0]}:{proxy.split(":")[1]}/'+'"'+'},')
#         except:
#             pass
# #
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


# while wrong_proxy:
#     try:
#             r.proxies.update(pr[randint(0,len(pr)-1)])
#             wrong_proxy = False
#     except requests.exceptions.ProxyError:
#             print('requests.exceptions.ProxyError')


import random
from requests.auth import HTTPProxyAuth
ua = [
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5666.197 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 OPR/99.0.0.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5666.197 Safari/537.36'
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'

]

headers = {
    'User-agent': ua[random.randint(0, len(ua) - 1)],
    'Referer':'https://csfloat.com/'
}

session = requests.Session()




link = 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20M4374741056448178759A32955593566D7849392219500181207'
h = {'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
     'Referer':'https://csfloat.com/'}
print(session.get(f'https://api.csfloat.com/?url='+link,
                  headers=headers).json())




























