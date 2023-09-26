# from tenacity import retry, stop_after_attempt, wait_exponential
# @retry(
#     stop=stop_after_attempt(4), # Maximum number of retries
#     wait=wait_exponential(multiplier=1, min=1, max=60) # Exponential backoff
# )

COEFF = 86.956521739130434782608695652174

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

base_market_url = 'https://steamcommunity.com/market/search?q='

page_url = '/render/?query=&start=0&count=50&country=RU&language=english&currency=18&format=json'

float_cheacker = 'https://tradeit.gg/api/steam/v1/steams/float-item-finder'


def set_buy_headers(listing_id, refer_link): return {
    'POST': f'/market/buylisting/{listing_id} HTTP/1.1',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '117',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'timezoneOffset=14400,0; browserid=2765828910521038245; sessionid=f5b4846f421bc918f22a74c0; steamCountry=RU%7C6607ef4ee463b8f05f82c3d839bd63e6; steamLoginSecure=76561199085391840%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQ1OF8yMzMzQzY4MF9FMkNBMCIsICJzdWIiOiAiNzY1NjExOTkwODUzOTE4NDAiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY5NTMxOTY4OSwgIm5iZiI6IDE2ODY1OTMwODgsICJpYXQiOiAxNjk1MjMzMDg4LCAianRpIjogIjBENEJfMjMzM0M2NkFfRTBGNDgiLCAib2F0IjogMTY5NTIzMzA4OCwgInJ0X2V4cCI6IDE3MTM2MDI2MzYsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICI2Mi4xMTguNzIuNDkiLCAiaXBfY29uZmlybWVyIjogIjMxLjEyOS42NC4xNjAiIH0.4XUzBosVTYqI1QxaITS0bsUBt40SiTrrP6mMHCbnB6yLPExaMZG1leJ3xAKkAgzUGwTe_07HKS_G4Jr38SXfCg; Steam_Language=english; webTradeEligibility=%7B%22allowed%22%3A1%2C%22allowed_at_time%22%3A0%2C%22steamguard_required_days%22%3A15%2C%22new_device_cooldown_days%22%3A0%2C%22time_checked%22%3A1695233210%7D; strInventoryLastContext=730_2',
    'Host': 'steamcommunity.com',
    'Referer': refer_link,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.734 Yowser/2.5 Safari/537.36'

}


def set_buy_payload(subtotal, fee, total): return {
    'sessionid': 'f5b4846f421bc918f22a74c0',
    'currency': '18',
    'subtotal': str(int(subtotal)),
    'fee': str(int(fee)),
    'total': str(int(total)),
    'quantity': '1',
    'billing_state': '',
    'save_my_address': '0'
}


c = {
    'timezoneOffset	': '14400,0',
    'browserid': '2765828910521038245',
    'Steam_Language': 'english',
    'strInventoryLastContext': '730_2',
    'steamLoginSecure': '76561199085391840%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQ1OF8yMzMzQzY4MF9FMkNBMCIsICJzdWIiOiAiNzY1NjExOTkwODUzOTE4NDAiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY5NTQwOTM2NywgIm5iZiI6IDE2ODY2ODI0NTIsICJpYXQiOiAxNjk1MzIyNDUyLCAianRpIjogIjBENEJfMjMzM0M2QjVfQ0QyRUQiLCAib2F0IjogMTY5NTIzMzA4OCwgInJ0X2V4cCI6IDE3MTM2MDI2MzYsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICI2Mi4xMTguNzIuNDkiLCAiaXBfY29uZmlybWVyIjogIjMxLjEyOS42NC4xNjAiIH0.k7h-ypvSo_HrIi7XjB_7efOuMYj3PJyI4ya2ACUx7iqf8Cxn2Xe8dGUVFnRDcbMDEAR_S_vgHleqVAeMJGnCCQ',
    'recentlyVisitedAppHubs': '730',
    'sessionid': '4ffc951c4b8e86b3c63d6386',
    'webTradeEligibility': '%7B%22allowed%22%3A1%2C%22allowed_at_time%22%3A0%2C%22steamguard_required_days%22%3A15%2C%22new_device_cooldown_days%22%3A0%2C%22time_checked%22%3A1695393132%7D',
    'app_impressions': '730@2_9_100006_100202'

}

