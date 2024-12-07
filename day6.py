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
print(hashlib.md5(b"password123").hexdigest())
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
## TASK: source code repo scanner for hardcoded credentials and API keys in files with regex and show findings

# -------------------------------------------------------------------------

# requests
## thm room
## get
## verify=False
## proxies
## TASK: security header checker
## post - data, json
## session
## timeout
## uploading file
## TASK: login brute-force script
## BeautifulSoup
## TASK: implement web scraper