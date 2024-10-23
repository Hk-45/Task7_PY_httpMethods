import requests as rq
import json

paUrl = "https://httpbin.org/patch"

paHeaders = {
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'Info' : "['Arc','Nagpur','Pune']"
}

paResp = rq.patch(url=paUrl , headers=paHeaders)

jsResp = paResp.json()

userHeader = jsResp['headers']

userValue = userHeader['Info']

print('userValue =',userValue , 'type =',type(userValue))

#Convert into list 
repValue = userValue.replace("'", '"')

conList = json.loads(repValue)

print("conList =",conList, 'type =',type(conList))