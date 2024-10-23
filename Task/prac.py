import requests

deUrl = "https://httpbin.org/delete"

deHeaders = {
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'User-Name' : "['ARC','Vigo']"
}

deResp = requests.delete(url=deUrl, headers= deHeaders)

jsResp = deResp.json()

reHeaders = jsResp['headers']

print('deResp headers =',reHeaders['User-Name'] , 'type =',type(reHeaders['User-Name']))