cookies = {'timezoneOffset': '14400,0',
           'browserid': '2765828910521038245',
           'sessionid': 'f5b4846f421bc918f22a74c0',
           'steamCountry': 'RU%7C6607ef4ee463b8f05f82c3d839bd63e6',
           'steamLoginSecure': '76561199085391840%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQ1OF8yMzMzQzY4MF9FMkNBMCIsICJzdWIiOiAiNzY1NjExOTkwODUzOTE4NDAiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY5NTMxOTY4OSwgIm5iZiI6IDE2ODY1OTMwODgsICJpYXQiOiAxNjk1MjMzMDg4LCAianRpIjogIjBENEJfMjMzM0M2NkFfRTBGNDgiLCAib2F0IjogMTY5NTIzMzA4OCwgInJ0X2V4cCI6IDE3MTM2MDI2MzYsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICI2Mi4xMTguNzIuNDkiLCAiaXBfY29uZmlybWVyIjogIjMxLjEyOS42NC4xNjAiIH0.4XUzBosVTYqI1QxaITS0bsUBt40SiTrrP6mMHCbnB6yLPExaMZG1leJ3xAKkAgzUGwTe_07HKS_G4Jr38SXfCg',
           'Steam_Language': 'english',

           }

buylink = 'https://steamcommunity.com/market/buylisting/4395006694800366176'
'''country=UA&language=english&currency=18&item_nameid=2384550&two_factor=0'''

cookebuy = {
    'timezoneOffset': '14400,0',
    'browserid': '2765828910521038245',
    'sessionid': 'f5b4846f421bc918f22a74c0',
    'steamCountry': 'RU%7C6607ef4ee463b8f05f82c3d839bd63e6',
    'steamLoginSecure': '76561199085391840%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQ1OF8yMzMzQzY4MF9FMkNBMCIsICJzdWIiOiAiNzY1NjExOTkwODUzOTE4NDAiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY5NTMxOTY4OSwgIm5iZiI6IDE2ODY1OTMwODgsICJpYXQiOiAxNjk1MjMzMDg4LCAianRpIjogIjBENEJfMjMzM0M2NkFfRTBGNDgiLCAib2F0IjogMTY5NTIzMzA4OCwgInJ0X2V4cCI6IDE3MTM2MDI2MzYsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICI2Mi4xMTguNzIuNDkiLCAiaXBfY29uZmlybWVyIjogIjMxLjEyOS42NC4xNjAiIH0.4XUzBosVTYqI1QxaITS0bsUBt40SiTrrP6mMHCbnB6yLPExaMZG1leJ3xAKkAgzUGwTe_07HKS_G4Jr38SXfCg',
    'Steam_Language': 'english',
    'webTradeEligibility': '%7B%22allowed%22%3A1%2C%22allowed_at_time%22%3A0%2C%22steamguard_required_days%22%3A15%2C%22new_device_cooldown_days%22%3A0%2C%22time_checked%22%3A1695233210%7D',
    'strInventoryLastContext': '730_2'
}

payload_buy = {
    'sessionid': 'f5b4846f421bc918f22a74c0',
    'currency': '18',
    'subtotal': '56',
    'fee': '7',
    'total': '63',
    'quantity': '1',
    'billing_state': '',
    'save_my_address': '0'
}

h = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'timezoneOffset=14400,0; browserid=2765828910521038245; Steam_Language=english; strInventoryLastContext=730_2; steamLoginSecure=76561199085391840%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQ1OF8yMzMzQzY4MF9FMkNBMCIsICJzdWIiOiAiNzY1NjExOTkwODUzOTE4NDAiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY5NTQwOTM2NywgIm5iZiI6IDE2ODY2ODI0NTIsICJpYXQiOiAxNjk1MzIyNDUyLCAianRpIjogIjBENEJfMjMzM0M2QjVfQ0QyRUQiLCAib2F0IjogMTY5NTIzMzA4OCwgInJ0X2V4cCI6IDE3MTM2MDI2MzYsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICI2Mi4xMTguNzIuNDkiLCAiaXBfY29uZmlybWVyIjogIjMxLjEyOS42NC4xNjAiIH0.k7h-ypvSo_HrIi7XjB_7efOuMYj3PJyI4ya2ACUx7iqf8Cxn2Xe8dGUVFnRDcbMDEAR_S_vgHleqVAeMJGnCCQ; recentlyVisitedAppHubs=730; sessionid=4ffc951c4b8e86b3c63d6386; webTradeEligibility=%7B%22allowed%22%3A1%2C%22allowed_at_time%22%3A0%2C%22steamguard_required_days%22%3A15%2C%22new_device_cooldown_days%22%3A0%2C%22time_checked%22%3A1695393132%7D; app_impressions=730@2_9_100006_100202',
    'Host': 'steamcommunity.com',
    'Referer': 'https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B0%5D=any&category_730_ProPlayer%5B0%5D=any&category_730_StickerCapsule%5B0%5D=any&category_730_TournamentTeam%5B0%5D=any&category_730_Exterior%5B0%5D=tag_WearCategory2&category_730_Exterior%5B1%5D=tag_WearCategory4&category_730_Exterior%5B2%5D=tag_WearCategoryNA&appid=730',
    'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "YaBrowser";v="23"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': 'Windows',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.734 Yowser/2.5 Safari/537.36'

}

'''Cookie:
timezoneOffset=14400,0; browserid=2765828910521038245; sessionid=f5b4846f421bc918f22a74c0; Steam_Language=english; webTradeEligibility=%7B%22allowed%22%3A1%2C%22allowed_at_time%22%3A0%2C%22steamguard_required_days%22%3A15%2C%22new_device_cooldown_days%22%3A0%2C%22time_checked%22%3A1695233210%7D; strInventoryLastContext=730_2; steamCountry=RU%7Cc0f039c1bc6a8407e52e32733204bed0; steamLoginSecure=76561199085391840%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQ1OF8yMzMzQzY4MF9FMkNBMCIsICJzdWIiOiAiNzY1NjExOTkwODUzOTE4NDAiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY5NTQwOTM2NywgIm5iZiI6IDE2ODY2ODI0NTIsICJpYXQiOiAxNjk1MzIyNDUyLCAianRpIjogIjBENEJfMjMzM0M2QjVfQ0QyRUQiLCAib2F0IjogMTY5NTIzMzA4OCwgInJ0X2V4cCI6IDE3MTM2MDI2MzYsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICI2Mi4xMTguNzIuNDkiLCAiaXBfY29uZmlybWVyIjogIjMxLjEyOS42NC4xNjAiIH0.k7h-ypvSo_HrIi7XjB_7efOuMYj3PJyI4ya2ACUx7iqf8Cxn2Xe8dGUVFnRDcbMDEAR_S_vgHleqVAeMJGnCCQ; recentlyVisitedAppHubs=730; app_impressions=730@2_9_100006_100202'''

# 'webTradeEligibility': '%7B%22allowed%22%3A1%2C%22allowed_at_time%22%3A0%2C%22steamguard_required_days%22%3A15'
#                        '%2C%22new_device_cooldown_days%22%3A0%2C%22time_checked%22%3A1695233210%7D'


