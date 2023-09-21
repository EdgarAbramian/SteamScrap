# from tenacity import retry, stop_after_attempt, wait_exponential
# @retry(
#     stop=stop_after_attempt(4), # Maximum number of retries
#     wait=wait_exponential(multiplier=1, min=1, max=60) # Exponential backoff
# )

COEFF = 86.956521739130434782608695652174

prox_list = [
    {"https": 'http://edikaraslanov_gmail_com:4bc4ca9131@193.176.227.8:30013/'},
    {"https": 'http://edikaraslanov_gmail_com:4bc4ca9131@193.176.227.105:30013/'},
    {"https": 'http://edikaraslanov_gmail_com:4bc4ca9131@193.176.220.166:30013/'},
    {"https": 'http://edikaraslanov_gmail_com:4bc4ca9131@193.176.220.129:30013/'},
    {"https": 'http://edikaraslanov_gmail_com:4bc4ca9131@193.176.220.6:30013/'},

    {"https": 'http://edikaraslanov_gmail_com:4bc4ca9131@193.176.220.164:30013/'},
    {"https": 'http://edikaraslanov_gmail_com:4bc4ca9131@193.176.220.21:30013/'},
    {"https": 'http://edikaraslanov_gmail_com:4bc4ca9131@193.176.227.142:30013/'},
    {"https": 'http://edikaraslanov_gmail_com:4bc4ca9131@193.176.220.86:30013/'},
    {"https": 'http://edikaraslanov_gmail_com:4bc4ca9131@193.176.227.90:30013/'},
]

base_market_url = 'https://steamcommunity.com/market/search?q='


def buy_headers(listing_id, refer_link): return {
    'POST': f'/market/buylisting/{listing_id} HTTP/1.1',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language':'ru,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '117',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'timezoneOffset=14400,0; browserid=2765828910521038245; sessionid=f5b4846f421bc918f22a74c0; steamCountry=RU%7C6607ef4ee463b8f05f82c3d839bd63e6; steamLoginSecure=76561199085391840%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQ1OF8yMzMzQzY4MF9FMkNBMCIsICJzdWIiOiAiNzY1NjExOTkwODUzOTE4NDAiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY5NTMxOTY4OSwgIm5iZiI6IDE2ODY1OTMwODgsICJpYXQiOiAxNjk1MjMzMDg4LCAianRpIjogIjBENEJfMjMzM0M2NkFfRTBGNDgiLCAib2F0IjogMTY5NTIzMzA4OCwgInJ0X2V4cCI6IDE3MTM2MDI2MzYsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICI2Mi4xMTguNzIuNDkiLCAiaXBfY29uZmlybWVyIjogIjMxLjEyOS42NC4xNjAiIH0.4XUzBosVTYqI1QxaITS0bsUBt40SiTrrP6mMHCbnB6yLPExaMZG1leJ3xAKkAgzUGwTe_07HKS_G4Jr38SXfCg; Steam_Language=english; webTradeEligibility=%7B%22allowed%22%3A1%2C%22allowed_at_time%22%3A0%2C%22steamguard_required_days%22%3A15%2C%22new_device_cooldown_days%22%3A0%2C%22time_checked%22%3A1695233210%7D; strInventoryLastContext=730_2',
    'Host': 'steamcommunity.com',
    'Referer': refer_link,
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.734 Yowser/2.5 Safari/537.36'

}


def buy_payload(subtotal, fee, total, qty): return {
    'sessionid': 'f5b4846f421bc918f22a74c0',
    'currency': '18',
    'subtotal': str(subtotal),
    'fee': str(fee),
    'total': str(total),
    'quantity': str(qty),
    'billing_state': '',
    'save_my_address': '0'
}





cookes = {'timezoneOffset': '14400,0',
     'browserid': '2765828910521038245',
     'sessionid': 'f5b4846f421bc918f22a74c0',
     'steamCountry': 'RU%7C6607ef4ee463b8f05f82c3d839bd63e6',
     'steamLoginSecure': '76561199085391840%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQ1OF8yMzMzQzY4MF9FMkNBMCIsICJzdWIiOiAiNzY1NjExOTkwODUzOTE4NDAiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY5NTMxOTY4OSwgIm5iZiI6IDE2ODY1OTMwODgsICJpYXQiOiAxNjk1MjMzMDg4LCAianRpIjogIjBENEJfMjMzM0M2NkFfRTBGNDgiLCAib2F0IjogMTY5NTIzMzA4OCwgInJ0X2V4cCI6IDE3MTM2MDI2MzYsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICI2Mi4xMTguNzIuNDkiLCAiaXBfY29uZmlybWVyIjogIjMxLjEyOS42NC4xNjAiIH0.4XUzBosVTYqI1QxaITS0bsUBt40SiTrrP6mMHCbnB6yLPExaMZG1leJ3xAKkAgzUGwTe_07HKS_G4Jr38SXfCg',
     'Steam_Language': 'english',
          # 'webTradeEligibility': '%7B%22allowed%22%3A1%2C%22allowed_at_time%22%3A0%2C%22steamguard_required_days%22%3A15'
          #                        '%2C%22new_device_cooldown_days%22%3A0%2C%22time_checked%22%3A1695233210%7D'
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
buylink = 'https://steamcommunity.com/market/buylisting/4395006694800366176'
'''country=UA&language=english&currency=18&item_nameid=2384550&two_factor=0'''
cookebuy={
    'timezoneOffset':'14400,0',
    'browserid':'2765828910521038245',
    'sessionid':'f5b4846f421bc918f22a74c0',
    'steamCountry':'RU%7C6607ef4ee463b8f05f82c3d839bd63e6',
    'steamLoginSecure':'76561199085391840%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQ1OF8yMzMzQzY4MF9FMkNBMCIsICJzdWIiOiAiNzY1NjExOTkwODUzOTE4NDAiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY5NTMxOTY4OSwgIm5iZiI6IDE2ODY1OTMwODgsICJpYXQiOiAxNjk1MjMzMDg4LCAianRpIjogIjBENEJfMjMzM0M2NkFfRTBGNDgiLCAib2F0IjogMTY5NTIzMzA4OCwgInJ0X2V4cCI6IDE3MTM2MDI2MzYsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICI2Mi4xMTguNzIuNDkiLCAiaXBfY29uZmlybWVyIjogIjMxLjEyOS42NC4xNjAiIH0.4XUzBosVTYqI1QxaITS0bsUBt40SiTrrP6mMHCbnB6yLPExaMZG1leJ3xAKkAgzUGwTe_07HKS_G4Jr38SXfCg',
    'Steam_Language':'english',
    'webTradeEligibility':'%7B%22allowed%22%3A1%2C%22allowed_at_time%22%3A0%2C%22steamguard_required_days%22%3A15%2C%22new_device_cooldown_days%22%3A0%2C%22time_checked%22%3A1695233210%7D',
    'strInventoryLastContext':'730_2'
}












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
