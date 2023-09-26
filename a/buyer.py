import requests
from fake_useragent import UserAgent
from my_config import cookebuy
s = requests.Session()
ua = UserAgent()
headers = {
    'POST': '/market/buylisting/4375866396344743549 HTTP/1.1',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language':'ru,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '117',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'timezoneOffset=14400,0; browserid=2765828910521038245; sessionid=f5b4846f421bc918f22a74c0; steamCountry=RU%7C6607ef4ee463b8f05f82c3d839bd63e6; steamLoginSecure=76561199085391840%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQ1OF8yMzMzQzY4MF9FMkNBMCIsICJzdWIiOiAiNzY1NjExOTkwODUzOTE4NDAiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY5NTMxOTY4OSwgIm5iZiI6IDE2ODY1OTMwODgsICJpYXQiOiAxNjk1MjMzMDg4LCAianRpIjogIjBENEJfMjMzM0M2NkFfRTBGNDgiLCAib2F0IjogMTY5NTIzMzA4OCwgInJ0X2V4cCI6IDE3MTM2MDI2MzYsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICI2Mi4xMTguNzIuNDkiLCAiaXBfY29uZmlybWVyIjogIjMxLjEyOS42NC4xNjAiIH0.4XUzBosVTYqI1QxaITS0bsUBt40SiTrrP6mMHCbnB6yLPExaMZG1leJ3xAKkAgzUGwTe_07HKS_G4Jr38SXfCg; Steam_Language=english; webTradeEligibility=%7B%22allowed%22%3A1%2C%22allowed_at_time%22%3A0%2C%22steamguard_required_days%22%3A15%2C%22new_device_cooldown_days%22%3A0%2C%22time_checked%22%3A1695233210%7D; strInventoryLastContext=730_2',
    'Host': 'steamcommunity.com',
    'Referer': 'https://steamcommunity.com/market/listings/730/Tec-9%20%7C%20Groundwater%20%28Battle-Scarred%29',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.734 Yowser/2.5 Safari/537.36'

}
buylink = 'https://steamcommunity.com/market/buylisting/4395006636686553926'
c = {'timezoneOffset': '14400,0; ',
     'browserid':'2765828910521038245;' ,
     'sessionid': 'f5b4846f421bc918f22a74c0; ',
     'steamCountry': 'RU%7C6607ef4ee463b8f05f82c3d839bd63e6;',
     'steamLoginSecure': '76561199085391840%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQ1OF8yMzMzQzY4MF9FMkNBMCIsICJzdWIiOiAiNzY1NjExOTkwODUzOTE4NDAiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY5NTMxOTY4OSwgIm5iZiI6IDE2ODY1OTMwODgsICJpYXQiOiAxNjk1MjMzMDg4LCAianRpIjogIjBENEJfMjMzM0M2NkFfRTBGNDgiLCAib2F0IjogMTY5NTIzMzA4OCwgInJ0X2V4cCI6IDE3MTM2MDI2MzYsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICI2Mi4xMTguNzIuNDkiLCAiaXBfY29uZmlybWVyIjogIjMxLjEyOS42NC4xNjAiIH0.4XUzBosVTYqI1QxaITS0bsUBt40SiTrrP6mMHCbnB6yLPExaMZG1leJ3xAKkAgzUGwTe_07HKS_G4Jr38SXfCg; ',
     'Steam_Language': 'english;',
     'webTradeEligibility': '%7B%22allowed%22%3A1%2C%22allowed_at_time%22%3A0%2C%22steamguard_required_days%22%3A15%2C%22new_device_cooldown_days%22%3A0%2C%22time_checked%22%3A1695233210%7D'
     }
'''{'sessionid': 'f5b4846f421bc918f22a74c0', 'currency': '18', 'subtotal': '64', 'fee': '9', 'total': '73', 'quantity': '1', 'billing_state': '', 'save_my_address': '0'}
'''

payloadbuy = {
    'sessionid': 'f5b4846f421bc918f22a74c0',
    'currency': '18',
    'subtotal': '62',
    'fee': '9',
    'total': '71',
    'quantity': '1',
    'billing_state': '',
    'save_my_address': '0'
}

s.headers.update(headers)
s.proxies.update(cookebuy)
resp = (s.post(url=buylink,data = payloadbuy,headers=headers))
with open('r.html','w',encoding = 'utf-8') as f:
    f.write(str(resp.text))
print(resp.content)
print(resp.status_code)




'''
buylink = 'https://steamcommunity.com/market/buylisting/4371362796697537123'

sessionid: f5b4846f421bc918f22a74c0 - из куки берется
currency: 18                        - валюта
subtotal: 56                        -с
fee: 7
total: 63
quantity: 1
billing_state:
save_my_address: 0


Accept:
*/*
Accept-Encoding:
gzip, deflate, br
Accept-Language:
ru,en;q=0.9
Connection:
keep-alive
Content-Length:
117
Content-Type:
application/x-www-form-urlencoded; charset=UTF-8
Cookie:
timezoneOffset=14400,0; browserid=2765828910521038245; sessionid=f5b4846f421bc918f22a74c0; steamCountry=RU%7C6607ef4ee463b8f05f82c3d839bd63e6; steamLoginSecure=76561199085391840%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQ1OF8yMzMzQzY4MF9FMkNBMCIsICJzdWIiOiAiNzY1NjExOTkwODUzOTE4NDAiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY5NTMxOTY4OSwgIm5iZiI6IDE2ODY1OTMwODgsICJpYXQiOiAxNjk1MjMzMDg4LCAianRpIjogIjBENEJfMjMzM0M2NkFfRTBGNDgiLCAib2F0IjogMTY5NTIzMzA4OCwgInJ0X2V4cCI6IDE3MTM2MDI2MzYsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICI2Mi4xMTguNzIuNDkiLCAiaXBfY29uZmlybWVyIjogIjMxLjEyOS42NC4xNjAiIH0.4XUzBosVTYqI1QxaITS0bsUBt40SiTrrP6mMHCbnB6yLPExaMZG1leJ3xAKkAgzUGwTe_07HKS_G4Jr38SXfCg; Steam_Language=english; webTradeEligibility=%7B%22allowed%22%3A1%2C%22allowed_at_time%22%3A0%2C%22steamguard_required_days%22%3A15%2C%22new_device_cooldown_days%22%3A0%2C%22time_checked%22%3A1695233210%7D
Host:
steamcommunity.com
Origin:
https://steamcommunity.com
Referer:
https://steamcommunity.com/market/listings/730/AUG%20%7C%20Contractor%20%28Field-Tested%29
Sec-Ch-Ua:
"Not.A/Brand";v="8", "Chromium";v="114", "YaBrowser";v="23"
Sec-Ch-Ua-Mobile:
?0
Sec-Ch-Ua-Platform:
"Windows"
Sec-Fetch-Dest:
empty
Sec-Fetch-Mode:
cors
Sec-Fetch-Site:
same-origin
User-Agent:
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.734 Yowser/2.5 Sa

"https://steamcommunity.com/market/listings/730/AUG | Contractor#buylisting|4401762036182792104|730|2|33395814025"
'''