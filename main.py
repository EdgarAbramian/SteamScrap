import re
import time
import random
import logging
import requests
import concurrent.futures
from random import randint
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_exponential
import json


def set_proxy():
    wrong_proxy = True
    while wrong_proxy:
        try:
            s.proxies.update(prox_list[randint(0, len(prox_list) - 1)])
            wrong_proxy = False
        except requests.exceptions.ProxyError:
            logging.info('requests.exceptions.ProxyError')


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("steam_log.log"),
        logging.StreamHandler()
    ],
)

_all_cookies_ = {}
_all_items_ = {}
with open('request.json') as f:
    _cookies_data = json.load(f)
for i in (str(_cookies_data['cookies']).split(';')):
    _all_cookies_.update({i.split('=')[0].replace(' ', ''): i.split('=')[1]})
_all_cookies_.update({"User-Agent": _cookies_data['User-Agent']})

logging.basicConfig(level=logging.INFO, filename="steam_log.log", filemode="a")
prox_list = [

    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.176.227.22:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.176.220.148:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.176.227.236:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.176.220.136:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.176.220.181:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.176.227.112:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.176.227.11:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.176.227.169:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.176.227.142:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.176.227.28:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.176.220.168:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.176.227.8:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.176.227.105:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.176.220.166:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.176.220.129:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.176.220.6:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.176.220.164:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.176.220.21:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.176.220.86:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.176.227.90:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.193.160.125:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.193.160.94:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.193.160.190:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.193.160.122:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.193.160.58:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.193.160.149:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.193.160.211:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.193.160.64:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.193.160.212:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.193.160.40:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.193.160.91:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.193.160.134:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.193.160.179:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.193.160.201:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.193.160.158:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.193.160.188:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.193.160.9:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.193.160.90:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.193.160.97:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.193.160.235:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.36.228.173:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.36.228.105:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.36.228.110:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.36.228.21:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.36.228.136:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.36.228.190:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.36.228.96:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.36.228.161:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.36.228.162:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.36.228.84:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.36.228.32:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.36.228.26:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.36.228.74:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.36.228.208:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.36.228.169:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.36.228.131:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.36.228.64:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.36.228.36:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.36.228.12:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.36.228.153:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@45.67.121.5:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@45.67.120.134:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@45.67.122.169:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@45.67.121.81:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@45.67.122.3:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@45.67.121.60:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@45.67.123.127:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@45.67.122.44:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@45.67.121.70:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@45.67.120.136:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@45.67.122.107:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@45.67.122.225:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@45.67.121.129:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@45.67.121.65:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@45.67.123.242:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@45.67.120.48:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@45.67.123.7:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@45.67.120.112:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@45.67.121.202:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@45.67.121.133:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.37.51.77:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.37.51.241:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.37.48.182:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.37.48.230:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.37.48.81:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.37.50.186:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.37.50.65:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.37.49.34:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.37.50.221:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.37.51.107:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.37.50.219:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.37.48.243:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.37.48.138:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.37.48.49:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.37.49.72:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.37.50.234:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.37.51.181:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.37.50.216:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.37.50.35:30013/"},
    {"https": "http://edikaraslanov_gmail_com:4bc4ca9131@193.37.49.57:30013/"},
]
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


def set_buy_headers(listing_id, refer_link) -> dict:
    return {
        'POST': f'/market/buylisting/{listing_id} HTTP/1.1',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',  # str(dfheaders['Accept-Encoding'][0])
        'Accept-Language': 'ru,en;q=0.9',  # str(dfheaders['Accept-Language'][0]),
        'Connection': 'keep-alive',  # str(dfheaders['Connection'][0]),
        'Content-Length': '117',  # str(dfheaders['Content-Length'][0]),
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',  # str(dfheaders['Content-Type'][0]),
        'Cookie': str(_cookies_data['cookies']),
        'Host': 'steamcommunity.com',
        'Referer': refer_link,
        'User-Agent': str(_all_cookies_['User-Agent'])
    }


