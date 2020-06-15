import requests
res=requests.post('http://site.kz/login',json={'login':'login','password':'101299'})
print(res.status_code)