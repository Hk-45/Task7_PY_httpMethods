import requests as rq
import json

psUrl = "https://httpbin.org/post"

psHeaders = {
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'Cmp-Name' : "['ARC','Vigo','TCS']"
}

psResp = rq.post(url=psUrl , headers=psHeaders)

jsResp = psResp.json()

headerValue = jsResp['headers']

userValue = headerValue['Cmp-Name']

print('userValue = ',userValue, 'type = ',type(userValue))

#Convert into List
repValue = userValue.replace("'",'"')

conList = json.loads(repValue)

print('conList = ',conList, 'type =',type(conList))