import asyncio
import time
from datetime import datetime
from tenacity import retry, stop_after_attempt, wait_exponential
import requests
from fake_useragent import UserAgent
from random import randint
from bs4 import BeautifulSoup
import random
import re
from config import prox_list, base_market_url, cookes, buy_headers, buy_payload
import logging
import concurrent.futures

logging.basicConfig(level=logging.INFO, filename="dep_log.log", filemode="a")
ua = UserAgent()

search = ['AK-47 Азимов Прямо с завода', 'P2000 | Эконом-класс (Немного поношенное)']
page_url = '/render/?query=&start=0&count=50&country=RU&language=english&currency=18&format=json'
# cooke = {'sessionid': 'e579b88b78fbed962aeccc4e', 'timezoneOffset': '14400,0', 'Steam_Language': 'russian',
#          'steamCountry': 'RU%7C39eaabc62621425b7351fa48d901d07a', 'strResponsiveViewPrefs': 'touch'}

sessionid = 'f5b4846f421bc918f22a74c0'
test_url = 'https://steamcommunity.com/market/listings/730/StatTrak™%20P90%20%7C%20Virus%20%28Minimal%20Wear%29'

payload = {
    'query': '',
    'start': '18',
    'count': 50,
    'country': 'RU',
    'language': 'english',
    'currency': '18'
}

headers = {
    'User-agent': ua.random,
}

s = requests.Session()

s.headers.update(headers)
s.proxies.update(prox_list[random.randint(0, len(prox_list) - 1)])

float_cheacker = 'https://tradeit.gg/api/steam/v1/steams/float-item-finder'


@retry(
    stop=stop_after_attempt(10),  # Maximum number of retries
    wait=wait_exponential(multiplier=1, min=1, max=60)  # Exponential backoff
)
def get_float(inspectLink):
    payload = {'inspectLink': inspectLink}
    try:
        get_float = s.get(url=float_cheacker, params=payload, headers=headers).json()
    except:
        time.sleep(1.5)
        s.proxies.update(prox_list[randint(0, len(prox_list))])
        get_float = s.get(url=float_cheacker, params=payload, headers=headers).json()

    return get_float['paintwear']


def item_search(itemname, link_to_item, maxprice, minfloat=1, qty=1):
    run = True

    while run:

        s.proxies.update(prox_list[random.randint(0, len(prox_list) - 1)])

        try:
            items1 = s.get(url=link_to_item + page_url, params=payload)
        except requests.exceptions.ProxyError:
            s.proxies.update(prox_list[random.randint(0, len(prox_list) - 1)])
            items1 = s.get(url=link_to_item + page_url, params=payload)

        soup = BeautifulSoup(str(items1.json()['results_html']), 'lxml')
        with open('t.html', 'w', encoding='utf-8') as f:
            f.write(str(soup))

        items = items1.json()
        for i in items['listinginfo']:

            price_code = (soup.find("div", id=f'listing_{i}', ).find('span', {
                'class': "market_listing_price market_listing_price_with_fee"})).text.replace(',', '.')

            subtotal_code = (soup.find("div", id=f'listing_{i}', ).find('span', {
                'class': "market_listing_price market_listing_price_without_fee"})).text.replace(',', '.')

            price = float(re.findall(r'\d+', price_code)[0] + re.findall(r'\d+', price_code)[1])
            subtotal = float(re.findall(r'\d+', subtotal_code)[0] + re.findall(r'\d+', subtotal_code)[1])
            fee = price - subtotal

            if price / 100 <= maxprice:

                s.proxies.update(prox_list[random.randint(0, len(prox_list) - 1)])
                listingid = items['listinginfo'][i]
                assetid = listingid['asset']['id']
                item_base_link = str(listingid['asset']['market_actions'][0]['link']).replace('%listingid%',
                                                                                              str(i)).replace(
                    '%assetid%', str(assetid))
                try:
                    item_float = get_float(item_base_link)
                except:
                    s.proxies.update(prox_list[random.randint(0, len(prox_list) - 1)])
                    item_float = get_float(item_base_link)
                print(itemname)

                if item_float <= minfloat:
                    try:
                        buy = s.post(f'https://steamcommunity.com/market/buylisting/{i}',
                                 data=buy_payload(subtotal, fee, price,qty), headers=buy_headers(i, link_to_item))
                        if int(buy.json()["wallet_info"]["success"]) == 1:
                            logging.info(
                                f'{datetime.now()} BUY>>> item: {itemname}\nid: {i}\nfloat : {item_float}\nprice: {price / 100}\nspent: {(price / 100) * qty}\nProxy: {s.proxies}')
                            time.sleep(1)
                        else:
                            logging.info(
                                f'{datetime.now()} UNABLE TO BUY>>> item: {itemname}\nid: {i} ')
                    except:
                        logging.info(
                            f'{datetime.now()} UNABLE TO BUY>>> item: {itemname}\nid: {i} ')


        time.sleep(10)


def get_url_to_item(itemname, session):
    itempayload = {'q': itemname, }

    try:
        resp = session.get(url=base_market_url + itemname.replace(' ', '+'), params=itempayload, cookies=cookes)
        soup = BeautifulSoup(resp.text, 'lxml')
        link_item = soup.find('a', class_='market_listing_row_link', id="resultlink_0").get('href')
    except:
        s.proxies.update(prox_list[random.randint(0, len(prox_list) - 1)])
        resp = session.get(url=base_market_url + itemname.replace(' ', '+'), params=itempayload, cookies=cookes)
        soup = BeautifulSoup(resp.text, 'lxml')
        link_item = soup.find('a', class_='market_listing_row_link', id="resultlink_0").get('href')

    logging.info(f'{datetime.now()}: resp.url: {resp.url} link: {link_item} Proxy: {session.proxies}')

    return link_item


l = get_url_to_item('AUG | Contractor', s)
item_search('itemname', l, maxprice=1)

# links = [get_url_to_item(i, s) for i in search]
#
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     futures = []
#     for url in links:
#         futures.append(executor.submit(item_search,itemname = search[links.index(url)],link_to_item = url,maxprice = 1))
#     for future in concurrent.futures.as_completed(futures):
#         future.result()
