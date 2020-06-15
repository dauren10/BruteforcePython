import requests
i=0
while i <100:
    i+=1
    res=requests.get('http://site.kz')
    print(res.status_code)