def set_buy_payload(subtotal, fee, total) -> dict: return {
    'sessionid': str(_all_cookies_['sessionid']),
    'currency': '18',
    'subtotal': str(int(subtotal)),
    'fee': str(int(fee)),
    'total': str(int(total)),
    'quantity': '1',
    'billing_state': '',
    'save_my_address': '0'
}


def cookies() -> dict:
    return {
        'timezoneOffset': str(_all_cookies_['timezoneOffset']),
        'browserid': str(_all_cookies_['browserid']),
        'sessionid': str(_all_cookies_['sessionid']),
        'steamLoginSecure': str(_all_cookies_['steamLoginSecure']),
        'Steam_Language': 'english',  # str(dfheaders['Steam_Language'][0])
    }


base_market_url = 'https://steamcommunity.com/market/search?q='

page_url = '/render/?query=&start=0&count=50&country=RU&language=english&currency=18&format=json'

float_cheacker = 'https://tradeit.gg/api/steam/v1/steams/float-item-finder'

payload = {
    'query': '',
    'start': '1',
    'count': 50,
    'country': 'RU',
    'language': 'english',
    'currency': '18'
}

headers = {
    'User-agent': ua[random.randint(0, len(ua) - 1)]
}

s = requests.Session()

set_proxy()


def get_price(price_code):
    f = ''
    mas = re.findall(r'\d+', price_code)
    for i in mas:
        f += i

    return int(f)


@retry(
    stop=stop_after_attempt(10),  # Maximum number of retries
    wait=wait_exponential(multiplier=1, min=1, max=60)  # Exponential backoff
)
def get_float(inspectLink):
    isfl = True
    start = time.time()
    try:
        set_proxy()
        float_payload = {'inspectLink': inspectLink}

        while isfl:
            try:
                get_float_resp = s.get(url=float_cheacker, params=float_payload, headers=headers).json()
                isfl = False
            except:
                time.sleep(1.5)
                set_proxy()
                # get_float_resp = s.get(url=float_cheacker, params=float_payload, headers=headers).json()

        return get_float_resp['paintwear']
    except:
        logging.info(f'GET_FLOAT ERROR{s.proxies} link: {inspectLink}')


def exchanger(items):
    for i in items['listinginfo']:
        print(items['listinginfo'][i]['listingid'], items['listinginfo'][i]['price'])


