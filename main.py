from re import findall
from sys import stdout
from time import time, sleep
from json import load
from random import choice
from concurrent.futures import ThreadPoolExecutor, as_completed

from requests import Session
from bs4 import BeautifulSoup
from sqlalchemy import select
from database import *

import logging
logging.basicConfig(
    encoding='utf-8',
    level=logging.INFO,
    format='%(asctime)s: [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('steam.log'),
        logging.StreamHandler(stdout)
    ]
)

ITEM_LINK_BASE_URL = 'https://steamcommunity.com/market/listings/730/'
FLOAT_CHECK_URL = 'https://api-float.cs.trade/getFloat?url='
BUY_ITEM_URL = 'https://steamcommunity.com/market/buylisting/'


def store_item(item_id):
    with session_scope() as session:
        listing = Listing()
        listing.id = str(item_id)
        session.add(listing)


def get_price_from_code(price_code):
    f = ''
    mas = findall(r'\d+', price_code)
    for i in mas:
        f += i
    return int(f)


def get_float(settings, link, minfloat, price, subtotal, name, link_to_item, item_id):
    while True:
        try:
            session = Session()
            session.proxies.update({
                'http': choice(settings.get('proxies')),
                'https': choice(settings.get('proxies')),
            })

            response = session.get(
                url=FLOAT_CHECK_URL + link,
                headers={'User-Agent': settings.get('agent')},
            )

            if response.text[0] != '{':
                logging.error(f'Float >>> Service not responding: {response.text}')
                return 0

            response = response.json()
            float_value = response.get('result', {}).get('floatvalue')
            if float_value is None:
                return None

            logging.info(f"Float >>> {name} {item_id}: {float_value}")
            if float(float_value) <= minfloat:
                try:
                    data = {
                        'sessionid': settings.get('session_id'),
                        'currency': '18',
                        'subtotal': str(int(subtotal)),
                        'fee': str(int(price - subtotal)),
                        'total': str(int(price)),
                        'quantity': '1',
                        'billing_state': '',
                        'save_my_address': '0'
                    }

                    headers = {
                        'Accept': '*/*',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'ru,en;q=0.9',
                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'Cookie': settings.get('cookies'),
                        'Host': 'steamcommunity.com',
                        'Referer': link_to_item,
                        'User-Agent': settings.get('agent')
                    }

                    session.proxies.update({
                        'http': choice(settings.get('proxies')),
                        'https': choice(settings.get('proxies')),
                    })

                    buy = session.post(
                        BUY_ITEM_URL + item_id,
                        data=data,
                        headers=headers
                    )

                    if buy.json().get('wallet_info', {}).get('success', False):
                        logging.info(f'Buy >>> {name} -> {item_id} -> Float [{float_value}] -> price [{price / 100}]')
                        store_item(item_id)
                        return 1

                    else:
                        logging.warning(f'Unable >>> {name} -> {item_id}: {buy.content}')
                        store_item(item_id)
                        return 0

                except Exception as e:
                    logging.error(f'Buy >>> {repr(e)}')
                    return 0

            else:
                store_item(item_id)
                return 0

        except Exception as e:
            logging.error(f'Float >>> {name} -> {repr(e)}')


def get_price(soup, item_id):
    try:
        price_code = soup.find('div', id=f'listing_{item_id}').find('span', {
            'class': 'market_listing_price market_listing_price_with_fee'
        }).text.replace(',', '.')

        subtotal_code = soup.find('div', id=f'listing_{item_id}').find('span', {
            'class': 'market_listing_price market_listing_price_without_fee'
        }).text.replace(',', '.')

        price = get_price_from_code(price_code)
        subtotal = get_price_from_code(subtotal_code)
        return price, subtotal

    except Exception as e:
        logging.error(f'Price >>> {item_id} -> {repr(e)}')
        return None, None


def search(settings, item):
    name = item.get('name')
    link = item.get('link')
    max_price = item.get('price')
    min_float = item.get('float')

    logging.info(f'Started >>> {name}')
    clock_tick = 0

    while True:
        if time() - clock_tick >= settings.get('log_interval'):
            logging.info(f'Searching >>> {name} -> {link}')
            clock_tick = time()

        futures = []
        try:
            page_url = '/render'
            payload = {
                'query': '',
                'start': 0,
                'count': 100,
                'country': 'UA',
                'language': 'english',
                'currency': '18'
            }

            session = Session()
            session.proxies.update({
                'http': choice(settings.get('proxies')),
                'https': choice(settings.get('proxies')),
            })

            items = session.get(
                link + page_url,
                params=payload,
                headers={'Referer': link}
            ).json()

            if items is None:
                sleep(0.5)
                continue

            with ThreadPoolExecutor() as pool:
                with session_scope() as db_session:
                    query = select(Listing).where(Listing.id.in_([i for i in items.get('listinginfo').keys()]))
                    listing_ids = list(map(lambda x: x.id, db_session.scalars(query).all()))

                for listing in items.get('listinginfo').values():
                    if listing.get('listingid') not in listing_ids:
                        price, subtotal = get_price(
                            soup=BeautifulSoup(items.get('results_html'), 'lxml'),
                            item_id=listing.get('listingid')
                        )

                        if price is None or subtotal is None:
                            continue

                        if price / 100 > max_price:
                            break

                        item_base_link = listing['asset']['market_actions'][0]['link']
                        item_base_link = item_base_link.replace('%listingid%', listing.get('listingid'))
                        item_base_link = item_base_link.replace('%assetid%', listing.get('asset').get('id'))

                        futures.append(
                            pool.submit(
                                get_float,
                                settings=settings,
                                link=item_base_link,
                                minfloat=min_float,
                                price=price,
                                subtotal=subtotal,
                                name=name,
                                link_to_item=link,
                                item_id=listing.get('listingid')
                            )
                        )

        except Exception as e:
            logging.error(f'Search >>> {name} -> {repr(e)}')

        finally:
            for future in as_completed(futures):
                future.result()
            sleep(0.5)


def main():
    with open('settings.json') as file:
        settings = load(file)

    logging.info('Collected items')
    for item in settings.get('items'):
        name = item.get('name')
        item.update(link=ITEM_LINK_BASE_URL + name)
        logging.info(f'Collected Item >>> {name}')

    with ThreadPoolExecutor(max_workers=200) as pool:
        futures = []
        for item in settings.get('items'):
            futures.append(pool.submit(
                search,
                settings=settings,
                item=item
            ))

        for result in as_completed(futures):
            logging.info(result)


if __name__ == '__main__':
    main()
