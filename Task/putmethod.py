import requests as rq
import json

pUrl = "https://httpbin.org/put"

pHeaders = {
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'User-Name' : "['ARC' , 'Vigo']",
}

pResp = rq.put(url=pUrl, headers=pHeaders)

jsResp = pResp.json()

valueHeader = jsResp['headers'] 

userHeader = valueHeader['User-Name']

print('pResp header:',userHeader)

print('headers type :',type(userHeader))

#Convert into List
conJson = userHeader.replace("'",'"')

#print(conJson, type(conJson))
convertList = json.loads(conJson)

print('convertList = ',convertList)

print('type =',type(convertList))