'''



https://steamcommunity.com/market/buylisting/4375866396344743549

POST /market/buylisting/4375866396344743549 HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: ru,en;q=0.9
Connection: keep-alive
Content-Length: 117
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: timezoneOffset=14400,0; browserid=2765828910521038245; sessionid=f5b4846f421bc918f22a74c0; steamCountry=RU%7C6607ef4ee463b8f05f82c3d839bd63e6; steamLoginSecure=76561199085391840%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQ1OF8yMzMzQzY4MF9FMkNBMCIsICJzdWIiOiAiNzY1NjExOTkwODUzOTE4NDAiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY5NTMxOTY4OSwgIm5iZiI6IDE2ODY1OTMwODgsICJpYXQiOiAxNjk1MjMzMDg4LCAianRpIjogIjBENEJfMjMzM0M2NkFfRTBGNDgiLCAib2F0IjogMTY5NTIzMzA4OCwgInJ0X2V4cCI6IDE3MTM2MDI2MzYsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICI2Mi4xMTguNzIuNDkiLCAiaXBfY29uZmlybWVyIjogIjMxLjEyOS42NC4xNjAiIH0.4XUzBosVTYqI1QxaITS0bsUBt40SiTrrP6mMHCbnB6yLPExaMZG1leJ3xAKkAgzUGwTe_07HKS_G4Jr38SXfCg; Steam_Language=english; webTradeEligibility=%7B%22allowed%22%3A1%2C%22allowed_at_time%22%3A0%2C%22steamguard_required_days%22%3A15%2C%22new_device_cooldown_days%22%3A0%2C%22time_checked%22%3A1695233210%7D; strInventoryLastContext=730_2
Host: steamcommunity.com
Origin: https://steamcommunity.com
Referer: https://steamcommunity.com/market/listings/730/Tec-9%20%7C%20Groundwater%20%28Battle-Scarred%29
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.734 Yowser/2.5 Safari/537.36
sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "YaBrowser";v="23"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"


HTTP/1.1 200 OK
{'Server': 'nginx'
Content-Type: application/json; charset=utf-8
Vary: Accept-Encoding, Origin
Access-Control-Allow-Origin: https://steamcommunity.com
Access-Control-Allow-Methods: POST, GET, HEAD, OPTIONS
Access-Control-Allow-Credentials: true
Access-Control-Max-Age: 604800
Access-Control-Expose-Headers: X-NotLoggedIn
X-Frame-Options: SAMEORIGIN
Expires: Mon, 26 Jul 1997 05:00:00 GMT
Cache-Control: no-cache
Content-Encoding: gzip
Vary: Accept-Encoding
Content-Length: 190
Date: Wed, 20 Sep 2023 23:51:07 GMT
Connection: keep-alive}

{"wallet_info":{"wallet_currency":18,"wallet_country":"UA","wallet_state":"","wallet_fee":"1","wallet_fee_minimum":"1","wallet_fee_percent":"0.05","wallet_publisher_fee_percent_default":"0.10","wallet_fee_base":"0","wallet_balance":"3006","wallet_delayed_balance":"0","wallet_max_balance":"7300000","wallet_trade_max_balance":"6570000","success":1,"rwgrsn":-2}}






send @ https://community.akamai.steamstatic.com/public/javascript/jquery-1.11.1.min.js?v=.isFTSRckeNhC:4
ajax @ https://community.akamai.steamstatic.com/public/javascript/jquery-1.11.1.min.js?v=.isFTSRckeNhC:4
OnAccept @ https://community.akamai.steamstatic.com/public/javascript/market.js?v=uxihnOZh-iuR&l=english:923
(anonymous) @ https://community.akamai.steamstatic.com/public/javascript/prototype-1.7.js?v=.55t44gwuwgvw:400
responder @ https://community.akamai.steamstatic.com/public/javascript/prototype-1.7.js?v=.55t44gwuwgvw:5599

curl "https://steamcommunity.com/market/buylisting/4375866396344743549" ^
  -H "Accept: */*" ^
  -H "Accept-Language: ru,en;q=0.9" ^
  -H "Connection: keep-alive" ^
  -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" ^
  -H "Cookie: timezoneOffset=14400,0; browserid=2765828910521038245; sessionid=f5b4846f421bc918f22a74c0; steamCountry=RU^%^7C6607ef4ee463b8f05f82c3d839bd63e6; steamLoginSecure=76561199085391840^%^7C^%^7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQ1OF8yMzMzQzY4MF9FMkNBMCIsICJzdWIiOiAiNzY1NjExOTkwODUzOTE4NDAiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY5NTMxOTY4OSwgIm5iZiI6IDE2ODY1OTMwODgsICJpYXQiOiAxNjk1MjMzMDg4LCAianRpIjogIjBENEJfMjMzM0M2NkFfRTBGNDgiLCAib2F0IjogMTY5NTIzMzA4OCwgInJ0X2V4cCI6IDE3MTM2MDI2MzYsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICI2Mi4xMTguNzIuNDkiLCAiaXBfY29uZmlybWVyIjogIjMxLjEyOS42NC4xNjAiIH0.4XUzBosVTYqI1QxaITS0bsUBt40SiTrrP6mMHCbnB6yLPExaMZG1leJ3xAKkAgzUGwTe_07HKS_G4Jr38SXfCg; Steam_Language=english; webTradeEligibility=^%^7B^%^22allowed^%^22^%^3A1^%^2C^%^22allowed_at_time^%^22^%^3A0^%^2C^%^22steamguard_required_days^%^22^%^3A15^%^2C^%^22new_device_cooldown_days^%^22^%^3A0^%^2C^%^22time_checked^%^22^%^3A1695233210^%^7D; strInventoryLastContext=730_2" ^
  -H "Origin: https://steamcommunity.com" ^
  -H "Referer: https://steamcommunity.com/market/listings/730/Tec-9^%^20^%^7C^%^20Groundwater^%^20^%^28Battle-Scarred^%^29" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: same-origin" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.734 Yowser/2.5 Safari/537.36" ^
  -H "sec-ch-ua: ^\^"Not.A/Brand^\^";v=^\^"8^\^", ^\^"Chromium^\^";v=^\^"114^\^", ^\^"YaBrowser^\^";v=^\^"23^\^"" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H "sec-ch-ua-platform: ^\^"Windows^\^"" ^
  --data-raw "sessionid=f5b4846f421bc918f22a74c0&currency=18&subtotal=56&fee=7&total=63&quantity=1&billing_state=&save_my_address=0" ^
  --compressed

BASH 
$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
$session.UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.734 Yowser/2.5 Safari/537.36"
$session.Cookies.Add((New-Object System.Net.Cookie("timezoneOffset", "14400,0", "/", "steamcommunity.com")))
$session.Cookies.Add((New-Object System.Net.Cookie("browserid", "2765828910521038245", "/", "steamcommunity.com")))
$session.Cookies.Add((New-Object System.Net.Cookie("sessionid", "f5b4846f421bc918f22a74c0", "/", "steamcommunity.com")))
$session.Cookies.Add((New-Object System.Net.Cookie("steamCountry", "RU%7C6607ef4ee463b8f05f82c3d839bd63e6", "/", "steamcommunity.com")))
$session.Cookies.Add((New-Object System.Net.Cookie("steamLoginSecure", "76561199085391840%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQ1OF8yMzMzQzY4MF9FMkNBMCIsICJzdWIiOiAiNzY1NjExOTkwODUzOTE4NDAiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY5NTMxOTY4OSwgIm5iZiI6IDE2ODY1OTMwODgsICJpYXQiOiAxNjk1MjMzMDg4LCAianRpIjogIjBENEJfMjMzM0M2NkFfRTBGNDgiLCAib2F0IjogMTY5NTIzMzA4OCwgInJ0X2V4cCI6IDE3MTM2MDI2MzYsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICI2Mi4xMTguNzIuNDkiLCAiaXBfY29uZmlybWVyIjogIjMxLjEyOS42NC4xNjAiIH0.4XUzBosVTYqI1QxaITS0bsUBt40SiTrrP6mMHCbnB6yLPExaMZG1leJ3xAKkAgzUGwTe_07HKS_G4Jr38SXfCg", "/", "steamcommunity.com")))
$session.Cookies.Add((New-Object System.Net.Cookie("Steam_Language", "english", "/", "steamcommunity.com")))
$session.Cookies.Add((New-Object System.Net.Cookie("webTradeEligibility", "%7B%22allowed%22%3A1%2C%22allowed_at_time%22%3A0%2C%22steamguard_required_days%22%3A15%2C%22new_device_cooldown_days%22%3A0%2C%22time_checked%22%3A1695233210%7D", "/", "steamcommunity.com")))
$session.Cookies.Add((New-Object System.Net.Cookie("strInventoryLastContext", "730_2", "/", "steamcommunity.com")))
Invoke-WebRequest -UseBasicParsing -Uri "https://steamcommunity.com/market/buylisting/4375866396344743549" `
-Method "POST" `
-WebSession $session `
-Headers @{
"Accept"="*/*"
  "Accept-Encoding"="gzip, deflate, br"
  "Accept-Language"="ru,en;q=0.9"
  "Origin"="https://steamcommunity.com"
  "Referer"="https://steamcommunity.com/market/listings/730/Tec-9%20%7C%20Groundwater%20%28Battle-Scarred%29"
  "Sec-Fetch-Dest"="empty"
  "Sec-Fetch-Mode"="cors"
  "Sec-Fetch-Site"="same-origin"
  "sec-ch-ua"="`"Not.A/Brand`";v=`"8`", `"Chromium`";v=`"114`", `"YaBrowser`";v=`"23`""
  "sec-ch-ua-mobile"="?0"
  "sec-ch-ua-platform"="`"Windows`""
} `
-ContentType "application/x-www-form-urlencoded; charset=UTF-8" `
-Body "sessionid=f5b4846f421bc918f22a74c0&currency=18&subtotal=56&fee=7&total=63&quantity=1&billing_state=&save_my_address=0"







$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
$session.UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.734 Yowser/2.5 Safari/537.36"
$session.Cookies.Add((New-Object System.Net.Cookie("timezoneOffset", "14400,0", "/", "steamcommunity.com")))
$session.Cookies.Add((New-Object System.Net.Cookie("browserid", "2765828910521038245", "/", "steamcommunity.com")))
$session.Cookies.Add((New-Object System.Net.Cookie("sessionid", "f5b4846f421bc918f22a74c0", "/", "steamcommunity.com")))
$session.Cookies.Add((New-Object System.Net.Cookie("steamCountry", "RU%7C6607ef4ee463b8f05f82c3d839bd63e6", "/", "steamcommunity.com")))
$session.Cookies.Add((New-Object System.Net.Cookie("steamLoginSecure", "76561199085391840%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQ1OF8yMzMzQzY4MF9FMkNBMCIsICJzdWIiOiAiNzY1NjExOTkwODUzOTE4NDAiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY5NTMxOTY4OSwgIm5iZiI6IDE2ODY1OTMwODgsICJpYXQiOiAxNjk1MjMzMDg4LCAianRpIjogIjBENEJfMjMzM0M2NkFfRTBGNDgiLCAib2F0IjogMTY5NTIzMzA4OCwgInJ0X2V4cCI6IDE3MTM2MDI2MzYsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICI2Mi4xMTguNzIuNDkiLCAiaXBfY29uZmlybWVyIjogIjMxLjEyOS42NC4xNjAiIH0.4XUzBosVTYqI1QxaITS0bsUBt40SiTrrP6mMHCbnB6yLPExaMZG1leJ3xAKkAgzUGwTe_07HKS_G4Jr38SXfCg", "/", "steamcommunity.com")))
$session.Cookies.Add((New-Object System.Net.Cookie("Steam_Language", "english", "/", "steamcommunity.com")))
$session.Cookies.Add((New-Object System.Net.Cookie("webTradeEligibility", "%7B%22allowed%22%3A1%2C%22allowed_at_time%22%3A0%2C%22steamguard_required_days%22%3A15%2C%22new_device_cooldown_days%22%3A0%2C%22time_checked%22%3A1695233210%7D", "/", "steamcommunity.com")))
$session.Cookies.Add((New-Object System.Net.Cookie("strInventoryLastContext", "730_2", "/", "steamcommunity.com")))
Invoke-WebRequest -UseBasicParsing -Uri "https://steamcommunity.com/market/buylisting/4375866396344743549" `
-Method "POST" `
-WebSession $session `
-Headers @{
"Accept"="*/*"
  "Accept-Encoding"="gzip, deflate, br"
  "Accept-Language"="ru,en;q=0.9"
  "Origin"="https://steamcommunity.com"
  "Referer"="https://steamcommunity.com/market/listings/730/Tec-9%20%7C%20Groundwater%20%28Battle-Scarred%29"
  "Sec-Fetch-Dest"="empty"
  "Sec-Fetch-Mode"="cors"
  "Sec-Fetch-Site"="same-origin"
  "sec-ch-ua"="`"Not.A/Brand`";v=`"8`", `"Chromium`";v=`"114`", `"YaBrowser`";v=`"23`""
  "sec-ch-ua-mobile"="?0"
  "sec-ch-ua-platform"="`"Windows`""
} `
-ContentType "application/x-www-form-urlencoded; charset=UTF-8" `
-Body "sessionid=f5b4846f421bc918f22a74c0&currency=18&subtotal=56&fee=7&total=63&quantity=1&billing_state=&save_my_address=0"














'''
