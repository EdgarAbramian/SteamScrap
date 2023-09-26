import pandas

dfheaders = pandas.read_csv('dist/main/zope/reqinfo.csv')


def set_buy_headers(listing_id, refer_link):
    return {
        'POST': f'/market/buylisting/{listing_id} HTTP/1.1',
        'Accept': '*/*',
        'Accept-Encoding': str(dfheaders['Accept-Encoding'][0]),
        'Accept-Language': str(dfheaders['Accept-Language'][0]),
        'Connection': str(dfheaders['Connection'][0]),
        'Content-Length': str(dfheaders['Content-Length'][0]),
        'Content-Type': str(dfheaders['Content-Type'][0]),
        'Cookie': str(dfheaders['Cookie'][0]),
        'Host': 'steamcommunity.com',
        'Referer': refer_link,
        'User-Agent': str(dfheaders['User-Agent'][0])
    }


def set_buy_payload(subtotal, fee, total): return {
    'sessionid': str(dfheaders['sessionid'][0]),
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
        'timezoneOffset': str(dfheaders['timezoneOffset'][0]),
        'browserid': str(dfheaders['browserid'][0]),
        'sessionid': str(dfheaders['sessionid'][0]),
        'steamCountry': str(dfheaders['steamCountry'][0]),
        'steamLoginSecure': str(dfheaders['steamLoginSecure'][0]),
        'Steam_Language': str(dfheaders['Steam_Language'][0]),
    }


base_market_url = 'https://steamcommunity.com/market/search?q='

page_url = '/render/?query=&start=0&count=50&country=RU&language=english&currency=18&format=json'

float_cheacker = 'https://tradeit.gg/api/steam/v1/steams/float-item-finder'

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
