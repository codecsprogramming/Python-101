# python .\tasks\dirbuster.py https://juice-shop.herokuapp.com wordlist.txt html,php
import sys

if len(sys.argv) < 3:
    print("[+] Usage: python dirbuster.py URL WORDLIST [EXTENSIONS]")
    sys.exit()

url = sys.argv[1]
wordlist_path = sys.argv[2]
extensions = sys.argv[3].split(",") if len(sys.argv) == 4 else []
print(url, wordlist_path, extensions)
