import time

from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_exponential
base_market_url = 'https://steamcommunity.com/market/search?q='


search = 'StatTrak™ P90 | Вирус'# Поисковая строка


cooke = {'sessionid':'e579b88b78fbed962aeccc4e', 'timezoneOffset':'14400,0', 'Steam_Language':'russian', 'steamCountry':'RU%7C39eaabc62621425b7351fa48d901d07a', 'strResponsiveViewPrefs':'touch'}


@retry(
    stop=stop_after_attempt(10), # Maximum number of retries
    wait=wait_exponential(multiplier=1, min=1, max=60) # Exponential backoff
)
def get_url_to_item(search, session):

    payload = {
        'q': search,
    }

    resp = session.get(url=base_market_url + search.replace(' ','+'), params=payload,cookies=cooke)
    print(resp.url)

    with open('test.html','w', encoding='utf-8') as f:
        f.write(str(resp.text))

    soup = BeautifulSoup(resp.text,'lxml')
    link = soup.find('a',class_ = 'market_listing_row_link',id="resultlink_0").get('href')
    print(link)
    return (link)


from pysteamauth.auth import Steam
from pysteamauth.auth import Steam
from pysteamauth.errors import SteamError, custom_error_exception


import asyncio
from pysteamauth.auth import Steam
from pysteamauth.errors import SteamError
import requests

sdresp = None
async def main():
    steam = Steam(
        login='Andrey_Prokofiev',
        password='u!:&JL7!Avuj?yW',
    )

    await steam.login_to_steam()
    sdresp = await (steam.request('https://steamcommunity.com/market/',))


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
#
# browser.get('https://steamcommunity.com/login/home/?goto=market%2F')
# time.sleep(3)
# browser.find_element(By.CSS_SELECTOR,'#responsive_page_template_content > div.page_content > div:nth-child(1) > div > div > div > div.newlogindialog_FormContainer_3jLIH > div > form > div:nth-child(1) > input').send_keys('Andrey_Prokofiev')
# browser.find_element(By.XPATH,'//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[2]/input').send_keys('u!:&JL7!Avuj?yW')
# browser.find_element(By.XPATH,'//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[4]/button').click()
#
# cookes = (browser.get_cookies())
# print(requests.get('https://steamcommunity.com/market/',params={cookes[0]['name']:cookes[0]['value'],cookes[1]['name']:cookes[1]['value'], cookes[2]['name']:cookes[2]['value']}).text)

#[{'domain': 'steamcommunity.com', 'expiry': 1726706861, 'httpOnly': False, 'name': 'timezoneOffset', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '14400,0'}, {'domain': 'steamcommunity.com', 'httpOnly': True, 'name': 'steamCountry', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'RU%7Cd3eaa930e0b7780b928e88ac54d65f72'}, {'domain': 'steamcommunity.com', 'httpOnly': False, 'name': 'sessionid', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'ac11f1ee515ea00f0dc47df1'}]

#https://steamcommunity.com/market/listings/730/AK-47%20%7C%20Asiimov%20%28Factory%20New%29
#BuyMarketListing('listing', '4399510226309769467', 730, '2', '33381783269')
p = {
    'action':'BuyMarketListing',
    'sElementPrefix':'listing',
    'listingid':'4399510226309769467',
    'appid':'730',
    'contextid':'2',
    'itemid':'33381783269',
}
authentication_url = 'https://store.steampowered.com/login/'
payload = {
    'username': 'Andrey_Prokofiev',
    'password': 'u!:&JL7!Avuj?yW',
    'captcha_text' : ''
}
with requests.sessions.Session() as session:
    session.auth = ("Andrey_Prokofiev", "u!:&JL7!Avuj?yW")
    lo = (requests.get('https://steamcommunity.com/market/listings/730/AK-47%20%7C%20Asiimov%20%28Factory%20New%29',params=p,cookies=session.cookies))
    print(lo.text)
    print(lo.cookies)
    print(lo.headers)