def item_search(itemname, link_to_item, maxprice, minfloat):
    run = True
    logging.info(f'{itemname} is STARTED')

    while run:
        logging.info(f'\nBOT IS SEARCHING item: {itemname}')
        set_proxy()

        try:
            items1 = s.get(url=link_to_item + page_url, params=payload)
        except requests.exceptions.ProxyError:
            set_proxy()
            items1 = s.get(url=link_to_item + page_url, params=payload)

        soup = BeautifulSoup(str(items1.json()['results_html']), 'lxml')

        items = items1.json()

        for i in items['listinginfo']:
            try:
                try:
                    price_code = (soup.find("div", id=f'listing_{i}', ).find('span', {
                        'class': "market_listing_price market_listing_price_with_fee"})).text.replace(',', '.')

                    subtotal_code = (soup.find("div", id=f'listing_{i}', ).find('span', {
                        'class': "market_listing_price market_listing_price_without_fee"})).text.replace(',', '.')

                except:
                    price_code = (soup.find("div", id=f'listing_{i}', ).find('span', {
                        'class': "market_listing_price market_listing_price_with_fee"})).text.replace(',', '.')

                    subtotal_code = (soup.find("div", id=f'listing_{i}', ).find('span', {
                        'class': "market_listing_price market_listing_price_without_fee"})).text.replace(',', '.')
                    logging.info(f'PRICE SCRAPPING ERROR{i}')
                try:
                    price = get_price(price_code)
                    subtotal = get_price(subtotal_code)
                    fee = price - subtotal

                except:
                    logging.info(f'PRICE EXCH ERROR {i} price-code = {price_code} subtotal: {subtotal}')

                print(price)
                if float(price / 100) <= maxprice:

                    set_proxy()
                    try:
                        listingid = items['listinginfo'][i]
                        assetid = listingid['asset']['id']
                        item_base_link = str(listingid['asset']['market_actions'][0]['link']).replace('%listingid%',
                                                                                                      str(i)).replace(
                            '%assetid%', str(assetid))
                    except:
                        logging.info(f'GET INFO FROM JSON ERROR listingid assetid')

                    try:
                        item_float = get_float(item_base_link)
                    except:
                        set_proxy()
                        item_float = get_float(item_base_link)

                    buymess = None
                    c = {
                        'timezoneOffset	': '14400,0',
                        'browserid': str(_all_cookies_['browserid']),
                        'Steam_Language': 'english',
                        'strInventoryLastContext': '730_2',
                        'steamLoginSecure': str(_all_cookies_['steamLoginSecure']),
                        'recentlyVisitedAppHubs': '730',
                        'sessionid': str(_all_cookies_['sessionid']),
                        'webTradeEligibility': str(_all_cookies_['webTradeEligibility']),
                        'app_impressions': '730@2_9_100006_100202'

                    }

                    if item_float <= minfloat:
                        try:

                            buy = s.post(f'https://steamcommunity.com/market/buylisting/{i}',
                                         data=set_buy_payload(subtotal, fee, price),
                                         headers=set_buy_headers(i, link_to_item),
                                         cookies=c)  # set_buy_headers(i, link_to_item)

                            if int(buy.json()["wallet_info"]["success"]) == 1:
                                logging.info(
                                    f'BUY>>> item: {itemname}\nid: {i}\nfloat : {item_float}\nprice: {price / 100}\n{buy.content} ')

                                time.sleep(1)
                            else:
                                logging.info(
                                    f'UNABLE TO BUY>>> item: {itemname}\nid: {i}\n{buy.content}')
                        except:
                            logging.info(
                                f'UNABLE TO BUY>>> item: {itemname}\nid: {i}\n{buymess}')
                else:
                    break
            except:
                logging.info(f'ID ERROR ID = {i}')
        time.sleep(10)


def get_url_to_item(itemname, session):
    itempayload = {'q': itemname, }
    try:
        try:
            resp = session.get(url=base_market_url + itemname.replace(' ', '+'), params=itempayload, cookies=cookies())
            soup = BeautifulSoup(resp.text, 'lxml')
            link_item = soup.find('a', class_='market_listing_row_link', id="resultlink_0").get('href')
        except:
            set_proxy()
            resp = session.get(url=base_market_url + itemname.replace(' ', '+'), params=itempayload, cookies=cookies())
            soup = BeautifulSoup(resp.text, 'lxml')
            link_item = soup.find('a', class_='market_listing_row_link', id="resultlink_0").get('href')
    except:
        logging.info(f'{itemname}: URL IS NOT FOUND')

    logging.info(f'resp.url: {resp.url} link: {link_item} Proxy: {session.proxies}')

    return link_item


with open('items.json') as f:
    _items_data = json.load(f)
for i in _items_data:
    _items_data[i]['link'] = get_url_to_item(_items_data[i]['name'], s)
logging.info(f'ITEMS>>> item: {_items_data}\n')

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for id_item in _items_data:
        if (str(_items_data[id_item]['price']).replace('.', '').isdecimal() and (_items_data[id_item]['float']).replace(
                '.', '').isdecimal()):
            futures.append(
                executor.submit(item_search, itemname=_items_data[id_item]['name'],
                                link_to_item=_items_data[id_item]['link'],
                                maxprice=float(_items_data[id_item]['price']),
                                minfloat=float(_items_data[id_item]['float'])))
        else:
            logging.info(f"INCORRECT INPUT {_items_data[id_item]['name']}")
    for future in concurrent.futures.as_completed(futures):
        future.result()
